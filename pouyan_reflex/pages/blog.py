import reflex as rx
from rxconfig import config
import os

def read_html_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def blog() -> rx.Component:
    html_content=read_html_from_file("/Users/pouyan/Desktop/builds/2025projects/pouyan-reflex/assets/bubble_plot.html")
    return rx.box(
            rx.html(html_content),
            border_radius="2px",
            width=rx.breakpoints(
                initial="50%",  # mobile
                sm="50%",       # tablet
                lg="50%"        # desktop
            ),
            margin="auto",
            padding=["1em", "2em", "3em"],  # responsive padding
            overflow="auto"
        )

    