import flet
from flet import IconButton, Page, Row, TextField, icons, theme, colors, border_radius,Container, Text

# from testeFlet2 import get_indice

def main(page: Page):
    page.title = "Calc App"
    result = Text(value="0", color=colors.WHITE, size=20)
    page.window_width = 350
    page.window_height = 350
    page.horizontal_alignment = "center"
    page.bgcolor = "#FFFFFF"
    page.add(
        Container(
            width=100,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20
        )
     )

flet.app(target=main)