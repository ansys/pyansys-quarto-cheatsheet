# PyAnsys quarto cheat sheet format


## Installation

To use this extension, you must have [Quarto](https://quarto.org/docs/getting-started/installation.html) installed.

### Install the extension

**From the github repository:**

From main branch:

```bash
quarto use ansys-internal/pyansys-quarto-cheatsheet@main
```

From a specific release:

```bash
quarto use ansys-internal/pyansys-quarto-cheatsheet@v0.1.0
```

**From the archive file:**

Download the cheat_sheet.zip or cheat_sheet.tar.gz file from the
[releases page](https://github.com/ansys-internal/pyansys-quarto-cheatsheet/releases) and run the following command:

```bash
quarto use cheat_sheet.zip
```
or
```bash
quarto use cheat_sheet.tar.gz
```

This command installs the extension in the quarto environment and creates
a ``_extensions`` directory in the current directory containing the extension files.

## Usage

```bash
quarto render examples/cheat_sheet.qmd --to cheat_sheet-pdf
```
## Format options

- **version**: Specifies the version of the cheat sheet.
```yaml
version: 0.1
```
- **title**: Sets the title of the cheat sheet.
```yaml
title: PyMAPDL cheat sheet
```
- **footer**: Defines the footer text.
```yaml
footer: PyMAPDL cheat sheet
```
- **footerlinks**:  Specifies a list of links to display in the footer.
Each link should have a ``url`` and ``text``.
```yaml
footerlinks:
- urls: https://mapdl.docs.pyansys.com/version/stable/
  text: PyMAPDL Documentation
```
- **format**: Determines the format of the cheat sheet. For PDF generation, use  `cheat_sheet-pdf`.
```yaml
format: cheat_sheet-pdf
```
- **execute**: Controls the code output in the code cell. Refer to the
[quarto documentation](https://quarto.org/docs/reference/cells/cells-knitr.html#code-output)
for available options.

  - *eval*: If set to `false`, the code will not be executed.
    ```yaml
    execute:
      eval: false
    ```
  - *echo*: If set to `false`, the code will not be displayed in the output.
    ```yaml
    execute:
      echo: false
    ```
  - *output*: If set to `false`, the output of the code will not be displayed.
    ```yaml
    execute:
      output: false
    ```
### Example of a cheat sheet configuration file

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
> utilize the `eval`, `echo`and similar options within the code cell.
>  ```
> #| eval: false
>
> #| echo: false
>  ```

> [!IMPORTANT]
> The output of the code cell is displayed by default. To disable the output, use the `execute` option.
>
> To disable the output of individual or multiple code cells,
> utilize the `output` option within the code cell.
>  ```
> #| output: false
>  ```

### ``_quarto.yml`` file
The `_quarto.yml` file is a configuration file that contains all the metadata at the project level.
Refer to the [quarto documentation project](https://quarto.org/docs/projects/quarto-projects.html#project-metadata)
for more information.

if you want to change the output directory, add the following line to the `_quarto.yml` file.
```yaml
output_dir: _build
```
example of [``_quarto.yml``](_quarto.yml) file is placed in the current directory.


## Example

Example of a [cheat_sheet.qmd](cheat_sheet.qmd) file is placed in the current directory.
Example of complete cheat sheet for pymapdl is placed in [pymapdl cheat sheet](examples/pymapdl_cheat_sheet_example.qmd) file.
To render the pymapdl example cheat sheet, run the following command:
```bash
quarto render examples/pymapdl_cheat_sheet_example.qmd
```
> [!TIP]
> If you want to open a `.qmd` file in Jupyter Notebook, follow these steps:
> 1. Install `jupytext` by running the command: `pip install jupytext`
> 2. Install `jupyter` by running the command: `pip install jupyter`
> 3. Open the `.qmd` file in Jupyter Notebook with the command: `jupyter notebook cheat_sheet.qmd`
