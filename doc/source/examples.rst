Examples
========

The following example is a simple ``.qmd`` file that uses the ``pyansys-quarto-cheat-sheet``
package to create a cheat sheet for the PyAnsys module.

.. literalinclude:: ../../examples/cheat_sheet.qmd
    :language: md

To render the cheat sheet, run the following command:

.. code-block:: bash

    quarto render cheat_sheet.qmd

The rendered cheat sheet will be saved as ``cheat_sheet.pdf`` in the same directory as the input file.
To see

.. button-link:: _static/cheat_sheet.pdf
    :ref-type: ref

    Rendered pdf
