# PyAnsys Quarto Cheat Sheet

PyAnsys Quarto Cheat Sheet is an extension for using [Quarto](https://quarto.org/), an open
source scientific and technical publishing system, to render cheat sheets from plain text
markdown.

## Prerequisites

Before you can use PyAnsys Quarto Cheat Sheet, you must have Quarto installed. For installation
information, see [Getting Started](https://quarto.org/docs/getting-started/installation.html) in
the Quarto documenation.

## Installation

You can install PyAnsys Quarto Cheat Sheet from the GitHub repository or an
archive file.

### Install from the GitHub repository

From the GitHub repository, you can install the latest version of PyAnsys Quart Cheat Sheet
from the main branch or install a version from a specific release branch.

To install the latest version from the main branch, run this command:

```bash
quarto use ansys-internal/pyansys-quarto-cheatsheet@main
```

To install the version from a specific release branch, rather than using ``@main``, use
the release branch:

```bash
quarto use ansys-internal/pyansys-quarto-cheatsheet@v0.1.0
```

### Install from an archive file

To install from an archive file, first download the `cheat_sheet.zip` or `cheat_sheet.tar.gz`
archive file from the repsitory's [Releases](https://github.com/ansys-internal/pyansys-quarto-cheatsheet/releases)
page.

Then, run the command that installs PyAnsys Quarto Cheat Sheet in the Quarto environment from
the ZIP or TAR.GZ file. The command creates an ``_extensions`` directory in the current
directory with all the extension's files.

For a ZIP file, run this command:

```bash
quarto use cheat_sheet.zip
```

For a TAR.GZ file, run this command:

```bash
quarto use cheat_sheet.tar.gz
```

## Usage

To render a cheat sheet as a PDF file, you run this command:

```bash
quarto render examples/cheat_sheet.qmd --to cheat_sheet-pdf
```

## Format options

The YAML configuration file for the cheat sheet specifies the
format options:

- **version**: Version of the cheat sheet.
```yaml
version: 0.1
```
- **title**: Title of the cheat sheet.
```yaml
title: PyMAPDL cheat sheet
```
- **footer**: Footer text of the cheat sheet.
```yaml
footer: PyMAPDL cheat sheet
```
- **footerlinks**:  List of links to display in the footer.
Each link must have a ``urls`` and ``text`` option.
```yaml
footerlinks:
- urls: https://mapdl.docs.pyansys.com/version/stable/
  text: PyMAPDL documentation
```
- **format**: Format for rendering the cheat sheet. For PDF generation, use `cheat_sheet-pdf`.
```yaml
format: cheat_sheet-pdf
```
- **execute**: Controls code and cell output. While descriptions for key options follow, see
[Code Cells: Knitr](https://quarto.org/docs/reference/cells/cells-knitr.html)
in the Quarto documentation for descriptions of all available options.

  - *eval*: Whether to evaluate code cells. If `False`, only echos the code into the output.
    ```yaml
    execute:
      eval: false
    ```
  - *echo*: Whether to include cell source code in rendered output.
    ```yaml
    execute:
      echo: false
    ```
  - *output*: Whether to include the results of executing the code in the output.
    ```yaml
    execute:
      output: false
    ```

## Example of a cheat sheet configuration file

```yaml
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
```

> [!NOTE]
> By default, code cells are executed. To disable execution, use the `execute` option.
>
> To disable execution and display of individual or multiple code cells,
> use the `eval`, `echo`, and similar options within the code cell:

>  ```
> #| eval: false
>
> #| echo: false
>  ```

> [!IMPORTANT]
> The output of the code cell is displayed by default. To disable the output, use the `execute` option.
>
> To disable the output of individual or multiple code cells,
> use the `output` option within the code cell:

>  ```
> #| output: false
>  ```

## The `_quarto.yml` file

The `_quarto.yml` file is a configuration file that contains all the metadata at the project level.
For more information, see the [quarto documentation project](https://quarto.org/docs/projects/quarto-projects.html#project-metadata).

If you want to change the output directory, add the following line to the `_quarto.yml` file:

```yaml
output_dir: _build
```

An example of a [_quarto.yml](_quarto.yml) file is placed in the current directory.

## Example

An example of a [cheat_sheet.qmd](cheat_sheet.qmd) file is placed in the current directory.
An example of a complete cheat sheet for PyMAPDL is placed in the [pymapdl_cheat_sheet_example_qmd](examples/pymapdl_cheat_sheet_example.qmd) file.

To render the PyMAPDL example cheat sheet, run this command:

```bash
quarto render examples/pymapdl_cheat_sheet_example.qmd
```

> [!TIP]
> If you want to open a `.qmd` file in Jupyter Notebook, follow these steps:
> 1. Install `jupytext` by running this command: `pip install jupytext`
> 2. Install `jupyter` by running this command: `pip install jupyter`
> 3. Open the `.qmd` file in Jupyter Notebook by running this command: `jupyter notebook cheat_sheet.qmd`
