# ✨ Ailuntz - Personal CV CLI Tool

An **elegant, cool, and practical** personal CV command-line tool. Display your beautiful resume in the terminal with a simple `cv` command.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![Node](https://img.shields.io/badge/node-12.0+-green.svg)

English | [简体中文](README.zh-CN.md)

## 🎯 Features

- 🎨 **Cool Interface** - Beautiful terminal UI crafted with ANSI color codes
- 🚀 **Quick Installation** - Support both pip and npm installation methods
- 💼 **Complete Display** - Showcase personal info, skills, education, project experience, etc.
- 🌈 **Cross-platform** - Support Windows, macOS, Linux
- ⚡ **Lightweight** - No additional dependencies, ready to use out of the box

## 📦 Installation

### Option 1: Install via pip (Python)

```bash
# Install
pip3 install ailuntz

# Run
ailuntz cv
```

### Option 2: Install via npm (Node.js)

```bash
# Install
npm install -g @ailuntz/cli

# Run
ailuntz cv
```

## 🚀 Usage

After installation, simply run the following command in your terminal to view your CV:

```bash
ailuntz cv
```

### ⚠️ Troubleshooting

**macOS shows "command not found: ailuntz"**

Python package installation path is not in PATH, solution:

```bash
# Add to PATH
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Or run with python -m
python3 -m ailuntz cv
```

## 💻 Local Development

### Python Version

```bash
# Enter Python directory
cd python

# Install in development mode
pip install -e .

# Run test
ailuntz cv
```

### Node.js Version

```bash
# Enter Node.js directory
cd nodejs

# Install dependencies (if needed)
npm install

# Test run
npm test

# Or run directly
node bin/cv.js
```

## 📁 Project Structure

```
cli.ailuntz.com/
├── README.md              # Main documentation (English)
├── README.zh-CN.md        # Chinese documentation
├── redeme.md             # Project introduction (Chinese)
├── python/               # Python version
│   ├── ailuntz/
│   │   ├── __init__.py
│   │   └── cli.py        # CLI main program
│   ├── setup.py          # setuptools configuration
│   ├── pyproject.toml    # Modern Python project configuration
│   └── MANIFEST.in       # Package manifest
└── nodejs/               # Node.js version
    ├── package.json      # npm package configuration
    ├── index.js          # Main module
    └── bin/
        └── cv.js         # CLI entry point
```

## 🛠️ Publishing

### Publish to PyPI

```bash
cd python

# Create virtual environment and install build tools
python3 -m venv .venv
source .venv/bin/activate
pip install build twine

# Build package
python -m build

# Upload to PyPI (register at https://pypi.org first)
twine upload dist/*
```

### Publish to npm

```bash
cd nodejs

# Login to npm (register at https://www.npmjs.com first)
npm login

# Publish (scoped packages need --access public)
npm publish --access public
```

## 🎨 Customization

You can modify the CV content according to your needs:

### Python Version
Edit the `print_cv()` function in `python/ailuntz/cli.py`

### Node.js Version
Edit the `printCV()` function in `nodejs/bin/cv.js`

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

## 👤 Author

**Ailuntz**

- Website: [https://ailuntz.com](https://ailuntz.com)
- GitHub: [@ailuntz](https://github.com/ailuntz)

## 🤝 Contributing

Issues and Pull Requests are welcome!

## ⭐ Star History

If this project helps you, please give it a Star ⭐️

---

<p align="center">Made with ❤️ by Ailuntz</p>