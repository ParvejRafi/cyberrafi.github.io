# Add CSS for the card-based skills design
css_to_add = """

/* ====================
   Skills Section - Card-Based Design
   ==================== */
.skills {
    padding: var(--spacing-xl) 0;
    background: var(--primary-dark);
}

.skills-categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.skill-category-card {
    background: linear-gradient(135deg, rgba(0, 238, 255, 0.03) 0%, rgba(0, 255, 102, 0.02) 100%);
    border: 2px solid rgba(0, 238, 255, 0.15);
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.skill-category-card::before {
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

.skill-category-card:hover {
    transform: translateY(-5px);
    border-color: var(--accent-color);
    box-shadow: 0 10px 40px rgba(0, 238, 255, 0.2);
}

.skill-category-card:hover::before {
    opacity: 1;
}

.category-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(0, 238, 255, 0.1);
}

.category-icon {
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

.category-icon i {
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
}

.category-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
}

.skills-items-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    gap: 1rem;
}

.skill-badge {
    background: rgba(0, 238, 255, 0.05);
    border: 1px solid rgba(0, 238, 255, 0.15);
    border-radius: 12px;
    padding: 1rem 0.8rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s ease;
    cursor: pointer;
}

.skill-badge:hover {
    background: rgba(0, 238, 255, 0.1);
    border-color: var(--accent-color);
    transform: translateY(-3px);
    box-shadow: 0 5px 20px rgba(0, 238, 255, 0.2);
}

.skill-icon {
    width: 45px;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    transition: all 0.3s ease;
}

.skill-icon i {
    font-size: 1.8rem;
}

.skill-badge:hover .skill-icon {
    transform: scale(1.1);
    background: rgba(255, 255, 255, 0.1);
}

.skill-name {
    font-size: 0.85rem;
    color: var(--text-secondary);
    text-align: center;
    font-weight: 500;
    line-height: 1.2;
}

.skill-badge:hover .skill-name {
    color: var(--text-primary);
}

/* Responsive Design */
@media (max-width: 768px) {
    .skills-categories-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .skills-items-grid {
        grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
        gap: 0.8rem;
    }
    
    .skill-badge {
        padding: 0.8rem 0.5rem;
    }
    
    .skill-icon {
        width: 40px;
        height: 40px;
    }
    
    .skill-icon i {
        font-size: 1.5rem;
    }
    
    .skill-name {
        font-size: 0.75rem;
    }
}

@media (max-width: 480px) {
    .skills-items-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
"""

# Read the existing CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Check if skills section CSS already exists
if '.skills-categories-grid' in css_content:
    print("Skills CSS already exists, updating...")
    # Find and replace the skills section
    start_marker = '/* ====================\n   Skills Section'
    end_marker = '@media (max-width: 480px) {\n    .skills-items-grid'
    
    start_idx = css_content.find(start_marker)
    if start_idx > 0:
        # Find the end of the skills section (look for next major section or end)
        next_section = css_content.find('\n/* ====================', start_idx + 100)
        if next_section > 0:
            css_content = css_content[:start_idx] + css_to_add + '\n' + css_content[next_section:]
        else:
            css_content = css_content[:start_idx] + css_to_add
    else:
        # Just append at the end
        css_content += css_to_add
else:
    print("Adding new skills CSS...")
    # Append the new CSS
    css_content += css_to_add

# Write back
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✓ CSS styling added for card-based skills design!")
print("✓ Grid layout with responsive design")
print("✓ Hover effects and animations")
print("✓ Category cards with icons")
print("✓ Skill badges with icons and labels")
print("\\nRefresh your browser to see the complete design!")
