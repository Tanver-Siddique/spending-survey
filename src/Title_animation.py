# In your Title_animation.py file

import flet as ft
import asyncio
import random


def get_random_color():
    """Generates a random hex color string."""
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"


class GradientAnimatedTextContainer(ft.Container):
    def __init__(self, value: str, size: float = 70,
                 font_family: str = "Arial", no_wrap: bool = False):
        super().__init__()

        self.text_control = ft.Text(
            value=value,
            size=size,
            font_family=font_family,
            text_align=ft.TextAlign.CENTER,
            # --- CORRECTED: Use no_wrap=False
            no_wrap=no_wrap,
        )

        self.content = ft.ShaderMask(
            content=self.text_control,
            blend_mode=ft.BlendMode.SRC_IN,
            shader=ft.LinearGradient(
                begin=ft.alignment.Alignment(-1.5, 0),
                end=ft.alignment.Alignment(0.5, 0),
                colors=[ft.Colors.CYAN_700, ft.Colors.ORANGE_300, ft.Colors.CYAN_700],
                stops=[0.0, 0.5, 1.0]
            )
        )

    async def animate_gradient_task(self):
        begin_x = -1.5
        end_x = 0.5
        step = 0.02
        moving_right = True

        while True:
            if moving_right:
                begin_x += step
                end_x += step
                if begin_x >= 1.5:
                    moving_right = False
            else:
                begin_x -= step
                end_x -= step
                if end_x <= -0.5:
                    moving_right = True

                    self.content.shader.colors = [
                        get_random_color(),
                        get_random_color(),
                        get_random_color()
                    ]

            self.content.shader.begin = ft.alignment.Alignment(begin_x, 0)
            self.content.shader.end = ft.alignment.Alignment(end_x, 0)
            self.update()
            await asyncio.sleep(0.016)