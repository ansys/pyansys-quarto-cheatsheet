User guide
==========

To render a cheat sheet to a PDF file locally, you run a command like this one:

.. code-block:: bash

     quarto render examples/cheat_sheet.qmd --to cheat_sheet-pdf


The preceding command saves the PDF file for the ``cheat_sheet.qmd`` file in
the ``Examples`` directory to the ``doc/_build`` directory by default. If
you want to change the output directory, you can modify the ``_quarto.yml``
file. For more information, see :ref:`quarto-yml`.

Format options
--------------

The YAML configuration file for a cheat sheet specifies format options:

- ``version``: Version of the cheat sheet::

   version: 0.1

- ``title``: Title of the cheat sheet::

   title: PyMAPDL cheat sheet

- ``footer``: Footer text of the cheat sheet::

   footer: PyMAPDL cheat sheet

- ``footerlinks``: List of links to display in the footer of the cheat sheet.
  Each link must have a ``urls`` and ``text`` option::

   footerlinks:
   - urls: https://mapdl.docs.pyansys.com/version/stable/
     text: PyMAPDL documentation

- ``format``: Format for rendering the cheat sheet. For PDF generation, use ``cheat_sheet-pdf``::

   format: cheat_sheet-pdf

- ``execute``: Controls code and cell output. While descriptions for key options follow, see
  `Code Cells: Knitr <https://quarto.org/docs/reference/cells/cells-knitr.html>`_ in the Quarto
  documentation for descriptions of all available options.

  - ``eval``: Whether to evaluate code cells. If ``False``, the code is only echoed in the output::

      execute:
        eval: false

  - ``echo``: Whether to include cell source code in the output::

      execute:
        echo: false

  - ``output``: Whether to include the results of executing the code in the output::

      execute:
        output: false


Configuration file example
--------------------------

Here is an example of a YAML configuration file::

   version: 0.1
   title: PyMAPDL cheat sheet
   footer: PyMAPDL cheat sheet
   footerlinks:
   - urls: https://mapdl.docs.pyansys.com/version/stable/
     text: PyMAPDL Documentation
   format: cheat_sheet-pdf
   execute:
     eval: false
     echo: false
     output: false


By default, code cells are executed. To disable execution, for the ``execute`` option,
set ``eval: false``.

To disable execution and exclude the cell source code in the output,
use the ``eval``, ``echo``, and similar options within the code cell::

   #| eval: false
   #| echo: false


By default, the results of executing the code are included in the output. To exclude these
results, for the ``execute`` option, set ``output: false``.

.. _quarto-yml:

The ``_quarto.yml`` file
------------------------

As indicated in `Project Metadata <https://quarto.org/docs/projects/quarto-projects.html#project-metadata>`_
in the Quarto documentation, all Quarto projects include a ``_quarto.yml`` configuration file. Any document
rendered within the project directory automatically inherit the metadata defined at the project level.

The root directory of the PyAnsys Cheat Sheet repository includes an example of a
 `_quarto.yml <https://github.com/ansys-internal/pyansys-quarto-cheatsheet/blob/main/_quarto.yml>`_ file.

To change the directory that PDF files for cheat sheets are saved to, you would modify this line::

   latex-output-dir: _build


Other example files
~~~~~~~~~~~~~~~~~~~

A Quarto QMD file is a format used for integrating plain text markdown and code into a single
compiled document. The ``Examples`` directory contains these QMD files:

- The `cheat_sheet.qmd <https://github.com/ansys-internal/pyansys-quarto-cheatsheet/blob/main/examples/cheat_sheet.qmd>`_
  file is a template that you can use to create your own cheat sheets.
- The `pymapdl_cheat_sheet_example_qmd <https://github.com/ansys-internal/pyansys-quarto-cheatsheet/blob/main/examples/pymapdl_cheat_sheet_example.qmd>`_
  file is an example of a PyMAPDL cheat sheet.

To render the example of a PyMAPDL cheat sheet, run this command::

   quarto render examples/pymapdl_cheat_sheet_example.qmd


.. tip::
   If you want to open a QMD file in Jupyter Notebook, follow these steps:

   #. Install the ``jupytext`` package by running this command: ``pip install jupytext``
   #. Install the ``jupyter`` package by running this command: ``pip install jupyter``
   #. Open the QMD file in Jupyter Notebook by running this command: ``jupyter notebook cheat_sheet.qmd``
