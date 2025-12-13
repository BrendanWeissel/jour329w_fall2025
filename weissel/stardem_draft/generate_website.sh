#!/bin/bash
# Generate the Eastern Shore Sports Beat Book website

echo "🏀 Generating Eastern Shore Sports Beat Book Website..."
echo ""

# Change to the script directory
cd "$(dirname "$0")"

# Check if the markdown file exists
if [ ! -f "Eastern_Shore_Sports_Beat_Book.md" ]; then
    echo "❌ Error: Eastern_Shore_Sports_Beat_Book.md not found!"
    echo "   Please make sure the beat book markdown file is in this directory."
    exit 1
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 not found!"
    exit 1
fi

# Check if markdown package is installed
if ! python3 -c "import markdown" &> /dev/null; then
    echo "📦 Installing markdown package..."
    pip install markdown
fi

# Run the generator
echo "⚙️  Running generator..."
python3 generate_beatbook_website.py

# Check if successful
if [ $? -eq 0 ] && [ -f "beatbook_website.html" ]; then
    echo ""
    echo "✅ Success! Website generated: beatbook_website.html"
    echo ""
    echo "To view the website:"
    echo "  - Open beatbook_website.html in your browser"
    echo "  - Or run: \$BROWSER beatbook_website.html"
else
    echo ""
    echo "❌ Error: Failed to generate website"
    exit 1
fi
