Contribute
##########

Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/how-to/contributing.html>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar
with this guide before attempting to contribute to PyAnsys Quarto Cheat Sheet.

The following contribution information is specific to PyAnsys Quarto Cheat Sheet.

Clone the repository
--------------------

To clone and install the latest PyAnsys Quarto Cheat Sheet in development mode, run
these commands:

.. code::

    git clone https://github.com/ansys-internal/pyansys-quarto-cheatsheet.git
    cd pyansys-quarto-cheatsheet

    # Install the package in development mode
    quarto install extension . --no-prompt


Post issues
-----------

Use the `PyAnsys Quarto Cheat Sheet Issues <https://github.com/ansys-internal/pyansys-quarto-cheatsheet/issues>`_
page to submit questions, report bugs, and request new features.

To reach the project support team, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

View documentation
------------------

Documentation for the latest stable release of PyAnsys Quarto Cheat Sheet is hosted at
`PyAnsys Quarto Cheat Sheet Documentation <https://quarto-cheat-sheet.docs.pyansys.com>`_.

In the upper right corner of the documentation's title bar, there is an option
for switching from viewing the documentation for the latest stable release
to viewing the documentation for the development version or previously
released versions.

Adhere to code style
--------------------

PyAnsys Quarto Cheat Sheet implements style checking using
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


Build the cheat sheet
---------------------
.. note::

  To build cheat sheet PDF locally, you must have `quarto <https://quarto.org/docs/getting-started/installation.html>`_ installed.

To build the cheat sheet PDF, run this command::

  quarto render examples/cheat_sheet.qmd

The cheat sheet PDF is built in the ``_build`` directory
since the output directory is set to ``_build`` in the ``_quarto.yml`` file.
if you want to change the output directory, you can change it in the ``_quarto.yml`` file.

Build the documentation
-----------------------
To build the documentation locally, you must run this command to install the
documentation dependencies in requirements_docs.txt in requirements directory::

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
