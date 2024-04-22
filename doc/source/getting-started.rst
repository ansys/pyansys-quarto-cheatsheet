Getting started and basic usage
===============================

.. include:: ../../README.md
   :parser: myst_parser.sphinx_
   :start-after: # PyAnsys quarto cheat sheet format
   :end-before: > [!NOTE]


.. note::

    By default, code cells are executed. To disable execution, use the `execute` option.
    To turn off execution and display of individual or multiple code cells, utilize the `execute` option within the code cell.

    .. code-block:: python
        :linenos:

        #| execute: false
        #| eval: false

.. important::

    The output of the code cell is displayed by default. To turn off the output, use the `execute` option.

    To disable the output of individual or multiple code cells,
    utilize the `output` option within the code cell.

    .. code-block:: python
        :linenos:

        #| output: false

``_quarto.yml`` file
--------------------

The `_quarto.yml` file is a configuration file that contains all the metadata at the project level.
Refer to the `quarto documentation project <https://quarto.org/docs/projects/quarto-projects.html#project-metadata>`_
for more information.

if you want to change the output directory, add the following line to the `_quarto.yml` file.

.. code-block:: yaml

    output_dir: _build

if you want to clean the latex output, add the following line to the `_quarto.yml` file.

.. code-block:: yaml

    latex-clean: true
