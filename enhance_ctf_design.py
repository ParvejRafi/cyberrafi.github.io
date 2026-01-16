# Enhance CTF Achievements design with better styling
css_enhancement = """

/* ====================
   CTF Achievements - Enhanced Design
   ==================== */
.ctf-achievements {
    padding: var(--spacing-xl) 0;
    background: var(--primary-dark);
}

.ctf-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.ctf-card {
    background: linear-gradient(135deg, rgba(0, 238, 255, 0.05) 0%, rgba(0, 255, 102, 0.03) 100%);
    border: 2px solid rgba(0, 238, 255, 0.2);
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
}

.ctf-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, transparent, var(--accent-color), var(--accent-color-2), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.ctf-card::after {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(0, 238, 255, 0.03) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
    pointer-events: none;
}

.ctf-card:hover {
    transform: translateY(-8px);
    border-color: var(--accent-color);
    box-shadow: 
        0 20px 40px rgba(0, 238, 255, 0.15),
        0 0 0 1px rgba(0, 238, 255, 0.1);
}

.ctf-card:hover::before {
    opacity: 1;
}

.ctf-card:hover::after {
    opacity: 1;
}

.ctf-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.ctf-icon {
    width: 60px;
    height: 60px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    color: white;
    box-shadow: 
        0 8px 20px rgba(0, 0, 0, 0.4),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    position: relative;
    transition: all 0.3s ease;
}

.ctf-card:hover .ctf-icon {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 
        0 12px 30px rgba(0, 0, 0, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.ctf-icon i {
    filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3));
}

.ctf-external-link {
    color: var(--text-muted);
    font-size: 1.1rem;
    transition: all 0.3s ease;
    padding: 0.5rem;
    border-radius: 8px;
}

.ctf-external-link:hover {
    color: var(--accent-color);
    background: rgba(0, 238, 255, 0.1);
    transform: translateY(-2px);
}

.ctf-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    line-height: 1.4;
    background: linear-gradient(135deg, var(--text-primary), var(--accent-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.ctf-info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding: 1.2rem;
    background: rgba(0, 238, 255, 0.03);
    border-radius: 12px;
    border: 1px solid rgba(0, 238, 255, 0.1);
}

.ctf-info-item {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-size: 0.9rem;
    color: var(--text-secondary);
    padding: 0.5rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.ctf-info-item:hover {
    background: rgba(0, 238, 255, 0.05);
    transform: translateX(3px);
}

.ctf-info-item i {
    color: var(--accent-color);
    font-size: 1rem;
    min-width: 18px;
    filter: drop-shadow(0 0 5px rgba(0, 238, 255, 0.5));
}

.ctf-description {
    font-size: 0.95rem;
    color: var(--text-muted);
    line-height: 1.7;
    margin: 0;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(0, 238, 255, 0.15);
}

/* Add special styling for first place */
.ctf-card:first-child {
    border-color: rgba(255, 215, 0, 0.3);
}

.ctf-card:first-child:hover {
    border-color: #FFD700;
    box-shadow: 
        0 20px 40px rgba(255, 215, 0, 0.2),
        0 0 0 1px rgba(255, 215, 0, 0.1);
}

.ctf-card:first-child::before {
    background: linear-gradient(90deg, transparent, #FFD700, #FFA500, transparent);
}

/* Responsive Design */
@media (max-width: 768px) {
    .ctf-cards-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .ctf-card {
        padding: 1.5rem;
    }
    
    .ctf-icon {
        width: 50px;
        height: 50px;
        font-size: 1.5rem;
    }
    
    .ctf-title {
        font-size: 1.2rem;
    }
    
    .ctf-info-grid {
        grid-template-columns: 1fr;
        gap: 0.8rem;
        padding: 1rem;
    }
}

@media (max-width: 480px) {
    .ctf-card {
        padding: 1.2rem;
    }
}
"""

# Read the existing CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find and replace the CTF section
start_marker = '/* ====================\n   CTF Achievements'
start_idx = css_content.find(start_marker)

if start_idx > 0:
    # Find the next major section or end of CTF section
    next_section = css_content.find('\n/* ====================', start_idx + 100)
    if next_section > 0:
        css_content = css_content[:start_idx] + css_enhancement + '\n' + css_content[next_section:]
    else:
        # If no next section, check for end of file
        end_marker = '@media (max-width: 480px) {\n    .ctf-card'
        end_idx = css_content.find(end_marker, start_idx)
        if end_idx > 0:
            # Find the closing brace
            closing_idx = css_content.find('}', end_idx + 100)
            if closing_idx > 0:
                css_content = css_content[:start_idx] + css_enhancement + css_content[closing_idx + 2:]
            else:
                css_content = css_content[:start_idx] + css_enhancement
        else:
            css_content = css_content[:start_idx] + css_enhancement
else:
    # Append if not found
    css_content += css_enhancement

# Write back
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✓ CTF Achievements design enhanced!")
print("✓ Better visual hierarchy with larger icons")
print("✓ Improved spacing and padding")
print("✓ Enhanced hover effects with smooth animations")
print("✓ Gradient text for titles")
print("✓ Info grid with background and borders")
print("✓ Special gold styling for 1st place achievement")
print("✓ Backdrop blur and glow effects")
print("\\nRefresh your browser to see the enhanced design!")
