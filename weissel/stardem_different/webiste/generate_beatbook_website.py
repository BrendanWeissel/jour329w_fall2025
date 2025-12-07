#!/usr/bin/env python3
"""
Generate an interactive HTML website from the Eastern Shore Sports Beat Book.
Reads the markdown beat book and creates a web page with collapsible dropdown sections.
"""

import re
import markdown
from pathlib import Path


def parse_beatbook(markdown_file):
    """
    Parse the beat book markdown file and extract sport sections.
    Returns a dictionary with sport names as keys and content as values.
    """
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = {}
    
    # Define the sports to extract with their section header patterns
    sports_mapping = {
        'Baseball': r'## .*Baseball.*Beat.*Guide',
        'Basketball': r'## .*Basketball.*Beat.*Guide',
        'Field Hockey': r'## .*Field.*Hockey.*Beat.*Guide',
        'Football': r'## .*Football.*Beat.*Guide',
        'Lacrosse': r'## .*Lacrosse.*Beat.*Guide',
        'Soccer': r'## .*Soccer.*Beat.*Guide',
        'Softball': r'## .*Softball.*Beat.*Guide',
        'Wrestling': r'## .*Wrestling.*Beat.*Guide'
    }
    
    # Extract each sport section
    for sport, header_pattern in sports_mapping.items():
        # Find the section header and capture everything until the next ## header or end of file
        pattern = rf'{header_pattern}\n+(.*?)(?=\n## |\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            section_content = match.group(1).strip()
            if section_content:
                sections[sport] = section_content
    
    return sections


def generate_html(sections, output_file):
    """
    Generate an HTML file with collapsible sections for each sport.
    """
    
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eastern Shore Sports Beat Book</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .intro {{
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 3px solid #e9ecef;
        }}
        
        .intro h2 {{
            color: #1e3c72;
            margin-bottom: 15px;
        }}
        
        .intro p {{
            margin-bottom: 10px;
            color: #555;
        }}
        
        .sports-nav {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 3px solid #e9ecef;
        }}
        
        .nav-button {{
            padding: 15px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            font-weight: 600;
            transition: all 0.3s ease;
            text-align: center;
        }}
        
        .nav-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .sport-section {{
            margin-bottom: 20px;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            overflow: hidden;
            transition: all 0.3s ease;
        }}
        
        .sport-section:hover {{
            border-color: #667eea;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.1);
        }}
        
        .sport-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 25px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
            transition: all 0.3s ease;
        }}
        
        .sport-header:hover {{
            background: linear-gradient(135deg, #5568d3 0%, #653991 100%);
        }}
        
        .sport-header h2 {{
            font-size: 1.8em;
            font-weight: 600;
        }}
        
        .toggle-icon {{
            font-size: 1.5em;
            transition: transform 0.3s ease;
        }}
        
        .sport-content {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s ease;
            background: white;
        }}
        
        .sport-content.active {{
            max-height: 10000px;
        }}
        
        .sport-content-inner {{
            padding: 30px;
        }}
        
        .sport-content h3 {{
            color: #1e3c72;
            margin-top: 25px;
            margin-bottom: 15px;
            font-size: 1.5em;
            border-bottom: 2px solid #667eea;
            padding-bottom: 8px;
        }}
        
        .sport-content h4 {{
            color: #2a5298;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}
        
        .sport-content p {{
            margin-bottom: 15px;
            color: #555;
        }}
        
        .sport-content ul, .sport-content ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        
        .sport-content li {{
            margin-bottom: 8px;
            color: #555;
        }}
        
        .sport-content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .sport-content table th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        .sport-content table td {{
            padding: 12px;
            border-bottom: 1px solid #e9ecef;
        }}
        
        .sport-content table tr:nth-child(even) {{
            background: #f8f9fa;
        }}
        
        .sport-content table tr:hover {{
            background: #e9ecef;
        }}
        
        .sport-content code {{
            background: #f8f9fa;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            color: #e83e8c;
        }}
        
        .sport-content pre {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
        }}
        
        .sport-content blockquote {{
            border-left: 4px solid #667eea;
            padding-left: 20px;
            margin: 20px 0;
            color: #666;
            font-style: italic;
        }}
        
        footer {{
            background: #1e3c72;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2em;
            }}
            
            .sports-nav {{
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                gap: 10px;
            }}
            
            .sport-header h2 {{
                font-size: 1.4em;
            }}
            
            .content {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📰 Eastern Shore Sports Beat Book</h1>
            <p>A Comprehensive Guide for Star Democrat Sports Reporters</p>
        </header>
        
        <div class="intro">
            <h2>Welcome to Your Beat</h2>
            <p>This interactive guide is your go-to resource for covering high school and community sports on Maryland's Eastern Shore. Click any sport below to explore detailed coverage guidelines, story ideas, and reporting strategies.</p>
            <p><strong>Tip:</strong> Use the quick navigation buttons to jump to a specific sport, or scroll down to browse all sections.</p>
        </div>
        
        <div class="sports-nav">
            {nav_buttons}
        </div>
        
        <div class="content">
            {sport_sections}
        </div>
        
        <footer>
            <p>&copy; 2025 Star Democrat Eastern Shore Sports Beat Book</p>
            <p>Generated for journalism excellence on Maryland's Eastern Shore</p>
        </footer>
    </div>
    
    <script>
        // Toggle dropdown functionality
        function toggleSection(sportId) {{
            const content = document.getElementById(sportId + '-content');
            const icon = document.getElementById(sportId + '-icon');
            
            content.classList.toggle('active');
            
            if (content.classList.contains('active')) {{
                icon.style.transform = 'rotate(180deg)';
            }} else {{
                icon.style.transform = 'rotate(0deg)';
            }}
        }}
        
        // Scroll to section
        function scrollToSport(sportId) {{
            const section = document.getElementById(sportId + '-section');
            section.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            
            // Open the section if it's closed
            const content = document.getElementById(sportId + '-content');
            const icon = document.getElementById(sportId + '-icon');
            
            if (!content.classList.contains('active')) {{
                content.classList.add('active');
                icon.style.transform = 'rotate(180deg)';
            }}
        }}
    </script>
</body>
</html>"""
    
    # Generate navigation buttons
    nav_buttons = []
    for sport in sections.keys():
        sport_id = sport.lower().replace(' ', '-')
        nav_buttons.append(f'<button class="nav-button" onclick="scrollToSport(\'{sport_id}\')">{sport}</button>')
    
    nav_buttons_html = '\n            '.join(nav_buttons)
    
    # Generate sport sections
    sport_sections_html = []
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'nl2br'])
    
    for sport, content in sections.items():
        sport_id = sport.lower().replace(' ', '-')
        
        # Convert markdown to HTML
        html_content = md.convert(content)
        md.reset()  # Reset the markdown parser for the next section
        
        section_html = f"""
        <div class="sport-section" id="{sport_id}-section">
            <div class="sport-header" onclick="toggleSection('{sport_id}')">
                <h2>{sport}</h2>
                <span class="toggle-icon" id="{sport_id}-icon">▼</span>
            </div>
            <div class="sport-content" id="{sport_id}-content">
                <div class="sport-content-inner">
                    {html_content}
                </div>
            </div>
        </div>"""
        
        sport_sections_html.append(section_html)
    
    sport_sections_combined = '\n'.join(sport_sections_html)
    
    # Fill in the template
    final_html = html_template.format(
        nav_buttons=nav_buttons_html,
        sport_sections=sport_sections_combined
    )
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✅ Website generated successfully: {output_file}")
    print(f"   Found {len(sections)} sport sections:")
    for sport in sections.keys():
        print(f"   - {sport}")


def main():
    """Main function to generate the beat book website."""
    
    # File paths
    script_dir = Path(__file__).parent
    input_file = script_dir / 'Eastern_Shore_Sports_Beat_Book.md'
    output_file = script_dir / 'beatbook_website.html'
    
    # Check if input file exists
    if not input_file.exists():
        print(f"❌ Error: Input file not found: {input_file}")
        print("   Please make sure 'Eastern_Shore_Sports_Beat_Book.md' exists in the same directory.")
        return
    
    print("🏀 Generating Eastern Shore Sports Beat Book Website...")
    print(f"   Reading from: {input_file}")
    print(f"   Writing to: {output_file}")
    print()
    
    # Parse the beat book
    sections = parse_beatbook(input_file)
    
    if not sections:
        print("⚠️  Warning: No sport sections found in the beat book.")
        print("   The markdown file may need to be formatted differently.")
        return
    
    # Generate the HTML website
    generate_html(sections, output_file)
    print()
    print("🎉 Done! Open the HTML file in your browser to view the interactive beat book.")


if __name__ == '__main__':
    main()
