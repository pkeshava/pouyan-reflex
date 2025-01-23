from ..pages.blog import blog
from ..pages.projects import projects
from ..general.component_designs import *
import reflex as rx

from rxconfig import config
class State(rx.State):
    """The app state."""

    ...


def create_header():
    """Create the header section with navigation links."""
    return rx.flex(
        rx.box(
            "Pouyan Keshavarzian, Ph.D.",
            font_weight="500",
            color="#1F2937",
            # font_size="1.25rem",
            # line_height="1.75rem",
            #as_="h1",
            #class_name="max-w-xs rounded-full"
        ),
        rx.box(
            create_nav_link(
                link_url="#about", link_text="About"
            ),
            create_nav_link(
                link_url="/projects", link_text="Projects"
            ),
            create_nav_link(
                link_url="#contact", link_text="Contact"
            ),
            create_nav_link(
                link_url="/blog", link_text="Blog"
            ),
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )




def create_header_container():
    """Create a container for the header with responsive styling."""
    return rx.box(
        rx.box(
            create_header(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
            padding_top="0.75rem",
            padding_bottom="0.75rem",
        ),
        background_color="#ffffff",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_about_content():
    """Create the content for the About Me section, including social links."""
    return rx.box(
        # create_large_heading(
        #     margin_bottom="1rem", heading_text="About Me"
        # ),
        rx.text(
            "Mixed-signal integrated circuit designer. Scientific researcher. Avid python and Julia tool developer.",
            margin_bottom="1rem",
            color="#4B5563",
        ),
        rx.flex(
            create_social_link(
                hover_style={"color": "#1E40AF"},
                icon_color="#2563EB",
                link_url="https://www.linkedin.com/in/keshavarzian/",
                icon_class="fa-2x fa-linkedin fab",
            ),
            create_social_link(
                hover_style={"color": "#4B5563"},
                icon_color="#1F2937",
                link_url="https://github.com/pkeshava",
                icon_class="fa-2x fa-github fab",
            ),
            create_social_link(
                hover_style={"color": "#065F46"},
                icon_color="#059669",
                link_url="https://scholar.google.com/citations?user=nVpmtE8AAAAJ&hl=en",
                icon_class="fa-2x fa-graduation-cap fas",
            ),
            display="flex",
            column_gap="1rem",
        ),
    )


def create_about_section():
    """Create the complete About Me section with image and content."""
    return rx.flex(
        rx.image(
            src="/photo4.png",
            height="12rem",
            margin_bottom=rx.breakpoints(
                {"0px": "1rem", "768px": "0"}
            ),
            object_fit="cover",
            border_radius="9999px",
            width="12rem",
            margin_right=rx.breakpoints({"768px": "2rem"}),
        ),
        create_about_content(),
        display="flex",
        flex_direction=rx.breakpoints(
            {"0px": "column", "768px": "row"}
        ),
        align_items="center",
    )




def create_message_textarea():
    """Create a textarea for the contact form message."""
    return rx.el.textarea(
        id="message",
        name="message",
        rows="4",
        required=True,
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
    )


def create_submit_button():
    """Create a submit button for the contact form."""
    return rx.el.button(
        "Send Message",
        type="submit",
        background_color="#3B82F6",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        font_weight="700",
        _hover={"background-color": "#2563EB"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
    )


def create_contact_form():
    """Create the complete contact form with fields and submit button."""
    return rx.form(
        create_form_field(
            label_text="Name",
            input_id="name",
            input_name="name",
            input_type="text",
        ),
        create_form_field(
            label_text="Email",
            input_id="email",
            input_name="email",
            input_type="email",
        ),
        rx.box(
            create_form_label(label_text="Message"),
            create_message_textarea(),
            margin_bottom="1rem",
        ),
        create_submit_button(),
        max_width="32rem",
        margin_left="auto",
        margin_right="auto",
    )


def create_main_content():
    """Create the main content area including About, Projects, and Contact sections."""
    return rx.box(
        rx.box(
            create_about_section(),
            id="about",
            margin_bottom="3rem",
        ),
        # rx.box(
        #     create_large_heading(
        #         margin_bottom="1.5rem",
        #         heading_text="Contact Me",
        #     ),
        #     create_contact_form(),
        #     id="contact",
        #     margin_bottom="3rem",
        # ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_footer():
    """Create the footer section with copyright information."""
    return rx.box(
        rx.box(
            rx.text(
                "© 2025 Pouyan Keshavarzian. All rights reserved."
            ),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
            text_align="center",
        ),
        background_color="#1F2937",
        padding_top="1rem",
        padding_bottom="1rem",
        color="#ffffff",
    )