# main.py
import flet as ft
import asyncio
from Title_animation import GradientAnimatedTextContainer
from data import start_text

class Survey(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(bgcolor=ft.Colors.BLACK, expand=True, padding=5)
        self.page = page
        self.language = "bn"
        self.current_page = "intro"
        self.question_manager = None
        self.is_completed = False

        # Initialize title text
        self.title_text = GradientAnimatedTextContainer(
            value="Desires After Duties",
            font_family="title_font",
            no_wrap=False
        )

        # Language selector
        self.language_slider = ft.SegmentedButton(
            selected={"1"},
            allow_multiple_selection=False,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
            segments=[
                ft.Segment(value="0", label=ft.Text("Eng")),
                ft.Segment(value="1", label=ft.Text("বাংলা")),
            ],
            on_change=self.change_language,
            col={"xs": 6, "sm": 3, "md": 2, "lg": 2},
        )

        # Main content area
        self.main_content_controls = ft.Column(
            spacing=8, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.main_content_container_column = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            col={"xs": 12, "sm": 12, "md": 4, "lg": 4},
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    bgcolor=ft.Colors.WHITE,
                                    padding=ft.padding.all(10),
                                    content=self.main_content_controls,
                                )
                            ],
                        )
                    ],
                )
            ],
        )

        # Main layout
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Divider(color=ft.Colors.TRANSPARENT, height=5),
                ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            col={"xs": 12},
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[self.title_text],
                        )
                    ],
                ),
                ft.Divider(color=ft.Colors.TRANSPARENT, height=10),
                ft.ResponsiveRow(
                    controls=[self.language_slider],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=False,
                ),
                ft.Divider(height=5, color=ft.Colors.TRANSPARENT),
                self.main_content_container_column,
            ],
        )

        # Don't refresh content here - wait until after the control is added to the page
        self.initialized = False

    def initialize_content(self):
        """Initialize content after the control is added to the page"""
        if not self.initialized:
            self._refresh_content()
            self.initialized = True

    def _create_intro_controls(self):
        t = start_text[self.language]
        return [
            ft.Text(
                value=t["welcome"],
                size=25,
                font_family="Arial",
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_GREY_900,
            ),
            ft.Text(value=t["request"], size=20, color=ft.Colors.BLUE_GREY_500),
            ft.Text(
                value=t["description"],
                size=12,
                color=ft.Colors.BLACK,
                text_align=ft.TextAlign.JUSTIFY,
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    ft.Row(
                        spacing=4,
                        controls=[
                            ft.Icon(name=ft.Icons.TIMER_ROUNDED, color=ft.Colors.BLACK),
                            ft.Text(
                                value=t["time"],
                                weight=ft.FontWeight.BOLD,
                                size=12,
                                color=ft.Colors.BLACK,
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=4,
                        controls=[
                            ft.Icon(
                                name=ft.Icons.ENHANCED_ENCRYPTION_ROUNDED,
                                color=ft.Colors.BLACK,
                            ),
                            ft.Text(
                                value=t["anonymous"],
                                weight=ft.FontWeight.BOLD,
                                size=12,
                                color=ft.Colors.BLACK,
                            ),
                        ],
                    ),
                ],
            ),
            ft.Divider(),
            ft.ElevatedButton(
                text=t["button"],
                bgcolor=ft.Colors.BLUE_GREY_200,
                color=ft.Colors.BLACK,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                on_click=self.clicked_start_survey,
            ),
        ]

    def _create_questionnaire_controls(self):
        try:
            from survey import general_info_questions
            
            if self.question_manager is None:
                self.question_manager = general_info_questions(
                    self.page, self.language, on_complete=self.on_survey_complete
                )
                return [self.question_manager.main_container]
            else:
                self.question_manager.update_language(self.language)
                return [self.question_manager.main_container]
        except Exception as e:
            import traceback
            print(f"Error loading questionnaire: {str(e)}")
            traceback.print_exc()
            return [
                ft.Text("Error loading survey. Please check the console for details.", color="red"),
                ft.ElevatedButton(
                    "Retry",
                    on_click=lambda e: self._refresh_content()
                )
            ]

    def _refresh_content(self):
        self.main_content_controls.controls.clear()
        if self.current_page == "intro":
            self.main_content_controls.controls.extend(self._create_intro_controls())
        elif self.current_page == "questionnaire":
            self.main_content_controls.controls.extend(self._create_questionnaire_controls())
        
        # Only update if the control is properly initialized
        if self.initialized:
            self.page.update()

    def on_survey_complete(self):
        self.is_completed = True
        print("Survey completed!")

    def change_language(self, e):
        selected_value = list(e.control.selected)[0]
        self.language = "en" if selected_value == "0" else "bn"
        self._refresh_content()

    def on_view_change(self, e):
        # Responsive title size
        size = 50
        if self.page.width < 600:
            size = 25
        elif self.page.width < 900:
            size = 40
        if hasattr(self.title_text, "text_control"):
            self.title_text.text_control.size = size
        self.page.update()

    def clicked_start_survey(self, e):
        self.current_page = "questionnaire"
        self._refresh_content()


# --------- MAIN ENTRY POINT ----------
def main(page: ft.Page):
    page.title = "Survey"
    page.spacing = 0
    page.padding = 0
    page.fonts = {
        "title_font": "ZenDots-Regular.ttf"
    }

    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color={
                ft.ControlState.HOVERED: ft.Colors.BLACK,
                ft.ControlState.DEFAULT: ft.Colors.BLACK87,
            },
            track_color=ft.Colors.GREY_800,
            thickness=10,
            radius=5,
            interactive=True,
        )
    )
    
    # Create and add survey
    survey_container = Survey(page)
    page.on_resized = survey_container.on_view_change
    page.add(survey_container)
    
    # Initialize content after adding to page
    survey_container.initialize_content()
    
    # Animate gradient
    if hasattr(survey_container.title_text, "animate_gradient_task"):
        page.run_task(survey_container.title_text.animate_gradient_task)
    survey_container.on_view_change(None)


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
    )