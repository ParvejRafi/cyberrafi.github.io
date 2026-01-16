#!/usr/bin/env python3
"""Script to remove the About Me section from index.html"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start and end of the About section
start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if '<!-- About Section -->' in line:
        start_idx = i
    elif start_idx is not None and '<!-- Education Section' in line:
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
    # Remove the About section (keep the Education comment)
    new_lines = lines[:start_idx] + lines[end_idx:]
    
    # Write back to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"✓ Removed About Me section (lines {start_idx+1} to {end_idx})")
    print(f"✓ Removed {end_idx - start_idx} lines")
else:
    print("✗ Could not find About section markers")
