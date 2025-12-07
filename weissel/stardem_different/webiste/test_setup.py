#!/usr/bin/env python3
"""
Simple test script to verify the setup before running the full generator.
"""

import sys
from pathlib import Path

def test_environment():
    """Test if the environment is set up correctly."""
    
    print("🧪 Testing Beat Book Website Generator Setup...\n")
    
    all_good = True
    
    # Test 1: Check Python version
    print("1. Checking Python version...")
    if sys.version_info >= (3, 6):
        print(f"   ✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    else:
        print(f"   ❌ Python version too old: {sys.version_info}")
        all_good = False
    
    # Test 2: Check for markdown module
    print("\n2. Checking for markdown module...")
    try:
        import markdown
        print(f"   ✅ markdown module installed (version {markdown.__version__})")
    except ImportError:
        print("   ❌ markdown module not found")
        print("      Run: pip install markdown")
        all_good = False
    
    # Test 3: Check for source markdown file
    print("\n3. Checking for source file...")
    script_dir = Path(__file__).parent
    source_file = script_dir / 'Eastern_Shore_Sports_Beat_Book.md'
    
    if source_file.exists():
        size = source_file.stat().st_size
        print(f"   ✅ Found: {source_file.name} ({size:,} bytes)")
    else:
        print(f"   ❌ Not found: {source_file}")
        all_good = False
    
    # Test 4: Check for generator script
    print("\n4. Checking for generator script...")
    generator = script_dir / 'generate_beatbook_website.py'
    
    if generator.exists():
        print(f"   ✅ Found: {generator.name}")
    else:
        print(f"   ❌ Not found: {generator}")
        all_good = False
    
    # Test 5: Check write permissions
    print("\n5. Checking write permissions...")
    test_file = script_dir / '.test_write'
    try:
        test_file.write_text("test")
        test_file.unlink()
        print(f"   ✅ Can write to directory")
    except Exception as e:
        print(f"   ❌ Cannot write to directory: {e}")
        all_good = False
    
    # Summary
    print("\n" + "="*50)
    if all_good:
        print("✅ All tests passed! You're ready to generate the website.")
        print("\nRun this command:")
        print("   python3 generate_beatbook_website.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(test_environment())
