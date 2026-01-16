# Add CSS for platform logo images
css_to_add = """
/* Platform Logo Images */
.platform-logo-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: brightness(1.2);
}

.platform-card:hover .platform-logo-img {
    filter: brightness(1.4);
}
"""

# Read the existing CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Check if the CSS already exists
if '.platform-logo-img' not in css_content:
    # Append the new CSS
    css_content += css_to_add
    
    # Write back
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print("✓ CSS added for platform logo images")
else:
    print("✓ CSS already exists for platform logos")

print("\\n✓ All done! Refresh your browser to see the official logos!")
