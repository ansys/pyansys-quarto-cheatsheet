.. _cheat_sheet_example:

Examples
========

The `cheat_sheet.qmd <https://github.com/ansys-internal/pyansys-quarto-cheatsheet/blob/main/examples/cheat_sheet.qmd>`_
file in the ``Examples`` directory is a simple QMD file that you can use as a template for creating
your own cheat sheets.

.. literalinclude:: ../../examples/cheat_sheet.qmd
    :language: md

To use PyAnsys Quarto Cheat Sheet to render this QMD file as a cheat sheet in PDF format, run this command:

.. code-block:: bash

    quarto render cheat_sheet.qmd


Output
------

The rendered cheat sheet is saved as the ``cheat_sheet.pdf`` file in the same directory as the QMD file.

You can download the PDF file of this cheat sheet by clicking the following link:

.. button-link:: https://quarto-cheat-sheet.docs.pyansys.com/version/dev/_static/cheat_sheet.pdf
    :color: info

    Rendered PDF file :octicon:`download;1em`
