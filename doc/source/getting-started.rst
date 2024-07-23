Getting started
===============

This section explains how to install PyAnsys Quarto Cheat Sheet in user mode. If you are
interested in contributing to PyAnsys Quarto Cheat Sheet, see :ref:`contribute` for information
on installing in developer mode.

Prerequisites
-------------

Before you can use PyAnsys Quarto Cheat Sheet, you must have Quarto installed. For installation
information, see `Getting Started <https://quarto.org/docs/getting-started/installation.html>`_ in
the Quarto documentation.

Installation
------------

You can install PyAnsys Quarto Cheat Sheet from the GitHub repository or from an
archive file.

Install from the GitHub repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the GitHub repository, you can install the latest version of PyAnsys Quart Cheat Sheet
from the main branch or install a version from a specific release branch.

- To install the latest version from the main branch, run this command:

  .. code-block:: bash

     quarto add ansys/pyansys-quarto-cheatsheet@main


- To install the version from a specific release branch, rather than using ``@main``, use
  the release branch, such as ``@v1``:


  .. code-block:: bash

     quarto add ansys/pyansys-quarto-cheatsheet@v1


Install from an archive file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install from an archive file:

#. Download the ``cheat_sheet.zip`` or ``cheat_sheet.tar.gz`` archive file from the
   repository's `Releases <https://github.com/ansys/pyansys-quarto-cheatsheet/releases>`_
   page.

#. Run the command that installs PyAnsys Quarto Cheat Sheet in the Quarto environment from
   the ZIP or TAR.GZ file.

   The command that you run creates an ``_extensions`` directory in the current directory
   with all the files for PyAnsys Quarto Cheat Sheet.

   - For a ZIP file, run this command:

     .. code-block:: bash

        quarto use cheat_sheet.zip


   - For a TAR.GZ file, run this command:

     .. code-block:: bash

         quarto use cheat_sheet.tar.gz
