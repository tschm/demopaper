# 📄 [Demo](https://github.com/tschm/ppp1/blob/draft/document.pdf)

[![LaTeX](https://github.com/tschm/ppp1/actions/workflows/latex.yml/badge.svg)](https://github.com/tschm/ppp1/actions/workflows/latex.yml)
[![Created with qCradle](https://img.shields.io/badge/Created%20with-qCradle-blue?style=flat-square)](https://github.com/tschm/paper)

Remove or update the arxiv link

[![arXiv](https://img.shields.io/badge/arXiv-2305.19484-b31b1b.svg)](https://arxiv.org/abs/2305.19484)

## 📝 Abstract

Include an abstract here...

## 🔗 Link to a companion Python package

Please correct the link as you wish

Companion [Python package](https://github.com/tschm)

## 🚀 Getting started

### **📋 Update the README.md file**

Insert your abstract, add graphs, etc.

### **✏️ Update the ppp1.tex file**

Write some beautiful content and commit the file.
We are using [tectonic](https://github.com/tectonic-typesetting/tectonic)
to compile your files. The resulting pdf documents are released
to the [draft branch](https://github.com/tschm/ppp1/tree/draft)
of the repo.

### **🏷️ Repository Tags**

The document can display a repository tag in the header.
This tag is read from the `REPO_TAG` environment variable during compilation:

- When building locally: Set the `REPO_TAG` environment variable
before running `make compile`

  ```bash
  REPO_TAG="v1.0.0" make compile
  ```

- In GitHub Actions: The tag is automatically set from the workflow
input during releases

If the `REPO_TAG` environment variable is not set, no tag will
be displayed in the document header.

Additionally, if a file named `header_text.txt` exists in the paper directory,
its contents will be included in the header. This allows you to add custom text
to the header without modifying the LaTeX code.

### **🔍 Click on the header of your README.md file**

The header links to your compiled document.
