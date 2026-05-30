# Contributing to codex-starter

Thank you for your interest in contributing! 🎉

---

## 📋 Table of Contents

- [Reporting Bugs](#-reporting-bugs)
- [Suggesting Features](#-suggesting-features)
- [Development Setup](#-development-setup)
- [Testing Your Changes](#-testing-your-changes)
- [Pull Requests](#-pull-requests)
- [Code Style Guidelines](#-code-style-guidelines)

---

## 🐛 Reporting Bugs

Use our [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md):

1. Check existing [Issues](https://github.com/andiupn/codex-starter/issues)
2. Search for similar reports
3. If not found, create new issue with template
4. Include:
   - Clear reproduction steps
   - Expected vs actual behavior
   - Environment details (OS, Python, Editor)
   - Error logs/screenshots

---

## 💡 Suggesting Features

Use our [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md):

1. Describe the problem/use case
2. Propose your solution
3. List alternatives considered
4. Explain who would benefit

---

## 🔧 Development Setup

### Prerequisites

- Python 3.10+
- Git for version control
- Shell-compatible environment (Linux/macOS/Git Bash)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/andiupn/codex-starter.git
cd codex-starter
```

### Setup Workflows

```bash
# 1. Run local health check script
./scripts/project-health.sh --auto

# 2. Setup environment
cp .env.example .env
# Update with your email and configurations

# 3. Verify memory & research indexes
python3 scripts/memory-health.py
python3 scripts/research-health.py
```

---

## 🧪 Testing Your Changes

Before submitting your contributions, please verify:

- Verify memory searches work: `python3 scripts/memory-find.py workflow`
- Verify research searches work: `python3 scripts/research-find.py model`
- Verify standard rules-health checks: `python3 scripts/rules-health.py`

- [ ] Check markdown files render correctly on GitHub
- [ ] Verify all links work
- [ ] Check for typos

---

## 🔀 Pull Requests

### Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make Changes**
   - Write clear, focused commits
   - Follow code style guidelines
   - Add/update tests if needed
   - Update documentation

3. **Commit with Conventional Format**
   ```bash
   git commit -m "feat: add new workflow for X"
   git commit -m "fix: resolve issue with Y"
   git commit -m "docs: update README with Z"
   ```

4. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open Pull Request**
   - Use PR template (auto-generated)
   - Reference related issues
   - Describe changes clearly
   - Add screenshots if UI changes

### Commit Message Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: add /export workflow` |
| `fix` | Bug fix | `fix: handle missing index.json` |
| `docs` | Documentation | `docs: update FAQ section` |
| `refactor` | Code refactoring | `refactor: simplify search logic` |
| `test` | Add/update tests | `test: add validation tests` |
| `chore` | Maintenance | `chore: update dependencies` |

---

## 📐 Code Style Guidelines

### Python Scripts

**Follow PEP 8:**
- 4 spaces for indentation
- Max line length: 88 characters (Black formatter)
- Use descriptive variable names
- Add docstrings to functions

**Example:**
```python
def save_knowledge(category: str, content: str) -> bool:
    """
    Save knowledge entry to specified category.
    
    Args:
        category: Category name (gotchas, patterns, decisions, context)
        content: Knowledge content to save
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Implementation
    pass
```

**Tools:**
- Use `black` for formatting (optional but recommended)
- Use `pylint` or `flake8` for linting

### Shell Scripts

**Follow ShellCheck recommendations:**
- Quote variables: `"$variable"`
- Use `set -e` for error handling
- Add comments for complex logic
- Test on target platforms

### Markdown Documentation

**Consistency:**
- Use ATX headers (`#` style, not underline style)
- Add blank lines between sections
- Use code fences with language specification
- Keep lines under 120 characters when possible

**Links:**
- Use reference-style links for readability
- Verify all links before committing

### Workflows (Markdown)

- Use YAML frontmatter for metadata
- Clear step-by-step instructions
- Include examples
- Mark dangerous operations with `// turbo` annotations appropriately

---

## 🎁 What We're Looking For

We especially appreciate contributions in these areas:

- **New Workflows** - Useful automation workflows
- 📚 **Documentation** - Tutorials, examples, translations
- 🧪 **Testing** - Test coverage improvements
- 🐛 **Bug Fixes** - Any size, all welcome
- ✨ **Feature Enhancements** - Based on user feedback

---

## 📦 Release Process

(For maintainers)

1. Update `CHANGELOG.md` with new version
2. Tag release: `git tag v1.x.x`
3. Push tags: `git push --tags`
4. Create GitHub release with notes

---

## 💖 Support This Project

If codex-starter helps you, consider:

- ⭐ **Star the repo** - Helps others discover it
- 💬 **Spread the word** - Tweet, blog, or share
- ☕ **Buy me a coffee**:
  - [Ko-fi](https://ko-fi.com/andiupn)
  - [Patreon](https://www.patreon.com/AndiUpn)
  - [Trakteer](https://trakteer.id/andi_upn/gift) 🇮🇩
  - [Saweria](https://saweria.co/andiupn) 🇮🇩

---

## ❓ Questions?

- 📖 Check the [FAQ](README.md#-faq)
- 🔧 See [Troubleshooting](README.md#-troubleshooting)
- 💬 Ask in [Issues](https://github.com/andiupn/codex-starter/issues)
- 📧 Email: [Contact Form](https://www.kuncimu.com/)

---

**Thank you for contributing!** 🙏

*Made with ❤️ by Andi UPN and contributors*
