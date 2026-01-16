#!/usr/bin/env python3
"""Script to remove duplicate profile section and update CSS"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the duplicate profile-image-section that was added at the top
# This section is between hero-content and hero-text
old_profile_section = '''                <!-- Profile Image Section -->
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

if old_profile_section in content:
    content = content.replace(old_profile_section, '')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Removed duplicate profile section from top of hero")
else:
    print("  No duplicate profile section found (already removed or not present)")

# Now update the CSS to properly style the profile image in hero-image section
css_update = '''
/* Update hero-image to center profile image */
.hero-image {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    min-height: 500px;
}

.hero-image .profile-image-container {
    width: 350px;
    height: 350px;
    margin-bottom: 2rem;
}

.hero-image .carousel-dots {
    margin-top: 1rem;
}

@media only screen and (max-width: 992px) {
    .hero-image .profile-image-container {
        width: 280px;
        height: 280px;
    }
}

@media only screen and (max-width: 768px) {
    .hero-image {
        min-height: 400px;
        margin-top: 2rem;
    }
    
    .hero-image .profile-image-container {
        width: 240px;
        height: 240px;
    }
}
'''

# Read CSS file
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Check if the update already exists
if '.hero-image .profile-image-container' not in css_content:
    # Find where to insert (after profile-image-section styles)
    marker = '/* ====================\n   Skills Section\n   ==================== */'
    
    if marker in css_content:
        css_content = css_content.replace(marker, css_update + '\n' + marker)
        
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print("✓ Updated CSS for hero-image profile styling")
    else:
        # Append to end
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write('\n' + css_update)
        print("✓ Added CSS for hero-image profile styling")
else:
    print("  CSS already updated")
