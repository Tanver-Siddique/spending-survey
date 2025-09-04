# survey.py
import flet as ft
from data import *
import asyncio
import traceback
import re
import requests
import string
import random

# Map spending/assume option ids -> category datasets
CATEGORY_MAP = {
    1: fashion,
    2: accessories,
    3: beauty,
    4: food,
    5: hobbies,
    6: homeDecor,
    7: homeKitchen,
    8: gadget,
    9: babyKids
}


class QuestionManager:
    def __init__(self, page, language="en", on_complete=None):
        self.page = page
        # integration url
        self.APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzcNrbSnmPUtg9A2iP2BlkRsY9Y3Zngi2INJIz33YxJ4t7rZ6Mm4_g3Xm1le_NEYMVsOA/exec"

        self.language = language
        self.questions = list(general_info[language].items())
        self.current_index = 0
        self.answers = {}
        self.on_complete = on_complete
        self.checkboxes = []
        self.is_completed = False

        self.added_categories = []
        self.blocks = []
        self.shown_category_reminders = set()

        self.CATEGORY_LABELS = {
            1: {"en": "Start Fashion Category Questions",      "bn": "ফ্যাশন এর প্রশ্নসমূহ শুরু হচ্ছে"},
            2: {"en": "Start Accessories Category Questions",  "bn": "এক্সেসরিজ এর প্রশ্নসমূহ শুরু হচ্ছে"},
            3: {"en": "Start Beauty Category Questions",       "bn": "বিউটি এর প্রশ্নসমূহ শুরু হচ্ছে"},
            4: {"en": "Start Dry Food Category Questions",     "bn": "শুকনো খাবার এর প্রশ্নসমূহ শুরু হচ্ছে"},
            5: {"en": "Start Hobbies Category Questions",      "bn": "শখ এর প্রশ্নসমূহ শুরু হচ্ছে"},
            6: {"en": "Start Home Decor Category Questions",   "bn": "হোম ডেকর এর প্রশ্নসমূহ শুরু হচ্ছে"},
            7: {"en": "Start Home & Kitchen Category Questions","bn": "বাড়ি ও রান্নাঘর এর প্রশ্নসমূহ শুরু হচ্ছে"},
            8: {"en": "Start Gadgets Category Questions",      "bn": "গ্যাজেট এর প্রশ্নসমূহ শুরু হচ্ছে"},
            9: {"en": "Start Baby & Kids Category Questions",  "bn": "শিশু ও শিশুদের পণ্য এর প্রশ্নসমূহ শুরু হচ্ছে"},
        }

        self.submit_action_container = ft.AnimatedSwitcher(
            content=ft.Container(),
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=300,
        )

        self.other_textfield = ft.TextField(
            visible=False,
            label="Please specify",
            color=ft.Colors.BLACK,
            border_color=ft.Colors.BLUE,
            on_change=self.handle_other_text_change,
        )
        self.other_option_id = None

        self.next_button_controls = ft.ElevatedButton(
            text="Next",
            on_click=self.go_next,
            disabled=True,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
        )
        self.previous_button_controls = ft.ElevatedButton(
            text="Previous",
            on_click=self.go_previous,
            disabled=True,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
        )

        self.progress_bar = ft.ProgressBar(
            value=0, expand=True, color=ft.Colors.BLUE, bgcolor=ft.Colors.GREY_300
        )

        self.question_switcher = ft.AnimatedSwitcher(
            content=ft.Container(),
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=500,
            switch_in_curve=ft.AnimationCurve.EASE_IN_OUT,
            switch_out_curve=ft.AnimationCurve.EASE_IN_OUT,
        )

        self.main_container = ft.Column(
            [
                self.progress_bar,
                self.question_switcher,
                ft.Divider(color=ft.Colors.BLACK, height=5),
                ft.Row(
                    controls=[self.previous_button_controls, self.next_button_controls],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]
        )

        self.show_question()

    # -------------------- helpers --------------------

    async def _show_category_then_start(self, category_key: int, target_index: int):
        """
        Shows a full-white reminder screen with the localized category name for 2 seconds,
        then jumps to target_index and shows the first question of that category.
        """
        try:
            # don't re-show same reminder more than once per session
            if category_key in self.shown_category_reminders:
                self.current_index = target_index
                self.show_question()
                return

            # get localized label (fallback)
            label = self.CATEGORY_LABELS.get(category_key, {}).get(self.language)
            if not label:
                label = f"Category {category_key}"

            # save visibility and hide nav while reminder shows
            prev_prev_vis = getattr(self, "previous_button_controls", None)
            prev_next_vis = getattr(self, "next_button_controls", None)
            if prev_prev_vis is not None:
                prev_prev_vis.visible = False
            if prev_next_vis is not None:
                prev_next_vis.visible = False

            reminder = ft.Container(
                expand=True,
                height=300,
                bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(label, size=25, weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER)
                    ],
                ),
            )

            # show reminder
            self.question_switcher.content = reminder
            self.page.update()

            # wait 2 seconds
            await asyncio.sleep(3)

            # mark shown and restore nav visibility
            self.shown_category_reminders.add(category_key)
            if prev_prev_vis is not None:
                prev_prev_vis.visible = True
            if prev_next_vis is not None:
                prev_next_vis.visible = True

            # jump to the target question and render it
            self.current_index = target_index
            self.show_question()

        except Exception:
            # Prevent unhandled future exceptions and print trace
            traceback.print_exc()
            # fallback: ensure UI doesn't get stuck
            try:
                self.current_index = target_index
                self.show_question()
            except Exception:
                pass



    def _commit_current_answer(self):
        """Saves the current state of inputs into self.answers without navigating."""
        if not self.questions or self.current_index >= len(self.questions):
            return

        qid, qdata = self.questions[self.current_index]

        if qdata["type"] == "checkbox":
            value = [cb.data for cb in self.checkboxes if cb.value]
            # If other option selected, replace the id with the text if provided
            if self.other_option_id is not None and self.other_option_id in value:
                value.remove(self.other_option_id)
                if self.other_textfield.value and self.other_textfield.value.strip():
                    value.append(self.other_textfield.value.strip())
            if value:
                self.answers[qid] = self._normalize_answer(value)
            else:
                # remove answer if nothing selected
                if qid in self.answers:
                    del self.answers[qid]

        elif qdata["type"] == "radio":
            # Radio answers are already recorded by the radio handler, but ensure "Other" text is saved
            answer = self.answers.get(qid)
            if answer is not None and self.other_option_id is not None and answer == self.other_option_id:
                if self.other_textfield.value and self.other_textfield.value.strip():
                    self.answers[qid] = self.other_textfield.value.strip()

    def _normalize_value(self, val):
        """Try to convert numeric-like values to int, otherwise return original."""
        try:
            if isinstance(val, int):
                return val
            if isinstance(val, str) and val.isdigit():
                return int(val)
            return val
        except (ValueError, TypeError):
            return val

    def _normalize_answer(self, val):
        """Normalize a radio value or checkbox list of values."""
        if isinstance(val, list):
            return [self._normalize_value(v) for v in val]
        else:
            return self._normalize_value(val)

    def _add_assume_block(self):
        insert_at = self._index_of_qid("SML3")  # Always insert after SML3
        if insert_at is None:
            return
        if any(b["type"] == "assume" for b in self.blocks):
            return

        self.questions.insert(insert_at + 1, ("AE5T", assume[self.language]["AE5T"]))
        self.blocks.append({"type": "assume", "qids": ["AE5T"], "source": "assume", "category_key": None})

    def _add_category_block(self, category_key: int, source: str, insert_after: str = None):
        if category_key not in CATEGORY_MAP:
            return

        cat = CATEGORY_MAP[category_key]
        qitems = list(cat[self.language].items())
        qids = [qid for qid, _ in qitems]

        if any(qid in dict(self.questions) for qid in qids):
            return

        # Use appropriate insert point based on source
        if insert_after is None:
            insert_after = "SML3" if source == "spending" else "AE5T"

        if insert_after:
            idx = self._index_of_qid(insert_after)
            if idx is not None:
                for offset, item in enumerate(qitems, start=1):
                    self.questions.insert(idx + offset, item)
        else:
            self.questions.extend(qitems)

        self.blocks.append({
            "type": "category",
            "qids": qids,
            "source": source,
            "category_key": category_key
        })

        if category_key not in self.added_categories:
            self.added_categories.append(category_key)

    def _remove_block_containing_qid(self, qid: str):
        block_idx = None
        for i in range(len(self.blocks) - 1, -1, -1):
            if qid in self.blocks[i]["qids"]:
                block_idx = i
                break
        if block_idx is None:
            return False

        block = self.blocks[block_idx]
        indices = [self._index_of_qid(q) for q in block["qids"] if self._index_of_qid(q) is not None]
        if not indices:
            self.blocks.pop(block_idx)
            return False

        start = min(indices)
        end = max(indices)

        for q in block["qids"]:
            if q in self.answers:
                del self.answers[q]

        # pop questions in reverse order to keep indices valid
        for i in range(end, start - 1, -1):
            if i < len(self.questions):
                self.questions.pop(i)

        if block["type"] == "category" and block["category_key"] in self.added_categories:
            try:
                self.added_categories.remove(block["category_key"])
            except ValueError:
                pass

        self.blocks.pop(block_idx)
        self.current_index = max(0, start - 1)
        return True

    def _index_of_qid(self, qid: str):
        for i, (qid_i, _) in enumerate(self.questions):
            if qid_i == qid:
                return i
        return None

    # -------------------- language update --------------------

    def show_contact_entry(self):
        """Show mandatory WhatsApp/Email entry before survey ends."""
        entry_field = ft.TextField(
            label="Enter WhatsApp number or Email",
            autofocus=True,
            width=400,
            border_color=ft.Colors.BLUE,
            color=ft.Colors.BLACK,
        )

        error_text = ft.Text("", color=ft.Colors.RED)

        submit_btn = ft.ElevatedButton(
            text="Submit",
            disabled=True,  # Initially disabled
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
        )

        def is_valid_contact(value: str) -> bool:
            """Check if value is a valid email or WhatsApp number."""
            value = value.strip()
            if not value:
                return False
            if value.isdigit() and len(value) == 11 and value.startswith("01"):
                return True
            # Fixed email regex
            email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
            if re.match(email_regex, value):
                return True
            return False

        def validate_input(e):
            value = entry_field.value.strip()
            valid = is_valid_contact(value)
            submit_btn.disabled = not valid
            if not valid and value:  # Show error only if user typed something invalid
                error_text.value = "Please enter a valid 11-digit number or email."
            else:
                error_text.value = ""
            self.page.update()

        entry_field.on_change = validate_input

        submit_btn.on_click = lambda e: self.page.run_task(
            self._process_final_submission, entry_field, error_text
        )

        self.submit_action_container.content = submit_btn

        self.question_switcher.content = ft.Column(
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value=contact_prompts[self.language],
                    size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK
                ),
                entry_field,
                error_text,
                self.submit_action_container,
            ],
        )

        self.previous_button_controls.visible = False
        self.next_button_controls.visible = False
        self.page.update()

    def update_language(self, new_language):
        """Rebuild the question list in the new language while preserving state."""

        # Store the current question ID before changing anything
        current_qid = None
        if self.questions and 0 <= self.current_index < len(self.questions):
            current_qid = self.questions[self.current_index][0]

        self.language = new_language

        # If survey already completed, show end in the new language
        if self.is_completed:
            self.show_end()
            return

        # If we're on the contact entry page, keep showing it in the new language
        is_on_contact_page = self.previous_button_controls.visible is False and self.next_button_controls.visible is False
        if is_on_contact_page:
            self.show_contact_entry()
            return

        # Commit any in-progress answer before rebuilding
        self._commit_current_answer()

        # Rebuild base questions in the new language (deduplicated)
        base_questions = list(general_info[self.language].items())

        # Only include spending base questions if 4GI answered or there are spending-sourced blocks
        if "4GI" in self.answers or any(b.get("source") == "spending" for b in self.blocks):
            base_questions.extend(list(spending[self.language].items()))

        new_questions = []
        qid_set = set()
        for qid, qdata in base_questions:
            if qid not in qid_set:
                new_questions.append((qid, qdata))
                qid_set.add(qid)

        # Insert spending-based category blocks after SML3 (preserve original blocks order)
        spending_blocks = [b for b in self.blocks if b.get("source") == "spending" and b.get("type") == "category"]
        for block in spending_blocks:
            category_key = block.get("category_key")
            if category_key in CATEGORY_MAP:
                sml3_idx = self._index_of_qid_in_list(new_questions, "SML3")
                if sml3_idx is not None:
                    cat_questions = list(CATEGORY_MAP[category_key][self.language].items())
                    for offset, (qid, qdata) in enumerate(cat_questions, start=1):
                        if qid not in qid_set:
                            new_questions.insert(sml3_idx + offset, (qid, qdata))
                            qid_set.add(qid)

        # Add AE5T if it was answered before or any assume-sourced blocks exist
        if "AE5T" in self.answers or any(b.get("source") == "assume" for b in self.blocks):
            # Heuristic: insert AE5T after the last spending category block if present, else after SML3
            last_category_idx = None
            for i, (qid, _) in enumerate(new_questions):
                if len(qid) == 3 and qid[0].isdigit():
                    last_category_idx = i
            sml3_idx = self._index_of_qid_in_list(new_questions, "SML3")
            insert_idx = (last_category_idx + 1) if last_category_idx is not None else sml3_idx
            if insert_idx is not None and "AE5T" not in qid_set:
                new_questions.insert(insert_idx, ("AE5T", assume[self.language]["AE5T"]))
                qid_set.add("AE5T")

        # Insert assume-based category blocks after AE5T
        assume_blocks = [b for b in self.blocks if b.get("source") == "assume" and b.get("type") == "category"]
        for block in assume_blocks:
            category_key = block.get("category_key")
            if category_key in CATEGORY_MAP:
                ae5t_idx = self._index_of_qid_in_list(new_questions, "AE5T")
                if ae5t_idx is not None:
                    cat_questions = list(CATEGORY_MAP[category_key][self.language].items())
                    for offset, (qid, qdata) in enumerate(cat_questions, start=1):
                        if qid not in qid_set:
                            new_questions.insert(ae5t_idx + offset, (qid, qdata))
                            qid_set.add(qid)

        # --- Ensure SML3 sits right after the general_info block (prevents it being pushed to the end) ---
        gen_count = len(list(general_info[self.language].items()))
        sml3_idx_in_new = self._index_of_qid_in_list(new_questions, "SML3")
        if sml3_idx_in_new is not None:
            sml3_item = new_questions.pop(sml3_idx_in_new)
            insert_pos = min(gen_count, len(new_questions))
            new_questions.insert(insert_pos, sml3_item)

        # --- Preserve END if it existed or if the user was on END before switching language ---
        had_end_before = any(qid == "END" for qid, _ in self.questions) or current_qid == "END"
        if had_end_before and "END" not in qid_set:
            new_questions.append(("END", end[self.language]["END"]))
            qid_set.add("END")

        # Replace the current questions with the rebuilt list
        self.questions = new_questions

        # Try to restore the same question ID in the new list, or choose a sensible fallback
        if current_qid:
            restored_idx = self._index_of_qid_in_list(self.questions, current_qid)
            if restored_idx is not None:
                self.current_index = restored_idx
            else:
                # If they were at END, jump to the END index (we appended it above if needed)
                if current_qid == "END":
                    end_idx = self._index_of_qid_in_list(self.questions, "END")
                    self.current_index = end_idx if end_idx is not None else min(self.current_index, max(0, len(self.questions) - 1))
                # If it was a category question (3 chars starting with digit), try to find a related category position
                elif len(current_qid) == 3 and current_qid[0].isdigit():
                    category_suffix = current_qid[1:3]
                    for i, (qid, _) in enumerate(self.questions):
                        if qid.endswith(category_suffix):
                            self.current_index = i
                            break
                    else:
                        ae5t_idx = self._index_of_qid_in_list(self.questions, "AE5T")
                        if ae5t_idx is not None:
                            self.current_index = ae5t_idx
                        else:
                            sml3_idx = self._index_of_qid_in_list(self.questions, "SML3")
                            self.current_index = sml3_idx if sml3_idx is not None else min(self.current_index, max(0, len(self.questions) - 1))
                else:
                    if current_qid == "AE5T":
                        ae5t_idx = self._index_of_qid_in_list(self.questions, "AE5T")
                        if ae5t_idx is not None:
                            self.current_index = ae5t_idx
                        else:
                            self.current_index = min(self.current_index, max(0, len(self.questions) - 1))
                    else:
                        self.current_index = min(self.current_index, max(0, len(self.questions) - 1))
        else:
            self.current_index = min(self.current_index, max(0, len(self.questions) - 1))

        self.show_question()


    def _index_of_qid_in_list(self, question_list, qid):
        """Helper method to find the index of a question ID in a question list"""
        for i, (qid_i, _) in enumerate(question_list):
            if qid_i == qid:
                return i
        return None

    # -------------------- UI render --------------------
    async def _process_final_submission(self, entry_field: ft.TextField, error_text: ft.Text):
        """Validates contact, shows loading, submits data, and shows end screen."""
        value = entry_field.value.strip()

        # Final validation check
        if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', value) and \
                not (value.isdigit() and len(value) == 11 and value.startswith("01")):
            error_text.value = "Invalid format. Please check your entry."
            self.page.update()
            return

        entry_field.disabled = True
        error_text.value = ""
        self.submit_action_container.content = ft.ProgressRing(width=24, height=24)
        self.page.update()

        # Ensure submission id exists BEFORE sending
        if "Submission_ID" not in self.answers:
            self.answers["Submission_ID"] = self._generate_submission_id()

        self.answers["CONTACT"] = value

        # Submit in a thread (network I/O)
        await asyncio.to_thread(self._submit_data_to_google_sheet)

        # Show the end screen (which will also keep the submission id)
        self.show_end()


    def update_button_states(self):
        self.previous_button_controls.disabled = self.current_index == 0
        if not self.questions or self.current_index >= len(self.questions):
            self.next_button_controls.disabled = True
            self.page.update()
            return

        qid, qdata = self.questions[self.current_index]
        if qdata["type"] == "checkbox":
            is_any_checked = any(cb.value for cb in self.checkboxes)
            self.next_button_controls.disabled = not is_any_checked
        else:  # Radio
            has_answer = qid in self.answers and self.answers[qid] is not None
            self.next_button_controls.disabled = not has_answer

        if self.other_textfield.visible and not self.other_textfield.value.strip():
            self.next_button_controls.disabled = True

        self.page.update()

    def handle_other_text_change(self, e):
        """Handles changes in the 'Others:' text field to update button states."""
        # If other text changed, commit the current answer for radio types immediately
        self.update_button_states()

    def handle_checkbox_change(self, e):
        qid, _ = self.questions[self.current_index]
        if self.other_option_id is not None and e.control.data == self.other_option_id:
            is_now_visible = e.control.value
            self.other_textfield.visible = is_now_visible
            self.other_textfield.autofocus = is_now_visible
            if not is_now_visible:
                self.other_textfield.value = ""

        if qid == "SML3":
            # Exclusive option id 10 was used to mean 'None or other' in prior code
            if e.control.data == 10 and e.control.value:
                for cb in self.checkboxes:
                    if cb.data != 10:
                        cb.value = False
                        if self.other_option_id is not None and cb.data == self.other_option_id:
                            self.other_textfield.visible = False
                            self.other_textfield.autofocus = False
                            self.other_textfield.value = ""
            elif e.control.value:
                for cb in self.checkboxes:
                    if cb.data == 10:
                        cb.value = False

        self.update_button_states()
        self.page.update()

    def record_radio_answer_and_conditionally_next(self, e):
        """
        Records the answer from a radio button and auto-advances.
        It calls go_next, which now contains the special logic for AE5T.
        """
        qid, _ = self.questions[self.current_index]
        # e.control.value will be a string; normalize it to int if numeric
        normalized_value = self._normalize_answer(e.control.value)
        self.answers[qid] = normalized_value
        is_other_selected = (self.other_option_id is not None and normalized_value == self.other_option_id)

        if is_other_selected:
            # Show the other textfield and wait for text entry
            self.other_textfield.visible = True
            self.other_textfield.autofocus = True
            # do not auto-advance; user must type the other value
            self.update_button_states()
            self.page.update()
        else:
            # Clear any previous other text
            self.other_textfield.visible = False
            self.other_textfield.autofocus = False
            self.other_textfield.value = ""
            # ALL radio clicks will now call go_next
            self.go_next(e)

    def create_question_content(self):
        if not self.questions or self.current_index >= len(self.questions):
            return ft.Container(content=ft.Text("Survey finished or error loading question."))

        qid, qdata = self.questions[self.current_index]

        # Reset and check for "Others:" option
        self.other_option_id = None
        self.other_textfield.visible = False
        self.other_textfield.value = ""
        self.other_textfield.autofocus = False  # Reset autofocus state

        # valid_ids are numeric or string ids present in options
        valid_ids = {self._normalize_value(k) for k in qdata["options"].keys()}
        for opt_id, opt_text in qdata["options"].items():
            # A more robust check for "Others"
            if "others:" in opt_text.lower() or "অন্যান্য:" in opt_text.lower():
                self.other_option_id = self._normalize_value(opt_id)
                break

        # State restoration logic
        current_answer = self.answers.get(qid)
        custom_text_from_answer = ""
        is_other_selected_from_answer = False

        if qdata["type"] == "checkbox" and isinstance(current_answer, list):
            for val in current_answer:
                if val not in valid_ids:
                    custom_text_from_answer = str(val)
                    is_other_selected_from_answer = True
                    break
        elif qdata["type"] == "radio" and current_answer is not None:
            if current_answer not in valid_ids:
                custom_text_from_answer = str(current_answer)
                is_other_selected_from_answer = True

        if self.other_option_id is not None and is_other_selected_from_answer:
            self.other_textfield.visible = True
            self.other_textfield.value = custom_text_from_answer

        container = ft.Column(
            spacing=10,
            controls=[
                ft.Markdown(
                    value=qdata["question"],
                    md_style_sheet=ft.MarkdownStyleSheet(
                        p_text_style=ft.TextStyle(color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)
                    ),
                ),
                ft.Divider(height=0,color=ft.Colors.BLACK)
            ],
        )

        options_container = ft.Column(spacing=10, scroll=ft.ScrollMode.ADAPTIVE, expand=True)
        self.checkboxes = []

        # --- CHECKBOX LOGIC ---
        if qdata["type"] == "checkbox":
            current_values = current_answer if isinstance(current_answer, list) else []
            for opt_id, opt_text in qdata["options"].items():
                normalized_id = self._normalize_value(opt_id)
                is_checked = (normalized_id in current_values) or (
                        is_other_selected_from_answer and normalized_id == self.other_option_id)
                cb = ft.Checkbox(
                    label=opt_text,
                    active_color=ft.Colors.BLACK,
                    check_color=ft.Colors.WHITE,
                    border_side=ft.BorderSide(color=ft.Colors.BLUE_GREY_400, width=2),
                    label_style=ft.TextStyle(color=ft.Colors.BLACK, weight=ft.FontWeight.W_400),
                    value=is_checked,
                    data=normalized_id,
                    on_change=self.handle_checkbox_change,
                )
                self.checkboxes.append(cb)
                options_container.controls.append(cb)
        # --- RADIO LOGIC ---
        else:
            radio_value = None
            if current_answer is not None:
                # If the stored answer was other-text, and an other_option_id exists, select that id
                if is_other_selected_from_answer and self.other_option_id is not None:
                    radio_value = str(self.other_option_id)
                else:
                    radio_value = str(self._normalize_value(current_answer))

            radio_group = ft.RadioGroup(
                value=radio_value,
                content=ft.Column(
                    controls=[
                        ft.Radio(
                            value=str(self._normalize_value(opt_id)),
                            fill_color={
                                ft.ControlState.SELECTED: ft.Colors.BLACK,
                                ft.ControlState.DEFAULT: ft.Colors.BLUE_GREY_400,
                            },
                            label=opt_text,
                            label_style=ft.TextStyle(color=ft.Colors.BLACK, weight=ft.FontWeight.W_400),
                        )
                        for opt_id, opt_text in qdata["options"].items()
                    ]
                ),
                on_change=self.record_radio_answer_and_conditionally_next,
            )
            options_container.controls.append(radio_group)

        container.controls.append(ft.Container(content=options_container, expand=True, height=300))
        options_container.controls.append(self.other_textfield)
        return container

    def show_question(self):
        if self.questions:
            total = len(self.questions)
            # keep END included but safe-guard division
            self.progress_bar.value = (self.current_index + 1) / total if total > 0 else 0
        else:
            self.progress_bar.value = 0
        self.question_switcher.content = self.create_question_content()
        self.update_button_states()
        self.page.update()

    # -------------------- navigation --------------------

    def go_next(self, e):
        # Commit current UI state to answers
        self._commit_current_answer()

        if not self.questions or self.current_index >= len(self.questions):
            return

        qid = self.questions[self.current_index][0]

        # --- Add spending questions when user answers 4GI (keeps original behavior) ---
        if qid == "4GI" and "SML3" not in dict(self.questions):
            self.questions.extend(list(spending[self.language].items()))

        # --- Handle SML3 (spending selection) ---
        if qid == "SML3":
            value = self.answers.get(qid, [])

            # remove any previously added spending/assume blocks so we can rebuild
            for block in self.blocks[:]:
                if block.get("source") in ["spending", "assume"]:
                    self._remove_block_containing_qid(block["qids"][0])

            # if 'Others (10)' selected, add AE5T (assume) question
            if 10 in value:
                self._add_assume_block()
                # jump to AE5T if inserted
                ae_idx = self._index_of_qid("AE5T")
                if ae_idx is not None:
                    self.current_index = ae_idx
                    self.show_question()
                    return
            else:
                # add selected categories (numeric options) after SML3
                numeric_options = [opt for opt in value if isinstance(opt, int)]
                added_first_idx = None
                for opt in sorted(numeric_options):
                    if opt in CATEGORY_MAP:
                        self._add_category_block(opt, source="spending", insert_after="SML3")
                        # if this was the first added category, record its first qid index
                        if added_first_idx is None and self.blocks:
                            for b in reversed(self.blocks):
                                if b.get("source") == "spending" and b.get("category_key") == opt:
                                    first_qid = b["qids"][0] if b["qids"] else None
                                    if first_qid:
                                        idx = self._index_of_qid(first_qid)
                                        if idx is not None:
                                            added_first_idx = idx
                                    break
                if added_first_idx is not None:
                    # show reminder for the first added category then start its first question
                    first_cat_key = None
                    # find the block that starts at that qid to learn its category_key
                    first_qid = self.questions[added_first_idx][0]
                    for b in self.blocks:
                        if b.get("type") == "category" and b.get("qids") and b["qids"][0] == first_qid:
                            first_cat_key = b.get("category_key")
                            break
                    if first_cat_key is not None:
                        # run async reminder coroutine
                        self.page.run_task(self._show_category_then_start, first_cat_key, added_first_idx)
                        return
                    else:
                        self.current_index = added_first_idx
                        self.show_question()
                        return

        # --- Handle AE5T (assume selection leading to adding a category) ---
        if qid == "AE5T":
            chosen_key = self.answers.get(qid)

            # Remove previously added *assume* category blocks (but keep AE5T itself)
            for block in self.blocks[:]:
                if block.get("source") == "assume" and block.get("type") == "category":
                    self._remove_block_containing_qid(block["qids"][0])

            # record AE5T index as fallback insertion point
            ae5t_idx = self._index_of_qid("AE5T")

            if chosen_key in CATEGORY_MAP:
                # attempt normal add (this expects AE5T to still be present)
                self._add_category_block(chosen_key, source="assume", insert_after="AE5T")

                # find the expected first qid of this category
                cat = CATEGORY_MAP[chosen_key]
                qitems = list(cat[self.language].items())
                expected_first = qitems[0][0] if qitems else None

                new_idx = self._index_of_qid(expected_first) if expected_first else None

                # fallback: if insertion failed for some reason, insert manually after AE5T
                if new_idx is None and ae5t_idx is not None and qitems:
                    for offset, item in enumerate(qitems, start=1):
                        self.questions.insert(ae5t_idx + offset, item)
                    new_idx = ae5t_idx + 1
                    # ensure we also record the block metadata so other logic works
                    if not any(b for b in self.blocks if b.get("type") == "category" and b.get("category_key") == chosen_key and b.get("source") == "assume"):
                        self.blocks.append({
                            "type": "category",
                            "qids": [qid for qid, _ in qitems],
                            "source": "assume",
                            "category_key": chosen_key
                        })
                        if chosen_key not in self.added_categories:
                            self.added_categories.append(chosen_key)

                if new_idx is not None:
                    # if we know the chosen category key, show its reminder first
                    if isinstance(chosen_key, int) and chosen_key in CATEGORY_MAP:
                        # schedule reminder using chosen_key and new_idx (NOT first_cat_key)
                        if hasattr(self.page, "run_task"):
                            self.page.run_task(self._show_category_then_start, chosen_key, new_idx)
                        else:
                            asyncio.create_task(self._show_category_then_start(chosen_key, new_idx))
                        return
                    # fallback: directly show the inserted question
                    self.current_index = new_idx
                    self.show_question()
                    return

        # --- If current question is the last in a category block, jump to next after that block ---
        if self._is_last_question_in_category(qid):
            next_idx = self._get_next_index_after_category()
            if next_idx is not None:
                # if the next index starts a category block, show that category reminder first
                next_qid = self.questions[next_idx][0]
                next_block = None
                for b in self.blocks:
                    if b.get("type") == "category" and b.get("qids") and b["qids"][0] == next_qid:
                        next_block = b
                        break

                if next_block and next_block.get("category_key") is not None:
                    cat_key = next_block["category_key"]
                    # show reminder then start next category
                    self.page.run_task(self._show_category_then_start, cat_key, next_idx)
                    return
                else:
                    self.current_index = next_idx
                    self.show_question()
                    return

        # --- Standard forward navigation ---
        if self.current_index < len(self.questions) - 1:
            self.current_index += 1
            self.show_question()
        else:
            # Append END if not present, then show contact/end flows as appropriate
            if "END" not in dict(self.questions):
                self.questions.append(("END", end[self.language]["END"]))
                self.current_index += 1
                self.show_question()
            elif "CONTACT" not in self.answers:
                self.show_contact_entry()
            else:
                self.show_end()


    def _is_last_question_in_category(self, qid):
        """Check if the current question is the last in its category block"""
        for block in self.blocks:
            if qid in block["qids"]:
                # Check if this is the last question in the block
                return block["qids"][-1] == qid
        return False

    def _get_next_index_after_category(self):
        """Find the index of the next question after the current category block"""
        if not self.questions or self.current_index >= len(self.questions):
            return None

        current_qid = self.questions[self.current_index][0]

        # Find which block contains the current question
        for block in self.blocks:
            if current_qid in block["qids"]:
                # Find the last question in this block
                last_qid_in_block = block["qids"][-1]

                # Find the index of the last question in this block
                last_idx = self._index_of_qid(last_qid_in_block)
                if last_idx is not None and last_idx < len(self.questions) - 1:
                    # Return the index after the last question in the block
                    return last_idx + 1
                break

        return None


    def go_previous(self, e):
        self._commit_current_answer()

        # Check if current_index is valid
        if self.current_index <= 0 or self.current_index >= len(self.questions):
            return

        block_to_remove = None
        for b in self.blocks:
            # Check if current_index is still valid before accessing
            if self.current_index < len(self.questions) and self.questions[self.current_index][0] in b["qids"]:
                if self.questions[self.current_index][0] == b["qids"][0]:
                    block_to_remove = b
                break
        if block_to_remove:
            source_qid = "SML3" if block_to_remove["source"] == "spending" else "AE5T"
            idx_before_block = self._index_of_qid(source_qid)
            self._remove_block_containing_qid(block_to_remove["qids"][0])
            self.current_index = idx_before_block if idx_before_block is not None else self.current_index - 1
        else:
            self.current_index -= 1

        # Ensure current_index is within valid range
        self.current_index = max(0, min(self.current_index, len(self.questions) - 1))
        self.show_question()

    # -------------------- end page --------------------

    def create_end_content(self):
        submission_id = self.answers.get("Submission_ID", "N/A")
        answer_controls = [ft.Text(f"Your Submission ID: {submission_id}", size=14, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)]
        for qid, ans in self.answers.items():
            if qid == "Submission_ID":
                continue
            src = None
            if qid in general_info[self.language]:
                src = general_info
            elif qid in spending[self.language]:
                src = spending
            elif qid in assume[self.language]:
                src = assume
            elif qid == "END":
                src = end
            elif qid == "CONTACT":
                answer_controls.append(ft.Text(f"Contact: {ans}", size=14, color=ft.Colors.GREY_800))
                continue
            else:
                for cat in CATEGORY_MAP.values():
                    if qid in cat[self.language]:
                        src = cat
                        break
            if not src:
                continue
            qtext = src[self.language][qid]["question"].replace("**", "")
            opts = src[self.language][qid]["options"]
            if isinstance(ans, list):
                ans_text = ", ".join([str(opts.get(a, a)) for a in ans])
            else:
                ans_text = opts.get(ans, str(ans))
            answer_controls.append(ft.Text(f"{qtext}\n  -> {ans_text}", size=14, color=ft.Colors.GREY_800))
        return answer_controls

    def _generate_submission_id(self, length=4):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def _submit_data_to_google_sheet(self):
        if not self.APPS_SCRIPT_URL or "YOUR_UNIQUE_URL_HERE" in self.APPS_SCRIPT_URL:
            return

        # Ensure we always have a submission id
        if "Submission_ID" not in self.answers:
            self.answers["Submission_ID"] = self._generate_submission_id()
        submission_id = self.answers.get("Submission_ID")

        answered_categories = set()
        category_prefixes = {
            "FA": "Fashion", "AC": "Accessories", "BS": "Beauty", "PF": "Food",
            "HO": "Hobbies", "HD": "HomeDecor", "HK": "HomeKitchen", "EG": "Gadget",
            "BK": "BabyKids"
        }
        # iterate safely over keys
        for qid in list(self.answers.keys()):
            prefix = None
            if len(qid) >= 2 and qid[:2] in category_prefixes:
                prefix = qid[:2]
            elif len(qid) >= 3 and qid[1:3] in category_prefixes:
                prefix = qid[1:3]
            if prefix:
                answered_categories.add(category_prefixes[prefix])

        payload = {
            "submissionID": submission_id,
            "categories": list(answered_categories),
            "answers": self.answers
        }

        try:
            response = requests.post(self.APPS_SCRIPT_URL, json=payload, timeout=10)
            response.raise_for_status()
            try:
                response_data = response.json()
            except ValueError:
                response_data = {"status": "unknown", "raw_text": response.text}
            return response_data  # return so caller can handle
        except requests.exceptions.RequestException:
            return {"status": "error", "message": "Failed to send data"}


    def show_end(self):
        # Mark completed
        self.is_completed = True

        # Ensure there is a submission id
        if "Submission_ID" not in self.answers:
            submission_id = self._generate_submission_id()
            self.answers["Submission_ID"] = submission_id

        # Ensure END exists in the question list (so language-switch and restore can find it)
        if "END" not in dict(self.questions):
            self.questions.append(("END", end[self.language]["END"]))
        # Move current_index to END
        end_idx = self._index_of_qid("END")
        if end_idx is not None:
            self.current_index = end_idx
        else:
            # Fallback - set to last index
            self.current_index = max(0, len(self.questions) - 1)

        # Update progress
        self.progress_bar.value = 1.0

        # Build and show end content
        end_content = ft.Column(
            scroll=ft.ScrollMode.AUTO, expand=True, height=300,
            controls=[
                ft.Text("Thank you for completing the survey!" if self.language == "en" else "জরিপটি সম্পূর্ণ করার জন্য আপনাকে ধন্যবাদ!",
                        size=22, color=ft.Colors.GREEN, text_align=ft.TextAlign.CENTER,
                        ),
                ft.Divider(),
                ft.Text("Final Answers:" if self.language == "en" else "চূড়ান্ত উত্তর:",
                        size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK,
                        ),
                *self.create_end_content(),
            ],
        )
        self.question_switcher.content = end_content
        self.previous_button_controls.visible = False
        self.next_button_controls.visible = False
        self.page.update()
        if self.on_complete:
            self.on_complete()


def general_info_questions(page, language, on_complete=None):
    return QuestionManager(page, language, on_complete)
