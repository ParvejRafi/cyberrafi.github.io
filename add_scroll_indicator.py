#!/usr/bin/env python3
"""Script to add scroll indicator to hero section"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Scroll indicator HTML
scroll_indicator = '''
        <!-- Scroll Indicator -->
        <div class="scroll-indicator" onclick="document.getElementById('education').scrollIntoView({behavior: 'smooth'})">
            <span>Scroll Down</span>
            <i class="fas fa-chevron-down"></i>
        </div>'''

# Find where to insert (before the closing </section> of hero)
# Look for the pattern that closes the hero section
search_pattern = '            </div>\n        </div>\n    </section>\n\n    <!-- Education Section -->'

if search_pattern in content:
    replacement = '            </div>\n        </div>\n' + scroll_indicator + '\n    </section>\n\n    <!-- Education Section -->'
    content = content.replace(search_pattern, replacement)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Added scroll indicator to hero section")
    print("  - Animated bounce effect")
    print("  - Clickable to scroll to Education section")
else:
    print("✗ Could not find insertion point")
    print("  Trying alternative pattern...")
    
    # Try alternative pattern
    import re
    pattern = r'(</div>\s*</div>\s*</section>\s*<!-- Education Section -->)'
    
    if re.search(pattern, content):
        content = re.sub(
            r'(</div>\s*</div>)\s*(</section>)\s*(<!-- Education Section -->)',
            r'\1\n' + scroll_indicator + r'\n\2\n\n\3',
            content
        )
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✓ Added scroll indicator using alternative method")
    else:
        print("✗ Could not add scroll indicator")
