#!/usr/bin/env python3
"""Script to add CSS for resume button"""

# CSS for the resume button
resume_btn_css = '''
/* Resume Button Styles */
.resume-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.8rem 2rem;
    background: transparent;
    color: var(--accent-color);
    border: 2px solid var(--accent-color);
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.95rem;
    text-decoration: none;
    transition: all 0.3s ease;
    margin-top: 1rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.resume-btn:hover {
    background: var(--accent-color);
    color: var(--primary-dark);
    transform: translateY(-3px);
    box-shadow: 0 5px 20px rgba(0, 238, 255, 0.4);
}

.resume-btn i {
    font-size: 1.1rem;
}

@media only screen and (max-width: 768px) {
    .resume-btn {
        padding: 0.7rem 1.5rem;
        font-size: 0.85rem;
    }
}
'''

# Append to style.css
with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + resume_btn_css)

print("Added resume button CSS.")
