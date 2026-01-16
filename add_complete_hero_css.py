#!/usr/bin/env python3
"""Script to add comprehensive CSS for redesigned hero"""

# Complete CSS for the new hero design
hero_redesign_css = '''
/* ===================================
   COMPLETE HERO REDESIGN - CLEAN LAYOUT
   =================================== */

/* Hero Content Layout */
.hero-content {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 3rem;
    align-items: center;
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
}

/* LEFT SIDE - Text Content */
.hero-left {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.hero-main-name {
    font-size: 4rem;
    font-weight: 900;
    line-height: 1.1;
    margin: 0;
    display: flex;
    flex-direction: column;
}

.name-line {
    color: var(--accent-color);
    text-transform: uppercase;
    letter-spacing: 2px;
}

.name-highlight {
    color: var(--accent-color);
    text-shadow: 0 0 30px rgba(0, 238, 255, 0.5);
}

.hero-role-badge {
    display: inline-block;
    align-self: flex-start;
}

.hero-role-badge span {
    display: inline-block;
    padding: 0.6rem 1.5rem;
    background: var(--accent-color);
    color: var(--primary-dark);
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.hero-desc {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.7;
    max-width: 500px;
    margin: 0;
}

.hero-location-info {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-muted);
    font-size: 0.85rem;
}

.hero-location-info i {
    color: var(--accent-color);
}

.hero-actions {
    display: flex;
    gap: 1rem;
    margin-top: 0.5rem;
}

.hero-btn {
    padding: 0.8rem 1.8rem;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
}

.hero-btn-primary {
    background: var(--accent-color);
    color: var(--primary-dark);
    box-shadow: 0 0 20px rgba(0, 238, 255, 0.3);
}

.hero-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 25px rgba(0, 238, 255, 0.5);
}

.hero-btn-secondary {
    background: transparent;
    color: var(--accent-color);
    border: 2px solid var(--accent-color);
}

.hero-btn-secondary:hover {
    background: rgba(0, 238, 255, 0.1);
    transform: translateY(-2px);
}

/* CENTER - Stats Cards */
.hero-center {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.stat-card {
    background: rgba(0, 238, 255, 0.05);
    border: 1px solid rgba(0, 238, 255, 0.2);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    min-width: 150px;
    transition: all 0.3s ease;
}

.stat-card:hover {
    background: rgba(0, 238, 255, 0.1);
    border-color: var(--accent-color);
    transform: translateY(-5px);
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: var(--accent-color);
    margin-bottom: 0.3rem;
}

.stat-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    letter-spacing: 1px;
    font-weight: 600;
}

/* RIGHT SIDE - Profile & Connect */
.hero-right {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
}

.hero-right .profile-image-container {
    width: 320px;
    height: 320px;
}

.hero-connect {
    text-align: center;
}

.connect-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    letter-spacing: 2px;
    margin-bottom: 1rem;
    font-weight: 600;
}

.connect-icons {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

.connect-icon {
    width: 45px;
    height: 45px;
    border-radius: 8px;
    background: rgba(0, 238, 255, 0.1);
    border: 1px solid rgba(0, 238, 255, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent-color);
    font-size: 1.2rem;
    transition: all 0.3s ease;
    text-decoration: none;
}

.connect-icon:hover {
    background: var(--accent-color);
    color: var(--primary-dark);
    transform: translateY(-3px);
    box-shadow: 0 5px 20px rgba(0, 238, 255, 0.4);
}

/* RESPONSIVE */
@media only screen and (max-width: 1200px) {
    .hero-content {
        grid-template-columns: 1fr;
        gap: 3rem;
        text-align: center;
    }
    
    .hero-left {
        align-items: center;
    }
    
    .hero-main-name {
        font-size: 3rem;
    }
    
    .hero-desc {
        max-width: 600px;
    }
    
    .hero-center {
        flex-direction: row;
        justify-content: center;
    }
    
    .hero-actions {
        justify-content: center;
    }
}

@media only screen and (max-width: 768px) {
    .hero-main-name {
        font-size: 2.5rem;
    }
    
    .hero-center {
        flex-direction: column;
    }
    
    .hero-right .profile-image-container {
        width: 250px;
        height: 250px;
    }
}

@media only screen and (max-width: 480px) {
    .hero-main-name {
        font-size: 2rem;
    }
    
    .hero-actions {
        flex-direction: column;
        width: 100%;
    }
    
    .hero-btn {
        width: 100%;
        justify-content: center;
    }
}
'''

# Read CSS file
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove old hero styles if they exist
import re
css_content = re.sub(r'/\* Minimalist Hero Design \*/.*?@media only screen', 
                     '@media only screen', css_content, flags=re.DOTALL, count=1)

# Find where to insert
marker = '/* ====================\n   Skills Section\n   ==================== */'

if marker in css_content:
    css_content = css_content.replace(marker, hero_redesign_css + '\n' + marker)
    
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print("✓ Added complete hero redesign CSS")
    print("  - 3-column grid layout")
    print("  - Large cyan name styling")
    print("  - Role badge and buttons")
    print("  - Stats cards with hover effects")
    print("  - Profile image and connect section")
    print("  - Fully responsive design")
else:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + hero_redesign_css)
    print("✓ Added CSS to end of file")
