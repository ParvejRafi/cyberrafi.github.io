#!/usr/bin/env python3
"""Script to make hero section full-screen and improve layout"""

# Read CSS file
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# CSS to make hero full-screen
fullscreen_hero_css = '''
/* Full-Screen Hero Section */
.hero {
    min-height: 100vh;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.hero .container {
    height: 100%;
    display: flex;
    align-items: center;
}

.hero-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 4rem;
    width: 100%;
    height: 100%;
    padding: 2rem 0;
}

.hero-text {
    flex: 1;
    max-width: 600px;
}

.hero-image {
    flex: 0 0 400px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}

/* Scroll indicator */
.scroll-indicator {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    animation: bounce 2s infinite;
    cursor: pointer;
    z-index: 10;
}

.scroll-indicator span {
    color: var(--accent-color);
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.scroll-indicator i {
    color: var(--accent-color);
    font-size: 1.5rem;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateX(-50%) translateY(0);
    }
    40% {
        transform: translateX(-50%) translateY(-10px);
    }
    60% {
        transform: translateX(-50%) translateY(-5px);
    }
}

/* Responsive adjustments */
@media only screen and (max-width: 992px) {
    .hero-content {
        flex-direction: column;
        justify-content: center;
        gap: 2rem;
    }
    
    .hero-text {
        max-width: 100%;
        text-align: center;
    }
    
    .hero-image {
        flex: 0 0 auto;
    }
}

@media only screen and (max-width: 768px) {
    .hero {
        min-height: auto;
        height: auto;
        padding: 4rem 0;
    }
    
    .scroll-indicator {
        display: none;
    }
}
'''

# Find and replace the hero section CSS
import re

# Remove old hero CSS if exists
css_content = re.sub(r'/\* Full-Screen Hero Section \*/.*?@media only screen', 
                     '@media only screen', css_content, flags=re.DOTALL, count=1)

# Find a good place to insert (after hero section or at the beginning of media queries)
marker = '/* ====================\n   Skills Section\n   ==================== */'

if marker in css_content:
    css_content = css_content.replace(marker, fullscreen_hero_css + '\n' + marker)
    
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print("✓ Updated hero section CSS for full-screen layout")
    print("  - Hero section now takes full viewport height")
    print("  - Better responsive layout")
    print("  - Added scroll indicator animation")
else:
    # Append to end
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + fullscreen_hero_css)
    print("✓ Added full-screen hero CSS")
