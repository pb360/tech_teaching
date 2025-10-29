"""
Utility helpers for Jupyter-based workshops.

Currently exposes a `generate_toc_nb` function that builds a Markdown
table of contents for the active notebook, skipping headings deeper than
the supplied level.
"""

from __future__ import annotations

import os
import re
from typing import Optional

import nbformat
import ipykernel
import requests
from IPython.display import Markdown, display
import jupyter_server.serverapp as notebookapp


def get_current_notebook_name() -> Optional[str]:
    """Best-effort lookup of the active notebook's filename."""
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split("-", 1)[1].split(".")[0]

    for srv in notebookapp.list_running_servers():
        try:
            response = requests.get(
                os.path.join(srv["url"], "api/sessions"),
                params={"token": srv.get("token", "")},
                timeout=5,
            )
            for sess in response.json():
                if sess["kernel"]["id"] == kernel_id:
                    return sess["notebook"]["path"].split("/")[-1]
        except Exception:
            continue

    return None


def generate_toc_nb(nb_name: Optional[str] = None, skip_level: int = 3) -> None:
    """
    Display a Markdown table of contents for the current notebook.

    Parameters
    ----------
    nb_name:
        Explicit notebook filename. When omitted the function tries to
        detect the active notebook via the running server.
    skip_level:
        Highest heading depth to include (1 = H1, 2 = H2, etc.).
    """
    if nb_name is None:
        nb_name = get_current_notebook_name()

    if nb_name is None or not os.path.exists(nb_name):
        display(Markdown("_Unable to locate the notebook for TOC generation._"))
        return

    with open(nb_name, encoding="utf-8") as handle:
        nb = nbformat.read(handle, as_version=4)

    toc = []
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        for line in cell.source.split("\n"):
            if not line.strip().startswith("#"):
                continue

            level = line.count("#")
            if level > skip_level:
                continue

            title = line.strip("# ").strip()
            anchor = re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")
            toc.append(f"{'  ' * (level - 1)}* [{title}](#{anchor})")

    if toc:
        display(Markdown("\n".join(toc)))
    else:
        display(Markdown("_Add Markdown headings to populate the table of contents._"))


__all__ = ["generate_toc_nb", "get_current_notebook_name"]
