#!/bin/bash

# Process files in parts to avoid overwhelming the LLM

echo "Processing Fall Record Book..."
cat prompt_different.txt "Fall Record Book 2024.pdf.txt" | \
    uv run llm -m groq/openai/gpt-oss-120b > sports_fall.md 2>&1
echo "✓ Fall analysis saved to sports_fall.md"

echo "Processing Spring Record Book..."
cat prompt_different.txt "Spring record book 2025.pdf.txt" | \
    uv run llm -m groq/openai/gpt-oss-120b > sports_spring.md 2>&1
echo "✓ Spring analysis saved to sports_spring.md"

echo "Processing Winter Record Book..."
cat prompt_different.txt "Winter record book.pdf.txt" | \
    uv run llm -m groq/openai/gpt-oss-120b > sports_winter.md 2>&1
echo "✓ Winter analysis saved to sports_winter.md"

# Combine all into one document
echo "Combining all analyses into sports_all_seasons.md..."
{
  echo "# Eastern Shore High School Accomplishments - All Seasons"
  echo ""
  echo "## Fall Season"
  echo ""
  cat sports_fall.md
  echo ""
  echo "---"
  echo ""
  echo "## Spring Season"
  echo ""
  cat sports_spring.md
  echo ""
  echo "---"
  echo ""
  echo "## Winter Season"
  echo ""
  cat sports_winter.md
} > sports_all_seasons.md

echo "✓ All analyses combined into sports_all_seasons.md"
