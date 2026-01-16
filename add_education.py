# Simple script to add Education section after About Me
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find about section
about_pos = content.find('id="about"')

if about_pos > 0:
    # Find the closing </section> tag after about section
    section_end = content.find('</section>', about_pos)
    if section_end > 0:
        section_end += len('</section>')
        
        # Education section HTML
        education_section = """

    <!-- Education Section - POSITIONED RIGHT AFTER ABOUT ME -->
    <section id="education" class="education">
        <div class="container">
            <div class="section-header">
                <h2>Education</h2>
                <div class="underline"></div>
            </div>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <div class="timeline-content">
                        <h3>B.Sc. Computer Science (Cybersecurity)</h3>
                        <h4>Al Bukhary International University, Malaysia</h4>
                        <span class="timeline-date">October 2023 – October 2026</span>
                        <p>CGPA: 3.58 / 4.00</p>
                        <div class="achievement-badge">
                            <i class="fas fa-trophy"></i> Dean's List 2024 & 2025
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
        
        # Insert education section right after about section
        new_content = content[:section_end] + education_section + content[section_end:]
        
        # Write the updated content
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ SUCCESS!")
        print("✓ Education section added right after About Me section")
        print("✓ Refresh your browser at http://localhost:5500 to see the changes")
    else:
        print("ERROR: Could not find section closing tag")
else:
    print("ERROR: Could not find About section")
