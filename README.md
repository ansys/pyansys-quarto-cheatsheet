# PyAnsys quarto chetsheet format


## Installation

```bash
quarto use ansys-internal/pyansys-quarto-cheatsheet
```
This will install the extension and create an example qmd file that you can use as a starting place for your article.

## Usage

```bash
quarto render cheatsheet.qmd --to cheatsheet-pdf
```
## Format options

- **version**: Version of the cheatsheet
- **title**: Title of the cheatsheet
- **footer**: Footer text
```yaml
version: 0.1
title: PyMAPDL Cheatsheet
footer: PyMAPDL Cheatsheet
```
- **footerlinks**: List of links to be displayed in the footer. it has two keys urls and text. urls is the 
link to the page and text is the text to be displayed in the footer.
example:
```yaml
footerlinks:
- urls: https://mapdl-docs.pyansys.com/version/stable/
  text: PyMAPDL Documentation
```
**format**: Format of the cheatsheet. To use this extension for pdf, the format should be `cheatsheet-pdf`
```yaml
format: cheatsheet-pdf
```
**execute**: If set to true, the code blocks will be executed and the output will be displayed in the pdf.
```yaml



## Example

Example of a cheatsheet.qmd file is placed in the current directory.


