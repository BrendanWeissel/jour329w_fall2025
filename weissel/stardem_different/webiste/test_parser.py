#!/usr/bin/env python3
"""Test the parser to see what sections are extracted."""

import re

def parse_beatbook(markdown_file):
    """Parse the beat book markdown file and extract sport sections."""
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
                print(f"✓ Found {sport}: {len(section_content)} characters")
            else:
                print(f"✗ {sport}: Empty content")
        else:
            print(f"✗ {sport}: No match found")
    
    return sections

if __name__ == '__main__':
    sections = parse_beatbook('Eastern_Shore_Sports_Beat_Book.md')
    print(f"\nTotal sections found: {len(sections)}")
    for sport in sections:
        preview = sections[sport][:100].replace('\n', ' ')
        print(f"\n{sport} preview: {preview}...")
