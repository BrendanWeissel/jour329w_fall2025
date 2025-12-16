# 🏀 Eastern Shore Sports Beat Book - Website Generator

## Overview

This project converts your **Eastern Shore Sports Beat Book** markdown file into a beautiful, interactive website with dropdown sections for each sport.

## 📁 What You Have

Your `stardem_draft/` directory now contains:

| File | Purpose |
|------|---------|
| `Eastern_Shore_Sports_Beat_Book.md` | 📄 Your source data (beat book content) |
| `generate_beatbook_website.py` | 🚀 Main generator script (creates the website) |
| `generate_website.sh` | 🐚 Bash wrapper (alternative way to run) |
| `test_setup.py` | 🧪 Tests your environment before running |
| `create_demo.py` | 👀 Creates a demo to preview the design |
| `QUICKSTART.md` | ⚡ Quick start instructions |
| `README_WEBSITE.md` | 📚 Detailed documentation |

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
pip install markdown
```

### Step 2: Run the Generator

```bash
cd /workspaces/jour329w_fall2025/weissel/stardem_draft
python3 generate_beatbook_website.py
```

### Step 3: Open the Website

```bash
"$BROWSER" beatbook_website.html
```

Or right-click `beatbook_website.html` in VS Code and select "Open Preview"

## ✨ Features

The generated website includes:

✅ **8 Complete Sport Guides**
- Baseball
- Basketball  
- Field Hockey
- Football
- Lacrosse
- Soccer
- Softball
- Wrestling

✅ **Interactive Design**
- Click any sport name to expand/collapse the full guide
- Smooth animations and transitions
- Quick navigation buttons at the top

✅ **Professional Styling**
- Purple/blue gradient theme
- Responsive layout (mobile-friendly)
- Formatted tables, code blocks, and lists
- Professional typography

✅ **Fully Self-Contained**
- Single HTML file with embedded CSS and JavaScript
- No external dependencies
- Easy to share or host

## 📖 Usage Workflows

### Workflow 1: Test First, Then Generate

```bash
# 1. Test your setup
python3 test_setup.py

# 2. Create a demo preview
python3 create_demo.py

# 3. Generate the full website
python3 generate_beatbook_website.py
```

### Workflow 2: Use the Shell Script

```bash
# Make executable (first time only)
chmod +x generate_website.sh

# Run it
./generate_website.sh
```

### Workflow 3: Update Content, Then Regenerate

```bash
# 1. Update your beat book using LLM
cat prompt_sport_combine.txt sportsbooks.md | uv run llm -m groq/openai/gpt-oss-120b > Eastern_Shore_Sports_Beat_Book.md

# 2. Regenerate website with new content
python3 generate_beatbook_website.py
```

## 🎨 What the Website Looks Like

```
┌─────────────────────────────────────────────────────────┐
│  📰 Eastern Shore Sports Beat Book                      │
│  A Comprehensive Guide for Star Democrat Reporters      │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│  Welcome to Your Beat                                    │
│  Click any sport below to explore detailed guidelines... │
└─────────────────────────────────────────────────────────┘
┌──────────┬──────────┬──────────┬──────────┐
│ Baseball │Basketball│  Field   │ Football │  ← Quick nav
│          │          │  Hockey  │          │    buttons
├──────────┼──────────┼──────────┼──────────┤
│ Lacrosse │  Soccer  │ Softball │Wrestling │
└──────────┴──────────┴──────────┴──────────┘

┌─────────────────────────────────────────────────────────┐
│ ▶ Baseball                                          ▼   │  ← Click to
├─────────────────────────────────────────────────────────┤    expand
│ (collapsed - click header to expand)                    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ▼ Basketball                                        ▲   │  ← Expanded
├─────────────────────────────────────────────────────────┤
│  Local Sports Landscape Overview                        │
│  The Eastern Shore's high-school basketball...          │
│                                                          │
│  Reporter Lifestyle & Workflow                          │
│  Understanding how to structure your week...            │
│                                                          │
│  [Full formatted content with tables, lists, etc.]      │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Customization

### Change Colors

Edit `generate_beatbook_website.py`, find the style section, and modify:

```css
/* Current: Purple/Blue gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Example: Green/Teal */
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);

/* Example: Red/Orange */
background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
```

### Change Width

```css
.container {
    max-width: 1200px;  /* Change this value */
}
```

### Change Fonts

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    /* Replace with: 'Georgia', 'Times New Roman', 'Courier New', etc. */
}
```

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'markdown'"

**Solution:**
```bash
pip install markdown
```

### Problem: "No sport sections found"

**Solution:** Make sure `Eastern_Shore_Sports_Beat_Book.md` exists and has proper section headers.

**Check it:**
```bash
head -50 Eastern_Shore_Sports_Beat_Book.md
```

### Problem: Website looks unstyled

**Solution:** 
- Make sure you're opening the `.html` file (not the `.md` file)
- Try a different browser
- Check browser console for errors (F12 → Console tab)

### Problem: Terminal commands not working

**Solution:** Try running commands from the workspace root:
```bash
cd /workspaces/jour329w_fall2025
python3 weissel/stardem_draft/generate_beatbook_website.py
```

## 📤 Sharing the Website

The generated HTML file is completely self-contained. You can:

1. **Email it**: Just attach `beatbook_website.html`
2. **Upload to web hosting**: Use GitHub Pages, Netlify, or any web host
3. **Share via cloud**: Dropbox, Google Drive, OneDrive
4. **USB drive**: Copy the HTML file
5. **Print**: Open in browser, Print to PDF

### GitHub Pages Example

```bash
# Create a new repo branch
git checkout -b gh-pages

# Copy the HTML file
cp beatbook_website.html index.html

# Push to GitHub
git add index.html
git commit -m "Add beat book website"
git push origin gh-pages

# Enable GitHub Pages in repo settings
# Your site will be at: https://yourusername.github.io/reponame/
```

## 🎯 Integration with LLM Workflow

### Current Workflow
```bash
cat prompt_sport_combine.txt sportsbooks.md | \
  uv run llm -m groq/openai/gpt-oss-120b
```

### Enhanced Workflow
```bash
# 1. Generate beat book content
cat prompt_sport_combine.txt sportsbooks.md | \
  uv run llm -m groq/openai/gpt-oss-120b > Eastern_Shore_Sports_Beat_Book.md

# 2. Create interactive website
python3 generate_beatbook_website.py

# 3. Open and review
"$BROWSER" beatbook_website.html
```

## 📊 File Sizes

Typical sizes after generation:

| File | Size |
|------|------|
| `Eastern_Shore_Sports_Beat_Book.md` | ~50-100 KB |
| `beatbook_website.html` | ~150-250 KB |
| `generate_beatbook_website.py` | ~13 KB |

## 🚀 Advanced Usage

### Batch Process Multiple Files

```python
# Create variations with different LLMs
models = [
    "groq/openai/gpt-oss-120b",
    "anthropic/claude-sonnet-4-5"
]

for model in models:
    # Generate content
    os.system(f"cat prompt.txt data.md | llm -m {model} > beatbook_{model}.md")
    
    # Create website
    # (modify script to accept input/output params)
```

### Add Custom Sections

Edit `generate_beatbook_website.py` and add to the `sports` list:

```python
sports = [
    'Baseball',
    'Basketball',
    # ... existing sports ...
    'Track and Field',  # Add new sport
    'Volleyball',       # Add another
]
```

## 📚 Additional Resources

- **LLM Documentation**: [Simon Willison's LLM](https://llm.datasette.io/)
- **Markdown Guide**: [markdownguide.org](https://www.markdownguide.org/)
- **Python Markdown**: [python-markdown.github.io](https://python-markdown.github.io/)

## 🆘 Need Help?

1. Run the test script: `python3 test_setup.py`
2. Create a demo: `python3 create_demo.py`
3. Check the detailed docs: `README_WEBSITE.md`
4. Review quick start: `QUICKSTART.md`

## 📝 License

Part of JOUR329W Fall 2025 project at University of Maryland.

---

**Made with ❤️ for sports journalists on Maryland's Eastern Shore**
