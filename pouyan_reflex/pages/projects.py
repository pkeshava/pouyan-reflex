# Project definitions

import reflex as rx
from rxconfig import config
from ..general.component_designs import *

def create_project_image(image_alt, image_src):
    """Create an image element for a project with custom styling."""
    return rx.image(
        src=image_src,
        alt=image_alt,
        height="12rem",
        object_fit="cover",
        width="100%",
    )

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



## ------------

def projects() -> rx.Component:
    return rx.box(

        create_projects_section()

    )
