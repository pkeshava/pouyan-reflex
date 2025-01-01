"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_nav_link(link_url, link_text):
    """Create a navigation link with hover effects."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover={"color": "#1F2937"},
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        color="#4B5563",
    )


def create_large_heading(margin_bottom, heading_text):
    """Create a large heading (h2) with custom styling."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom=margin_bottom,
        font_size="1.875rem",
        line_height="2.25rem",
        color="#1F2937",
        as_="h2",
    )


def create_medium_heading(margin_bottom, heading_text):
    """Create a medium-sized heading (h3) with custom styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom=margin_bottom,
        color="#1F2937",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_icon(icon_class):
    """Create an icon element with a specified class name."""
    return rx.el.i(class_name=icon_class)


def create_social_link(
    hover_style, icon_color, link_url, icon_class
):
    """Create a social media link with an icon and hover effect."""
    return rx.el.a(
        create_icon(icon_class=icon_class),
        href=link_url,
        target="_blank",
        rel="noopener noreferrer",
        _hover=hover_style,
        color=icon_color,
    )


def create_project_image(image_alt, image_src):
    """Create an image element for a project with custom styling."""
    return rx.image(
        src=image_src,
        alt=image_alt,
        height="12rem",
        object_fit="cover",
        width="100%",
    )


def create_paragraph(paragraph_text):
    """Create a paragraph element with custom text color."""
    return rx.text(paragraph_text, color="#4B5563")


def create_project_description(
    project_title, project_description
):
    """Create a project description box with title and text."""
    return rx.box(
        create_medium_heading(
            margin_bottom="0.5rem",
            heading_text=project_title,
        ),
        create_paragraph(
            paragraph_text=project_description
        ),
        padding="1rem",
    )


def create_project_card(
    image_alt, image_src, project_title, project_description
):
    """Create a project card with image, title, and description."""
    return rx.box(
        create_project_image(
            image_alt=image_alt, image_src=image_src
        ),
        create_project_description(
            project_title=project_title,
            project_description=project_description,
        ),
        background_color="#ffffff",
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_form_label(label_text):
    """Create a form label with custom styling."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="700",
        margin_bottom="0.5rem",
        color="#374151",
    )


def create_form_input(input_id, input_name, input_type):
    """Create a form input element with custom styling and focus effects."""
    return rx.el.input(
        type=input_type,
        id=input_id,
        name=input_name,
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


def create_form_field(
    label_text, input_id, input_name, input_type
):
    """Create a form field with label and input."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_form_input(
            input_id=input_id,
            input_name=input_name,
            input_type=input_type,
        ),
        margin_bottom="1rem",
    )


def create_header():
    """Create the header section with navigation links."""
    return rx.flex(
        rx.heading(
            "Pouyan Keshavarzian, Ph.D.",
            font_weight="700",
            color="#1F2937",
            font_size="1.25rem",
            line_height="1.75rem",
            as_="h1",
        ),
        rx.box(
            create_nav_link(
                link_url="#about", link_text="About"
            ),
            create_nav_link(
                link_url="#projects", link_text="Projects"
            ),
            create_nav_link(
                link_url="#contact", link_text="Contact"
            ),
            create_nav_link(
                link_url="blog.html", link_text="Blog"
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
        create_large_heading(
            margin_bottom="1rem", heading_text="About Me"
        ),
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


def create_projects_section():
    """Create the Projects section with multiple project cards."""
    return rx.box(
        create_large_heading(
            margin_bottom="1.5rem", heading_text="Projects"
        ),
        rx.box(
            create_project_card(
                image_alt="Project 1",
                image_src="https://placehold.co/400x200?text=Project+1",
                project_title="Project 1",
                project_description="A brief description of Project 1 and its key features.",
            ),
            create_project_card(
                image_alt="Project 2",
                image_src="https://placehold.co/400x200?text=Project+2",
                project_title="Project 2",
                project_description="A brief description of Project 2 and its key features.",
            ),
            create_project_card(
                image_alt="Project 3",
                image_src="https://placehold.co/400x200?text=Project+3",
                project_title="Project 3",
                project_description="A brief description of Project 3 and its key features.",
            ),
            gap="1.5rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                    "1024px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
        id="projects",
        margin_bottom="3rem",
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
        create_projects_section(),
        rx.box(
            create_large_heading(
                margin_bottom="1.5rem",
                heading_text="Contact Me",
            ),
            create_contact_form(),
            id="contact",
            margin_bottom="3rem",
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





app = rx.App()
app.add_page(index)
