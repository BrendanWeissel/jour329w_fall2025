# Beat Book Website Generator - Files Moved

All website generator files have been moved from `stardem_draft` to `stardem_different`.

## Files in This Directory

### Core Scripts
- **`generate_beatbook_website.py`** - Main Python script that generates the interactive HTML website
- **`generate_website.sh`** - Bash wrapper script for easy execution
- **`test_setup.py`** - Environment testing script
- **`create_demo.py`** - Creates a demo preview of the website

### Documentation
- **`MASTER_GUIDE.md`** - Complete guide with all workflows and features
- **`QUICKSTART.md`** - Quick 3-step getting started guide
- **`README_WEBSITE.md`** - Detailed documentation and troubleshooting

## Quick Start

```bash
cd /workspaces/jour329w_fall2025/weissel/stardem_different
pip install markdown
python3 generate_beatbook_website.py
```

## What This Does

Converts your `Eastern_Shore_Sports_Beat_Book.md` file into an interactive website with:
- Collapsible dropdown sections for 8 sports
- Quick navigation buttons
- Professional purple/blue gradient design
- Mobile-responsive layout
- Self-contained single HTML file

## Next Steps

1. Make sure you have `Eastern_Shore_Sports_Beat_Book.md` in this directory
2. Run `python3 test_setup.py` to verify your environment
3. Run `python3 generate_beatbook_website.py` to create the website
4. Open `beatbook_website.html` in your browser

## More Info

See `MASTER_GUIDE.md` for complete documentation.
