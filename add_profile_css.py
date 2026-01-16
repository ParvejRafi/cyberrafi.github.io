#!/usr/bin/env python3
"""Script to add profile image CSS styles"""

# CSS styles for profile image section
profile_css = '''
/* ====================
   Profile Image Section
   ==================== */
.profile-image-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2rem;
    animation: fadeInDown 1s ease-out;
}

.profile-image-container {
    position: relative;
    width: 280px;
    height: 280px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.profile-gradient-border {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    padding: 4px;
    background: linear-gradient(135deg, 
        #667eea 0%, 
        #764ba2 25%, 
        #f093fb 50%, 
        #4facfe 75%, 
        #667eea 100%
    );
    background-size: 300% 300%;
    animation: gradientRotate 8s ease infinite;
    box-shadow: 
        0 0 40px rgba(102, 126, 234, 0.6),
        0 0 80px rgba(118, 75, 162, 0.4),
        0 10px 50px rgba(0, 0, 0, 0.3);
}

.profile-image-wrapper {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    overflow: hidden;
    background: var(--secondary-dark);
    border: 3px solid var(--primary-dark);
    position: relative;
}

.profile-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.profile-image-wrapper:hover .profile-img {
    transform: scale(1.1);
}

/* Carousel Dots */
.carousel-dots {
    display: flex;
    gap: 10px;
    justify-content: center;
    align-items: center;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
}

.dot.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    width: 30px;
    border-radius: 5px;
    box-shadow: 0 0 15px rgba(102, 126, 234, 0.8);
}

.dot:hover:not(.active) {
    background: rgba(255, 255, 255, 0.6);
    transform: scale(1.2);
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes gradientRotate {
    0%, 100% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
}

/* Responsive adjustments */
@media only screen and (max-width: 768px) {
    .profile-image-container {
        width: 220px;
        height: 220px;
    }
    
    .profile-image-section {
        margin-bottom: 1.5rem;
    }
}

@media only screen and (max-width: 480px) {
    .profile-image-container {
        width: 180px;
        height: 180px;
    }
}

'''

# Read the current CSS file
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Check if profile image styles already exist
if 'profile-image-section' in css_content:
    print("✓ Profile image CSS already exists")
else:
    # Find a good place to insert (after hero section styles)
    # Insert before the Skills Section
    marker = '/* ====================\n   Skills Section\n   ==================== */'
    
    if marker in css_content:
        css_content = css_content.replace(marker, profile_css + marker)
        
        # Write back to file
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print("✓ Successfully added profile image CSS styles")
        print("  - Circular image with gradient border")
        print("  - Animated gradient rotation")
        print("  - Carousel dots with active state")
        print("  - Hover effects and animations")
        print("  - Responsive design for mobile")
    else:
        # If marker not found, append to end
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write('\n' + profile_css)
        print("✓ Added profile image CSS to end of file")
