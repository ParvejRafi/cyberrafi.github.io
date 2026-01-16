#!/usr/bin/env python3
"""Script to replace cyber animation with profile image"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start and end of the cyber-animation section
start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if '<div class="hero-image">' in line:
        start_idx = i
    elif start_idx is not None and '</div>' in line and 'hero-image' in lines[i-1] if i > 0 else False:
        # This is tricky, we need to find the closing div for hero-image
        pass
    elif start_idx is not None and i > start_idx + 60 and '</div>' in line:
        # The cyber-animation section is quite long, so look for the closing after many lines
        # Check if this might be the closing div
        if i > start_idx + 70:  # cyber-animation section is about 70+ lines
            end_idx = i + 1
            break

# Let's use a different approach - replace the entire cyber-animation div content
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the cyber-animation section
old_section_start = '                <div class="hero-image">\n                    <div class="cyber-animation">'
old_section_end = '                    </div>\n                </div>\n            </div>\n        </div>\n    </section>'

# New profile image section
new_section = '''                <div class="hero-image">
                    <!-- Profile Image Section -->
                    <div class="profile-image-container">
                        <div class="profile-gradient-border">
                            <div class="profile-image-wrapper">
                                <img src="assets/profile.jpg" alt="MD Parvej Ahmed Rafi" class="profile-img" id="profileImg">
                            </div>
                        </div>
                    </div>
                    <!-- Carousel Dots -->
                    <div class="carousel-dots">
                        <span class="dot active" data-slide="0"></span>
                        <span class="dot" data-slide="1"></span>
                        <span class="dot" data-slide="2"></span>
                        <span class="dot" data-slide="3"></span>
                        <span class="dot" data-slide="4"></span>
                        <span class="dot" data-slide="5"></span>
                        <span class="dot" data-slide="6"></span>
                        <span class="dot" data-slide="7"></span>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

# Find the cyber-animation div and replace everything until the section closes
import re

# Pattern to match from hero-image opening to section closing
pattern = r'(<div class="hero-image">.*?</section>)'

# Check if we can find it
if re.search(pattern, content, re.DOTALL):
    # Replace the entire hero-image section
    content = re.sub(
        r'<div class="hero-image">.*?</div>\s*</div>\s*</div>\s*</section>',
        new_section,
        content,
        flags=re.DOTALL
    )
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Successfully replaced cyber animation with profile image")
    print("  - Removed all cyber animation elements")
    print("  - Added circular profile image with gradient border")
    print("  - Added carousel dots for image navigation")
else:
    print("✗ Could not find the section to replace")
