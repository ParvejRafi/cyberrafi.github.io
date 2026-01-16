#!/usr/bin/env python3
"""Script to redesign hero section to match sample image"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New cleaner hero text design
new_hero_text = '''                <div class="hero-text">
                    <div class="hero-text-wrapper">
                        <!-- Name -->
                        <h1 class="hero-name">
                            <span class="name-first">MD PARVEJ AHMED</span>
                            <span class="name-last">RAFI</span>
                        </h1>

                        <!-- Role Badge -->
                        <div class="role-badge-container">
                            <span class="role-badge">Penetration Tester</span>
                        </div>

                        <!-- Description -->
                        <p class="hero-description">
                            Currently pursuing B.Sc. in Computer Science with a focus on Cybersecurity at Al Bukhary International University, Malaysia. Passionate about building innovative solutions and exploring cybersecurity.
                        </p>

                        <!-- Location -->
                        <div class="hero-location">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>Al Bukhary International University, Malaysia</span>
                        </div>

                        <!-- Social Icons -->
                        <div class="hero-social-icons">
                            <a href="https://github.com/ParvejRafi" target="_blank" class="social-icon" title="GitHub">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="https://www.linkedin.com/in/parvej-rafi-ba43a3301/" target="_blank" class="social-icon" title="LinkedIn">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="mailto:mdparvej.ahmedrafi@student.aiu.edu.my" class="social-icon" title="Email">
                                <i class="fas fa-envelope"></i>
                            </a>
                        </div>
                    </div>
                </div>'''

# Find and replace the hero-text section
import re

# Pattern to match from hero-text opening to its closing
pattern = r'<div class="hero-text">.*?</div>\s*</div>'

if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, new_hero_text, content, flags=re.DOTALL, count=1)
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Redesigned hero section to match sample image")
    print("  - Split name into two parts (first in black, last in blue)")
    print("  - Added blue pill-shaped role badge")
    print("  - Simplified description")
    print("  - Added location with icon")
    print("  - Cleaner social icons at bottom")
else:
    print("✗ Could not find hero-text section to replace")
