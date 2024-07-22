.. _contribute:

Contribute
##########

Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/how-to/contributing.html>`_ topic
in the *PyAnsys developer's guide*. Ensure that you are thoroughly familiar
with this guide before attempting to contribute to PyAnsys Quarto Cheat Sheet.

The following contribution information is specific to PyAnsys Quarto Cheat Sheet.

Install in developer mode
-------------------------

Installing PyAnsys Quarto Cheat Sheet in developer mode allows you to modify
and enhance the source.

To clone and install the latest version of PyAnsys Quarto Cheat Sheet in
development mode, run these commands:

.. code::

    git clone https://github.com/ansys/pyansys-quarto-cheatsheet.git
    cd pyansys-quarto-cheatsheet

    # Install the package in development mode
    quarto install extension . --no-prompt


Adhere to code style
--------------------

PyAnsys Quarto Cheat Sheet follows the PEP8 standard as outlined in
`PEP 8 <https://dev.docs.pyansys.com/coding-style/pep8.html>`_ in
the *PyAnsys developer's guide* and implements style checking using
`pre-commit <https://pre-commit.com/>`_.

To ensure your code meets minimum code styling standards, run these commands::

  pip install pre-commit
  pre-commit run --all-files

You can also install this as a pre-commit hook by running this command::

  pre-commit install

This way, it's not possible for you to push code that fails the style checks::

  $ pre-commit install
  $ git commit -am "feat: Added my cool features"
  check yaml...............................................................Passed
  trim trailing whitespace.................................................Passed
  fix end of files.........................................................Passed
  check for merge conflicts................................................Passed
  Validate GitHub Workflows................................................Passed
  Add License Headers......................................................Passed

Render a cheat sheet
--------------------
.. note::

  To render a cheat sheet to a PDF file locally, you must have Quarto installed. For
  installation information, see `Getting Started <https://quarto.org/docs/getting-started/installation.html>`_
  in the Quarto documentation.

To render a cheat sheet to a PDF file, run a command like this one::

  quarto render examples/cheat_sheet.qmd

The preceding command saves the PDF file for the ``cheat_sheet.qmd`` file in
the ``Examples`` directory to the ``doc/_build`` directory by default. If you
want to change the output directory, you can modify the ``_quarto.yml`` file.
For more information, see :ref:`quarto-yml`.

Build the documentation
-----------------------
To build the documentation locally, you must run this command to install the
documentation dependencies in the ``requirements_docs.txt`` file in the ``requirements``
directory::

  pip install -r requirements/requirements_doc.txt

Then, navigate to the ``doc`` directory and run this command

.. tab-set::

    .. tab-item:: Linux/macOS

        .. code::

            make html

    .. tab-item:: Windows

        .. code::

            ./make.bat html

The documentation is built in the ``doc/_build/html`` directory.

You can clean the documentation build by running this command:

.. tab-set::

    .. tab-item:: Linux/macOS

        .. code::

            make clean

    .. tab-item:: Windows

        .. code::

            ./make.bat clean

Post issues
-----------

Use the `PyAnsys Quarto Cheat Sheet Issues <https://github.com/ansys/pyansys-quarto-cheatsheet/issues>`_
page to report bugs and request new features. When possible, use the issue templates provided.
If your issue does not fit into one of these templates, click the link for opening a blank issue.

If you have general questions about the PyAnsys ecosystem, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.
If your question is specific to PyAnsys Quarto Cheat Sheet, ask your question in an issue as described
in the previous paragraph.
