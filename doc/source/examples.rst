Examples
========

The following example is a simple ``.qmd`` file that uses PyAnsys Quarto Cheat Sheet
to render a cheat sheet for a PyAnsys module.

.. literalinclude:: ../../examples/cheat_sheet.qmd
    :language: md

To render the cheat sheet, run this command:

.. code-block:: bash

    quarto render cheat_sheet.qmd


Output
------

The rendered cheat sheet is saved as ``cheat_sheet.pdf`` in the same directory as the input file.

You can download the rendered cheat sheet by clicking the following link:

.. button-link:: _static/cheat_sheet.pdf
    :ref-type: ref
    :color: info
    :align: center

    Rendered PDF :octicon:`download;1em`
