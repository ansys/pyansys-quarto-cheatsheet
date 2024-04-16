"""Sphinx documentation configuration file."""

from datetime import datetime
import os

from ansys_sphinx_theme import (
    ansys_favicon,
    get_version_match,
    pyansys_logo_black,
)
from sphinx.builders.latex import LaTeXBuilder

from ansys.urlinclude import __version__

LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]

# Project information
project = "pyansys-quarto-cheat-sheet"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "curly-adventure-yr7kw1w.pages.github.io")

# Select desired logo, theme, and declare the html title
html_logo = pyansys_logo_black
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "PyAnsys Quarto Cheat Sheet"
html_favicon = ansys_favicon

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/ansys-internal/pyansys-quarto-cheatsheet",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "check_switcher": False,
}

# Sphinx extensions
extensions = [
    "sphinx_design",
    "myst_parser",
]

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"
