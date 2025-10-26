# ✨ Ailuntz - Personal CV CLI Tool

一个**优雅、炫酷、实用**的个人简介命令行工具。通过简单的 `cv` 命令即可在终端中展示精美的个人简历。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![Node](https://img.shields.io/badge/node-12.0+-green.svg)

## 🎯 特性

- 🎨 **炫酷界面** - 使用 ANSI 颜色代码打造精美的终端界面
- 🚀 **快速安装** - 支持 pip 和 npm 两种安装方式
- 💼 **完整展示** - 展示个人信息、技能、教育背景、项目经历等
- 🌈 **跨平台** - 支持 Windows、macOS、Linux
- ⚡ **轻量级** - 无需额外依赖，开箱即用

## 📦 安装

### 方式一：通过 pip 安装（Python）

```bash
# 安装
pip install ailuntz

# 运行
ailuntz cv
```

### 方式二：通过 npm 安装（Node.js）

```bash
# 安装
npm install -g @ailuntz/cli

# 运行
ailuntz cv
```

## 🚀 使用方法

安装完成后，在终端中输入以下命令即可查看个人简历：

```bash
ailuntz cv
```

### ⚠️ 常见问题

**macOS 提示 "command not found: ailuntz"**

Python 包安装路径不在 PATH 中，解决方法：

```bash
# 添加到 PATH
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 或使用 python -m 方式运行
python3 -m ailuntz cv
```

## 💻 本地开发

### Python 版本

```bash
# 进入 Python 目录
cd python

# 以开发模式安装
pip install -e .

# 运行测试
ailuntz cv
```

### Node.js 版本

```bash
# 进入 Node.js 目录
cd nodejs

# 安装依赖（如果需要）
npm install

# 测试运行
npm test

# 或直接运行
node bin/cv.js
```

## 📁 项目结构

```
cli.ailuntz.com/
├── README.md              # 主文档
├── redeme.md             # 项目介绍（中文）
├── python/               # Python 版本
│   ├── ailuntz/
│   │   ├── __init__.py
│   │   └── cli.py        # CLI 主程序
│   ├── setup.py          # setuptools 配置
│   ├── pyproject.toml    # 现代 Python 项目配置
│   └── MANIFEST.in       # 打包清单
└── nodejs/               # Node.js 版本
    ├── package.json      # npm 包配置
    ├── index.js          # 主模块
    └── bin/
        └── cv.js         # CLI 入口点
```

## 🛠️ 发布

### 发布到 PyPI

```bash
cd python

# 创建虚拟环境并安装构建工具
python3 -m venv .venv
source .venv/bin/activate
pip install build twine

# 构建包
python -m build

# 上传到 PyPI（需要先在 https://pypi.org 注册账号）
twine upload dist/*
```

### 发布到 npm

```bash
cd nodejs

# 登录 npm（需要先在 https://www.npmjs.com 注册账号）
npm login

# 发布（scoped package 需要 --access public）
npm publish --access public
```

## 🎨 自定义

你可以根据自己的需求修改简历内容：

### Python 版本
编辑 `python/ailuntz/cli.py` 中的 `print_cv()` 函数

### Node.js 版本
编辑 `nodejs/bin/cv.js` 中的 `printCV()` 函数

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 👤 作者

**Ailuntz**

- Website: [https://ailuntz.com](https://ailuntz.com)
- Email: ailuntz@example.com
- GitHub: [@ailuntz](https://github.com/ailuntz)

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star ⭐️

---

<p align="center">Made with ❤️ by Ailuntz</p>
