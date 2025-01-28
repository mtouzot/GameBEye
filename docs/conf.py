# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import importlib.metadata
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------
project = "gamebeye"
copyright = "2021 - 2025, Martin TOUZOT"
author = "Martin TOUZOT"

# The full version, including alpha/beta/rc tags
version = importlib.metadata.version(project)
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx_favicon",
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "vcs_pageview_mode": "raw",
    "style_nav_header_background": "#2980B9",
    "flyout_display": "hidden",
    "version_selector": True,
    "language_selector": True,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": False,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = "_static/icon/logo.svg"

html_css_files = ["css/custom.css"]

# A favicon
favicons = [
    "icon/favicon.ico",  # => `_static/icon/favicon.ico`
    "icon/favicon-16x16.png",
    "icon/favicon-32x32.png",
    "icon/android-chrome-192x192.png",
    "icon/android-chrome-512x512.png",
    "icon/apple-touch-icon.png",
]


# Add custom CSS file
def setup(app):
    app.add_css_file("css/custom.css")
