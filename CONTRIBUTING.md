# 🤝 贡献指南 / Contributing Guide

感谢你对 Ailuntz 项目的兴趣！我们欢迎任何形式的贡献。

## 🌟 如何贡献

### 报告 Bug

如果你发现了 bug，请创建一个 issue 并包含以下信息：

- Bug 的详细描述
- 复现步骤
- 期望的行为
- 实际的行为
- 系统环境（操作系统、Python/Node.js 版本等）

### 提出新功能

如果你有好的想法，请：

1. 先检查 issues 中是否已有类似建议
2. 创建一个新的 issue 描述你的想法
3. 等待维护者的反馈

### 提交代码

1. **Fork 项目**

```bash
git clone https://github.com/ailuntz/cli
cd ailuntz
```

2. **创建特性分支**

```bash
git checkout -b feature/your-feature-name
```

3. **进行开发**

- 保持代码风格一致
- 添加必要的注释
- 确保代码能正常运行

4. **测试你的更改**

Python 版本：
```bash
cd python
python -m ailuntz.cli cv
```

Node.js 版本：
```bash
cd nodejs
node bin/cv.js cv
```

5. **提交更改**

```bash
git add .
git commit -m "feat: add some feature"
```

提交信息格式：
- `feat:` 新功能
- `fix:` Bug 修复
- `docs:` 文档更新
- `style:` 代码格式（不影响功能）
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

6. **推送到你的 Fork**

```bash
git push origin feature/your-feature-name
```

7. **创建 Pull Request**

- 在 GitHub 上创建 PR
- 清楚地描述你的更改
- 链接相关的 issue

## 📝 代码规范

### Python

- 遵循 PEP 8 规范
- 使用 4 个空格缩进
- 函数和变量使用 snake_case
- 类名使用 PascalCase

### JavaScript

- 使用 2 个空格缩进
- 使用 const/let，避免 var
- 使用驼峰命名法（camelCase）
- 添加适当的 JSDoc 注释

## 🧪 测试

在提交 PR 前，请确保：

- [ ] 代码能够正常运行
- [ ] 没有引入新的 bug
- [ ] 更新了相关文档
- [ ] 代码风格一致

## 📖 文档

如果你的更改影响到用户使用方式，请：

- 更新 README.md
- 添加或更新代码注释
- 如需要，创建新的文档文件

## 💬 交流

如果你有任何问题：

- 创建一个 issue
- 通过邮件联系：ailuntz@example.com

## 📜 许可证

通过贡献代码，你同意你的贡献将在 MIT 许可证下发布。

---

感谢你的贡献！❤️
