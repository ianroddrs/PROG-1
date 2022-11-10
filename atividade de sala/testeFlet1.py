import flet
from flet import IconButton, Page, Row, TextField, icons, theme, colors, border_radius,Container, Text

from CadastraTelefone.main import programa

programa()

def main(page: Page):
    page.title = "Calc App"
    result = Text(value="0", color=colors.WHITE, size=20)
    page.window_width = 550
    page.window_height = 550
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

flet.app(target=main, view=flet.WEB_BROWSER)