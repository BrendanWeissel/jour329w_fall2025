# Eastern Shore Sports Beat Book Website Generator

## Overview
This script generates an interactive HTML website from the `Eastern_Shore_Sports_Beat_Book.md` file. The website features:
- Beautiful, responsive design
- Collapsible dropdown sections for each sport
- Quick navigation buttons
- Professional styling with gradients and hover effects
- Mobile-friendly layout

## Installation

First, make sure you have the `markdown` Python package installed:

```bash
pip install markdown
```

## Usage

### Basic Usage

Run the script from the `stardem_different` directory:

```bash
cd /workspaces/jour329w_fall2025/weissel/stardem_different
python generate_beatbook_website.py
```

### What It Does

The script will:
1. Read `Eastern_Shore_Sports_Beat_Book.md`
2. Parse all sport sections (Baseball, Basketball, Field Hockey, Football, Lacrosse, Soccer, Softball, Wrestling)
3. Convert markdown to HTML
4. Generate `beatbook_website.html` with an interactive interface

### Viewing the Website

After running the script, open the generated HTML file in your browser:

```bash
# On Linux/Mac with default browser
xdg-open beatbook_website.html

# Or in the dev container
"$BROWSER" beatbook_website.html

# Or manually open the file in VS Code and use the "Open Preview" feature
```

## Features

### Interactive Dropdowns
- Click any sport header to expand/collapse its content
- Smooth animations and transitions
- Visual feedback with hover effects

### Quick Navigation
- Navigation buttons at the top for each sport
- Clicking a button scrolls to that sport and opens the section automatically

### Responsive Design
- Looks great on desktop, tablet, and mobile
- Adjusts layout based on screen size
- Tables are scrollable on small screens

### Professional Styling
- Gradient color scheme (purple/blue theme)
- Clean typography with good readability
- Organized tables and formatted code blocks
- Highlighted section headers

## File Structure

```
stardem_different/
├── Eastern_Shore_Sports_Beat_Book.md    # Source markdown file
├── generate_beatbook_website.py         # Generator script
├── beatbook_website.html                # Generated website (after running)
└── README_WEBSITE.md                    # This file
```

## Customization

To customize the website appearance, edit the `<style>` section in `generate_beatbook_website.py`:

- **Colors**: Modify the gradient colors in `.nav-button` and `.sport-header`
- **Fonts**: Change the `font-family` in the `body` style
- **Layout**: Adjust `max-width` in `.container` for wider/narrower content
- **Spacing**: Modify padding and margin values

## Troubleshooting

### No sport sections found
- Make sure `Eastern_Shore_Sports_Beat_Book.md` exists in the same directory
- Check that the markdown file has proper section headers

### Markdown not converting properly
- Ensure the `markdown` package is installed: `pip install markdown`
- Check for any special characters that might need escaping

### HTML looks broken
- Open the HTML file in a modern browser (Chrome, Firefox, Safari, Edge)
- Check browser console for any JavaScript errors

## Using with LLM Command

The original command you used was:
```bash
cat prompt_sport_combine.txt sportsbooks.md | uv run llm -m groq/openai/gpt-oss-120b
```

This script provides a way to present the beat book content in a more user-friendly, interactive format compared to raw markdown.

## Future Enhancements

Possible improvements:
- Add search functionality
- Include print-friendly CSS
- Add export to PDF option
- Create a table of contents with section counts
- Add dark mode toggle
- Include story examples with syntax highlighting

## License

Part of the JOUR329W Fall 2025 project.
