# Quick Start Guide - Beat Book Website Generator

## The Easy Way

Since you're in a dev container, here's the simplest way to generate your website:

### Step 1: Navigate to the directory

```bash
cd /workspaces/jour329w_fall2025/weissel/stardem_different
```

### Step 2: Make sure markdown is installed

```bash
pip install markdown
```

### Step 3: Run the generator

```bash
python3 generate_beatbook_website.py
```

### Step 4: View the website

```bash
# Open in browser
"$BROWSER" beatbook_website.html

# Or if using VS Code, right-click the HTML file and select "Open Preview"
```

## What You Get

The script creates **beatbook_website.html** with:

✅ **8 Sport Sections**: Baseball, Basketball, Field Hockey, Football, Lacrosse, Soccer, Softball, Wrestling

✅ **Interactive Dropdowns**: Click any sport name to expand/collapse the full guide

✅ **Quick Navigation**: Buttons at the top jump you to any sport

✅ **Professional Design**: 
- Purple/blue gradient theme
- Responsive layout (works on mobile)
- Formatted tables and code blocks
- Smooth animations

## Screenshot Description

When you open the website, you'll see:

1. **Header**: Large title "Eastern Shore Sports Beat Book" with subtitle
2. **Intro Section**: Welcome message and usage tips
3. **Navigation Bar**: 8 colored buttons (one for each sport)
4. **Collapsible Sections**: Each sport has a clickable header that reveals detailed content
5. **Footer**: Attribution and copyright

## File Locations

After running the script:

```
/workspaces/jour329w_fall2025/weissel/stardem_different/
├── Eastern_Shore_Sports_Beat_Book.md     ← Your source data
├── generate_beatbook_website.py          ← The generator script  
├── beatbook_website.html                 ← Generated website! 📱
├── generate_website.sh                   ← Alternative: bash script
└── README_WEBSITE.md                     ← Detailed documentation
```

## Using the LLM Command

Your original workflow was:
```bash
cat prompt_sport_combine.txt sportsbooks.md | uv run llm -m groq/openai/gpt-oss-120b
```

Now you have **two options**:

### Option A: Use the LLM to generate/update content
```bash
# Generate new beat book content
cat prompt_sport_combine.txt sportsbooks.md | uv run llm -m groq/openai/gpt-oss-120b > Eastern_Shore_Sports_Beat_Book.md

# Then create the website from it
python3 generate_beatbook_website.py
```

### Option B: Use the website generator directly
```bash
# If you already have Eastern_Shore_Sports_Beat_Book.md
python3 generate_beatbook_website.py
```

## Customizing the Design

Want to change colors or layout? Edit `generate_beatbook_website.py` and look for these sections:

### Change the color scheme:
```python
# Find lines with gradients like:
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Replace hex codes with your colors
```

### Change fonts:
```python
# Find:
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

# Replace with your preferred fonts
```

### Adjust width:
```python
# Find:
max-width: 1200px;

# Change to make it wider or narrower
```

## Troubleshooting

### "No sport sections found"
- Check that `Eastern_Shore_Sports_Beat_Book.md` exists
- Make sure it has sections for Baseball, Basketball, etc.

### "ModuleNotFoundError: No module named 'markdown'"
```bash
pip install markdown
```

### HTML file looks plain/unstyled
- Make sure you're opening `beatbook_website.html` (not the .md file)
- Try a different browser (Chrome, Firefox, Edge)

### Want to share the website?
The HTML file is completely self-contained. You can:
- Email it as an attachment
- Upload to a web server
- Share via Dropbox/Google Drive
- Host on GitHub Pages

## Next Steps

1. ✅ You've got the generator script
2. Run it to create your website
3. Open beatbook_website.html in a browser
4. Share with other reporters at Star Democrat!

## Need Help?

Check these files:
- `README_WEBSITE.md` - Full documentation
- `generate_beatbook_website.py` - The source code (well-commented)
- `generate_website.sh` - Alternative bash script

---

**Pro Tip**: Bookmark `beatbook_website.html` in your browser for quick reference while covering games! 🏀⚾🏈
