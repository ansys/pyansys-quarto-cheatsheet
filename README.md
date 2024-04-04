# PyAnsys quarto chetsheet format


## Installation

```bash
quarto use ansys-internal/pyansys-quarto-cheatsheet
```
This command installs the extension and generates an example `.qmd` file that
serves as a starting point for your article.

## Usage

```bash
quarto render cheatsheet.qmd --to cheatsheet-pdf
```
## Format options

- **version**: Specifies the version of the cheatsheet.
```yaml
version: 0.1
```
- **title**: Sets the title of the cheatsheet.
```yaml
title: PyMAPDL Cheatsheet
```
- **footer**: Defines the footer text.
```yaml
footer: PyMAPDL Cheatsheet
```
- **footerlinks**:  Specifies a list of links to display in the footer.
Each link should have a ``url`` and ``text``.
```yaml
footerlinks:
- urls: https://mapdl-docs.pyansys.com/version/stable/
  text: PyMAPDL Documentation
```
- **format**: Determines the format of the cheatsheet. For PDF generation, use  `cheatsheet-pdf`.
```yaml
format: cheatsheet-pdf
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


## Example

Example of a [cheatsheet.qmd](cheatsheet.qmd) file is placed in the current directory.
