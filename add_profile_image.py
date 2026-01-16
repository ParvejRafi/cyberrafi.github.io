#!/usr/bin/env python3
"""Script to add profile image section to hero"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Profile image HTML to add
profile_section = '''                <!-- Profile Image Section -->
                <div class="profile-image-section">
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

'''

# Find the position to insert (after hero-content opening div)
search_pattern = '''            <div class="hero-content">
                <div class="hero-text">'''

# Check if profile section already exists
if 'profile-image-section' in content:
    print("✓ Profile image section already exists")
else:
    # Replace with the new content including profile section
    replacement = '''            <div class="hero-content">
''' + profile_section + '''                <div class="hero-text">'''
    
    if search_pattern in content:
        content = content.replace(search_pattern, replacement)
        
        # Write back to file
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✓ Successfully added profile image section to hero")
        print("  - Added circular image container with gradient border")
        print("  - Added carousel dots indicator")
        print("  - Image path: assets/profile.jpg")
    else:
        print("✗ Could not find the insertion point in the file")
