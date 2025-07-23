# 📄 [Demo](https://github.com/tschm/ppp1/blob/draft/document.pdf)

[![LaTeX](https://github.com/tschm/ppp1/actions/workflows/latex.yml/badge.svg)](https://github.com/tschm/ppp1/actions/workflows/latex.yml)
[![Created with qCradle](https://img.shields.io/badge/Created%20with-qCradle-blue?style=flat-square)](https://github.com/tschm/paper)

<!-- Add your arXiv badge here when available -->
<!-- [![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)-->

## 📋 Table of Contents

- [Abstract](#-abstract)
- [Link to a companion Python package](#-link-to-a-companion-python-package)
- [Features](#-features)
- [Getting started](#-getting-started)
  - [Customize the README.md file](#-customize-the-readmemd-file)
  - [Edit the LaTeX document](#️-edit-the-latex-document)
  - [Repository Tags and Headers](#️-repository-tags-and-headers)
  - [Viewing Your Document](#-viewing-your-document)
  - [Installation and Setup](#️-installation-and-setup)
- [Contributing](#-contributing)
- [License](#-license)

## 📝 Abstract

This project provides a comprehensive LaTeX template for academic
papers with automated build and release processes.
It features customizable headers, environment variable integration,
GitHub Actions workflows for continuous integration, and a streamlined
development workflow using Tectonic for reliable LaTeX compilation.

## 🔗 Link to a companion Python package

<!-- Update this link to your actual companion package if available -->
Companion [Python package](https://github.com/tschm)

## ✨ Features

- **Modern LaTeX Setup**: Uses Tectonic for reliable, reproducible builds
- **Automated Workflows**: GitHub Actions for continuous integration and releases
- **Smart Headers**: Automatically includes version information in document headers
- **Customizable**: Easy to adapt for your specific academic paper needs
- **Clean Design**: Professional formatting with sensible defaults

## 🚀 Getting started

### **📋 Customize the README.md file**

Update this README with your project-specific information:

- Add your project's abstract
- Update links to your companion packages or resources
- Add any additional sections relevant to your project

### **✏️ Edit the LaTeX document**

The main LaTeX file is `paper/document.tex`.
Edit this file to add your content.
We use [tectonic](https://github.com/tectonic-typesetting/tectonic)
to compile LaTeX files. The resulting PDF documents are automatically released
to the [draft branch](https://github.com/tschm/ppp1/tree/draft)
of the repository.

### **🏷️ Repository Tags and Headers**

The document can display metadata in the header, providing important context
about your document's version and status.

#### **Automated Headers**

Both in `latex.yml` and `release.yml` workflows, we create a file `header.txt`
that contains either the Git commit SHA (for regular builds)
or the release tag (for releases).
This metadata is automatically included in the document header,
making it easy to:

- Track which version of the document you're viewing
- Reference specific versions in discussions
- Maintain proper versioning for academic submissions

#### **Custom Headers**

You can also create your own `header.txt` file in the paper
directory to include custom text
in the document header without modifying the LaTeX code.
This is useful for:

- Adding draft status indicators
- Including review information
- Noting special instructions for reviewers

### **🔍 Viewing Your Document**

The title at the top of this README (marked with 📄)
links to your compiled document in the draft branch.
This provides an easy way to access the latest version
of your document without having to download the PDF file.

### **⚙️ Installation and Setup**

#### Prerequisites

Before you begin, ensure you have:

- A Unix-like environment (Linux, macOS, or WSL on Windows)
- Git installed
- Basic familiarity with command-line operations

#### Setup

To set up the development environment:

1. **Install Tectonic**:

    ```bash
    make install
    ```

2. **Compile the document**:

    ```bash
    make compile
    ```

3. **Clean up generated files**:

   ```bash
   make clean
   ```

For more details on available commands, run:

```bash
make help
```

## 🤝 Contributing

Contributions to improve this LaTeX template are welcome! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add some amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

Please make sure your code follows the existing style and includes appropriate documentation.

## 📄 License

This project is licensed under the MIT License - see
the [LICENSE](LICENSE) file for details.

---

Created with ❤️ using [qCradle](https://github.com/tschm/paper)
