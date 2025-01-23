#"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .pages.landing_page import *
from .pages.projects import *

class AppConfig(rx.Config):
    pass


config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={},
)

def index():
    """Create the complete portfolio page structure."""
    return rx.fragment(
        create_stylesheet_link(
            stylesheet_url="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
        create_stylesheet_link(
            stylesheet_url="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
        ),
        rx.box(
            create_header_container(),
            create_main_content(),
            create_footer(),
            background_color="#F3F4F6",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
    )



app = rx.App(stylesheets=[
        "/bootstrap.css",  # This path is relative to assets/
    ],)
app.add_page(index)
app.add_page(blog)
app.add_page(projects)

