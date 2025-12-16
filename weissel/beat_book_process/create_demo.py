#!/usr/bin/env python3
"""
Demo: Creates a minimal example website to show what the full version will look like.
This is a simplified version with just one sport section for testing.
"""

def create_demo_website():
    """Create a demo HTML file with one sport section."""
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beat Book Demo</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            margin: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        header {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        h1 { margin: 0; font-size: 2.5em; }
        .intro { padding: 30px; background: #f8f9fa; }
        .sport-section {
            margin: 20px;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            overflow: hidden;
        }
        .sport-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
        }
        .sport-header:hover {
            background: linear-gradient(135deg, #5568d3 0%, #653991 100%);
        }
        .sport-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s ease;
        }
        .sport-content.active {
            max-height: 5000px;
        }
        .sport-content-inner {
            padding: 30px;
        }
        .toggle { transition: transform 0.3s; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📰 Eastern Shore Sports Beat Book</h1>
            <p>Demo Version - Click sections below to expand</p>
        </header>
        
        <div class="intro">
            <h2>Demo Preview</h2>
            <p>This is a simplified demo showing how the full website will work.</p>
            <p><strong>Click the "Baseball" section below to see the dropdown in action!</strong></p>
        </div>
        
        <div class="sport-section">
            <div class="sport-header" onclick="toggleSection()">
                <h2>Baseball</h2>
                <span class="toggle" id="toggle">▼</span>
            </div>
            <div class="sport-content" id="content">
                <div class="sport-content-inner">
                    <h3>Local Sports Landscape Overview</h3>
                    <p>The Eastern Shore of Maryland is a tight-knit patchwork of small towns, 
                    each with a high-school that serves as a community hub. Baseball is the beating 
                    heart of that patchwork...</p>
                    
                    <h3>Reporter Lifestyle & Workflow</h3>
                    <p>Understanding how to structure your week around games, deadlines, and 
                    community events is essential for sustainable beat coverage.</p>
                    
                    <h3>Building Relationships</h3>
                    <p>Start with the Booster Clubs. Attend their meetings, volunteer for 
                    fund-raisers, and keep a running list of contact names.</p>
                    
                    <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                        <strong>💡 Tip:</strong> The full website will have 8 sports (Baseball, 
                        Basketball, Field Hockey, Football, Lacrosse, Soccer, Softball, Wrestling), 
                        each with complete guides, tables, and formatting.
                    </div>
                </div>
            </div>
        </div>
        
        <div style="padding: 20px; text-align: center; color: #666;">
            <p><em>This is just a demo. Run <code>python3 generate_beatbook_website.py</code> 
            to create the full interactive website!</em></p>
        </div>
    </div>
    
    <script>
        function toggleSection() {
            const content = document.getElementById('content');
            const toggle = document.getElementById('toggle');
            
            content.classList.toggle('active');
            
            if (content.classList.contains('active')) {
                toggle.style.transform = 'rotate(180deg)';
            } else {
                toggle.style.transform = 'rotate(0deg)';
            }
        }
    </script>
</body>
</html>"""
    
    output_file = 'demo_website.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Demo website created: {output_file}")
    print(f"   Open this file in your browser to see how the full version will look!")
    print(f"\n   To create the full website with all 8 sports:")
    print(f"   python3 generate_beatbook_website.py")

if __name__ == '__main__':
    create_demo_website()
