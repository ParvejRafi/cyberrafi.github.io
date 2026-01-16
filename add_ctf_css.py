# Add CSS for compact CTF cards design
css_to_add = """

/* ====================
   CTF Achievements - Compact Card Design
   ==================== */
.ctf-achievements {
    padding: var(--spacing-xl) 0;
    background: var(--primary-dark);
}

.ctf-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.ctf-card {
    background: linear-gradient(135deg, rgba(0, 238, 255, 0.03) 0%, rgba(0, 255, 102, 0.02) 100%);
    border: 2px solid rgba(0, 238, 255, 0.15);
    border-radius: 16px;
    padding: 1.5rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.ctf-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--accent-color), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.ctf-card:hover {
    transform: translateY(-5px);
    border-color: var(--accent-color);
    box-shadow: 0 10px 30px rgba(0, 238, 255, 0.2);
}

.ctf-card:hover::before {
    opacity: 1;
}

.ctf-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.ctf-icon {
    width: 50px;
    height: 50px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: white;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.ctf-icon i {
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
}

.ctf-external-link {
    color: var(--text-muted);
    font-size: 1rem;
    transition: all 0.3s ease;
}

.ctf-external-link:hover {
    color: var(--accent-color);
    transform: translateY(-2px);
}

.ctf-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1rem;
    line-height: 1.3;
}

.ctf-info-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
    margin-bottom: 1rem;
}

.ctf-info-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.ctf-info-item i {
    color: var(--accent-color);
    font-size: 0.9rem;
    min-width: 16px;
}

.ctf-description {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin: 0;
    padding-top: 1rem;
    border-top: 1px solid rgba(0, 238, 255, 0.1);
}

/* Responsive Design */
@media (max-width: 768px) {
    .ctf-cards-grid {
        grid-template-columns: 1fr;
        gap: 1.2rem;
    }
    
    .ctf-card {
        padding: 1.2rem;
    }
    
    .ctf-info-grid {
        grid-template-columns: 1fr;
        gap: 0.6rem;
    }
}
"""

# Read the existing CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Check if CTF CSS already exists
if '.ctf-cards-grid' in css_content:
    print("CTF CSS already exists, replacing...")
    # Find and replace the CTF section
    start_marker = '/* ====================\n   CTF Achievements'
    start_idx = css_content.find(start_marker)
    if start_idx > 0:
        # Find the next major section
        next_section = css_content.find('\n/* ====================', start_idx + 100)
        if next_section > 0:
            css_content = css_content[:start_idx] + css_to_add + '\n' + css_content[next_section:]
        else:
            css_content = css_content[:start_idx] + css_to_add
    else:
        css_content += css_to_add
else:
    print("Adding new CTF CSS...")
    css_content += css_to_add

# Write back
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✓ CSS styling added for compact CTF cards!")
print("✓ Grid layout with responsive design")
print("✓ Compact card design matching sample")
print("✓ Icon headers with gradient backgrounds")
print("✓ Info grid for details")
print("✓ Hover effects and animations")
print("\\nRefresh your browser to see the complete design!")
