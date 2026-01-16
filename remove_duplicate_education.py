#!/usr/bin/env python3
"""Script to remove duplicate Education section"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find all Education section markers
education_sections = []
for i, line in enumerate(lines):
    if '<!-- Education Section' in line or 'id="education"' in line:
        education_sections.append(i)

print(f"Found Education section markers at lines: {[i+1 for i in education_sections]}")

# Find the first complete Education section (the duplicate one that appears first)
# It should be from around line 205 to 216
first_section_start = None
first_section_end = None

for i, line in enumerate(lines):
    # Look for the first occurrence of the HSC education that's NOT part of the main section
    if i < 220 and 'Higher Secondary Certificate (HSC)' in line:
        # This is the orphaned HSC section, find its boundaries
        # Go back to find the start
        for j in range(i, max(0, i-20), -1):
            if '<div class="timeline-item">' in lines[j]:
                first_section_start = j
                break
        # Go forward to find the end
        for j in range(i, min(len(lines), i+20)):
            if '</section>' in lines[j]:
                first_section_end = j + 1
                break
        break

if first_section_start is not None and first_section_end is not None:
    print(f"Removing duplicate section from lines {first_section_start+1} to {first_section_end}")
    
    # Remove the duplicate section
    new_lines = lines[:first_section_start] + lines[first_section_end:]
    
    # Write back to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"✓ Removed duplicate Education section ({first_section_end - first_section_start} lines)")
else:
    print("✓ No duplicate section found or already cleaned up")
