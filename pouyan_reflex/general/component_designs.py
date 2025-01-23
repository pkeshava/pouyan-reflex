import reflex as rx

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

def create_paragraph(paragraph_text):
    """Create a paragraph element with custom text color."""
    return rx.text(paragraph_text, color="#4B5563")


def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


# ---------------------------------------------------------
# Contact form #
# ---------------------------------------------------------


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
