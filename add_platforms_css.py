# Add CSS for Practice Platforms section
css_to_add = """

/* ====================
   Practice Platforms Section
   ==================== */
.practice-platforms {
    padding: var(--spacing-xl) 0;
    background: var(--primary-dark);
}

.platforms-category {
    margin-bottom: 3rem;
}

.platforms-category:last-child {
    margin-bottom: 0;
}

.category-title {
    font-size: 1.5rem;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    padding-left: 0.5rem;
    border-left: 4px solid var(--accent-color);
}

.platforms-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
}

.platform-card {
    background: linear-gradient(135deg, rgba(0, 238, 255, 0.03) 0%, rgba(0, 255, 102, 0.02) 100%);
    border: 2px solid rgba(0, 238, 255, 0.15);
    border-radius: 16px;
    padding: 1.5rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.platform-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent-color), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.platform-card:hover {
    transform: translateY(-5px);
    border-color: var(--accent-color);
    box-shadow: 0 10px 30px rgba(0, 238, 255, 0.2);
}

.platform-card:hover::before {
    opacity: 1;
}

.platform-card.featured {
    border-color: var(--accent-color-2);
}

.platform-card.featured:hover {
    box-shadow: 0 10px 30px rgba(0, 255, 102, 0.2);
}

.platform-header {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(0, 238, 255, 0.1);
}

.platform-logo {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    font-size: 1.3rem;
}

.platform-name {
    flex: 1;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
}

.external-link {
    color: var(--text-muted);
    font-size: 0.9rem;
    transition: all 0.3s ease;
}

.external-link:hover {
    color: var(--accent-color);
    transform: translateY(-2px);
}

.platform-stats {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
    margin-bottom: 1rem;
}

.stat-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.9rem;
}

.stat-label {
    color: var(--text-muted);
    font-weight: 500;
}

.stat-value {
    color: var(--text-primary);
    font-weight: 600;
}

.platform-username {
    font-size: 0.85rem;
    color: var(--text-muted);
    padding-top: 0.8rem;
    border-top: 1px solid rgba(0, 238, 255, 0.1);
}

/* TryHackMe Badge */
.thm-badge {
    margin-top: 1rem;
    background: linear-gradient(135deg, rgba(0, 255, 102, 0.1) 0%, rgba(0, 238, 255, 0.05) 100%);
    border: 1px solid rgba(0, 255, 102, 0.2);
    border-radius: 12px;
    padding: 1rem;
}

.badge-content {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}

.badge-avatar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(0, 0, 0, 0.3);
    padding: 0.6rem 1rem;
    border-radius: 8px;
}

.rank-text {
    color: var(--text-primary);
    font-weight: 600;
    font-size: 0.9rem;
}

.rank-icon {
    color: var(--accent-color-2);
    font-size: 1.2rem;
}

.badge-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.5rem;
}

.badge-stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.75rem;
}

.badge-stat i {
    color: var(--accent-color-2);
    font-size: 0.9rem;
}

.badge-stat span {
    color: var(--text-secondary);
    font-weight: 600;
}

.badge-url {
    text-align: center;
    font-size: 0.75rem;
    color: var(--text-muted);
    padding-top: 0.5rem;
    border-top: 1px solid rgba(0, 255, 102, 0.1);
}

/* Responsive Design */
@media (max-width: 768px) {
    .platforms-grid {
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 1rem;
    }
    
    .platform-card {
        padding: 1.2rem;
    }
    
    .badge-stats {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .platforms-grid {
        grid-template-columns: 1fr;
    }
}
"""

# Read the existing CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Append the new CSS
css_content += css_to_add

# Write back
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✓ CSS styling added for Practice Platforms section!")
print("✓ Card-based layout with clean design")
print("✓ Separate styling for Coding and CTF platforms")
print("✓ TryHackMe featured badge styling")
print("✓ Hover effects and animations")
print("✓ Responsive design for mobile")
print("\\nRefresh your browser to see the complete design!")
