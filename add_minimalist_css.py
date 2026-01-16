#!/usr/bin/env python3
"""Script to add CSS for minimalist hero design"""

# CSS for the new minimalist hero design
minimalist_hero_css = '''
/* Minimalist Hero Design */
.hero-name {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.name-first {
    color: #1a1a1a;
    font-weight: 700;
}

.name-last {
    color: #4169E1;
    font-weight: 800;
    background: linear-gradient(135deg, #4169E1, #667eea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.role-badge-container {
    margin-bottom: 1.5rem;
}

.role-badge {
    display: inline-block;
    padding: 0.6rem 1.5rem;
    background: #4169E1;
    color: white;
    border-radius: 50px;
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.hero-description {
    font-size: 1rem;
    line-height: 1.7;
    color: #4a5568;
    margin-bottom: 1.5rem;
    max-width: 550px;
}

.hero-location {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #718096;
    font-size: 0.9rem;
    margin-bottom: 2rem;
}

.hero-location i {
    color: #4169E1;
}

.hero-social-icons {
    display: flex;
    gap: 1rem;
}

.hero-social-icons .social-icon {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #f7fafc;
    border: 2px solid #e2e8f0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #4a5568;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    text-decoration: none;
}

.hero-social-icons .social-icon:hover {
    background: #4169E1;
    border-color: #4169E1;
    color: white;
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(65, 105, 225, 0.3);
}

/* Responsive */
@media only screen and (max-width: 768px) {
    .hero-name {
        font-size: 2.5rem;
    }
    
    .hero-description {
        font-size: 0.95rem;
    }
}

@media only screen and (max-width: 480px) {
    .hero-name {
        font-size: 2rem;
    }
    
    .role-badge {
        font-size: 0.85rem;
        padding: 0.5rem 1.2rem;
    }
}
'''

# Read CSS file
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Check if minimalist hero CSS already exists
if '.hero-name' not in css_content or '.name-last' not in css_content:
    # Find where to insert (before Skills Section)
    marker = '/* ====================\n   Skills Section\n   ==================== */'
    
    if marker in css_content:
        css_content = css_content.replace(marker, minimalist_hero_css + '\n' + marker)
        
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print("✓ Added minimalist hero CSS styles")
        print("  - Split name styling (black + blue gradient)")
        print("  - Blue pill badge for role")
        print("  - Clean description and location")
        print("  - Minimal social icon buttons")
    else:
        # Append to end
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write('\n' + minimalist_hero_css)
        print("✓ Added minimalist hero CSS to end of file")
else:
    print("  Minimalist hero CSS already exists")
