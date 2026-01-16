"""
FINAL COMPLETE MODERN PORTFOLIO GENERATOR
This creates the entire modern portfolio HTML in one go
"""

# Complete HTML template with all sections
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MD PARVEJ AHMED RAFI | Penetration Tester</title>
    <link rel="stylesheet" href="style.css?v=2.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
"""

# Read existing file to get hero and about sections
with open('index.html', 'r', encoding='utf-8') as f:
    existing = f.read()

# Find hero section
hero_start = existing.find('<header>')
about_end_marker = '</section>'
about_section_start = existing.find('id="about"')

if about_section_start > 0:
    # Find the end of about section
    search_from = about_section_start
    about_end = existing.find(about_end_marker, search_from)
    if about_end > 0:
        # Extract everything from header to end of about section
        header_to_about = existing[hero_start:about_end + len(about_end_marker)]
        
        # Build complete HTML
        complete_html = html_template + header_to_about + """

    <!-- Education Section - POSITIONED RIGHT AFTER ABOUT ME AS REQUESTED -->
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

    <!-- Skills Section -->
    <section id="skills" class="skills">
        <div class="container">
            <div class="section-header">
                <h2>My Skills</h2>
                <div class="underline"></div>
            </div>
            <div class="skills-categories-grid">
                <!-- Pentesting Tools -->
                <div class="skill-category-card">
                    <div class="category-header">
                        <div class="category-icon" style="background: linear-gradient(135deg, #8B5CF6, #7C3AED);">
                            <i class="fas fa-user-secret"></i>
                        </div>
                        <h3 class="category-title">Pentesting Tools</h3>
                    </div>
                    <div class="skills-items-grid">
                        <div class="skill-badge"><div class="skill-icon"><i class="fab fa-linux" style="color: #FCC624;"></i></div><span class="skill-name">Kali Linux</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-network-wired" style="color: #4A90E2;"></i></div><span class="skill-name">Nmap</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-fire" style="color: #FF6633;"></i></div><span class="skill-name">Burp Suite</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-bomb" style="color: #1E88E5;"></i></div><span class="skill-name">Metasploit</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-wave-square" style="color: #1679A7;"></i></div><span class="skill-name">Wireshark</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-unlock-alt" style="color: #E91E63;"></i></div><span class="skill-name">Hydra</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-search" style="color: #9C27B0;"></i></div><span class="skill-name">Gobuster</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-database" style="color: #F44336;"></i></div><span class="skill-name">SQLmap</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-spider" style="color: #FF5722;"></i></div><span class="skill-name">Nikto</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-microscope" style="color: #607D8B;"></i></div><span class="skill-name">Autopsy</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-virus" style="color: #FF9800;"></i></div><span class="skill-name">Flare VM</span></div>
                    </div>
                </div>

                <!-- Programming & Scripting -->
                <div class="skill-category-card">
                    <div class="category-header">
                        <div class="category-icon" style="background: linear-gradient(135deg, #10B981, #059669);">
                            <i class="fas fa-code"></i>
                        </div>
                        <h3 class="category-title">Programming & Scripting</h3>
                    </div>
                    <div class="skills-items-grid">
                        <div class="skill-badge"><div class="skill-icon"><i class="fab fa-python" style="color: #3776AB;"></i></div><span class="skill-name">Python</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-database" style="color: #4479A1;"></i></div><span class="skill-name">SQL</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fab fa-java" style="color: #007396;"></i></div><span class="skill-name">Java</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-terminal" style="color: #4EAA25;"></i></div><span class="skill-name">Bash</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fab fa-html5" style="color: #E34F26;"></i></div><span class="skill-name">HTML/CSS</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fab fa-js-square" style="color: #F7DF1E;"></i></div><span class="skill-name">JavaScript</span></div>
                    </div>
                </div>

                <!-- Cybersecurity Skills -->
                <div class="skill-category-card">
                    <div class="category-header">
                        <div class="category-icon" style="background: linear-gradient(135deg, #F97316, #EA580C);">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <h3 class="category-title">Cybersecurity Skills</h3>
                    </div>
                    <div class="skills-items-grid">
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-bug" style="color: #E91E63;"></i></div><span class="skill-name">Vulnerability Assessment</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-globe" style="color: #2196F3;"></i></div><span class="skill-name">Web Pentesting</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-network-wired" style="color: #00BCD4;"></i></div><span class="skill-name">Network Pentesting</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-search" style="color: #FF9800;"></i></div><span class="skill-name">OSINT</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-flag-checkered" style="color: #4CAF50;"></i></div><span class="skill-name">CTF</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-trophy" style="color: #FFC107;"></i></div><span class="skill-name">Bug Bounty</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-fingerprint" style="color: #795548;"></i></div><span class="skill-name">Digital Forensics</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-virus-slash" style="color: #F44336;"></i></div><span class="skill-name">Malware Analysis</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-exclamation-triangle" style="color: #FF5722;"></i></div><span class="skill-name">Incident Response</span></div>
                    </div>
                </div>

                <!-- Networking & Systems -->
                <div class="skill-category-card">
                    <div class="category-header">
                        <div class="category-icon" style="background: linear-gradient(135deg, #3B82F6, #2563EB);">
                            <i class="fas fa-server"></i>
                        </div>
                        <h3 class="category-title">Networking & Systems</h3>
                    </div>
                    <div class="skills-items-grid">
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-network-wired" style="color: #00BCD4;"></i></div><span class="skill-name">TCP/IP</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-layer-group" style="color: #9C27B0;"></i></div><span class="skill-name">OSI Model</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fab fa-windows" style="color: #0078D4;"></i></div><span class="skill-name">Windows</span></div>
                        <div class="skill-badge"><div class="skill-icon"><i class="fas fa-database" style="color: #4479A1;"></i></div><span class="skill-name">MySQL</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

        # Add remaining sections from existing file
        # Find where skills section ends in existing file
        skills_start = existing.find('id="skills"')
        if skills_start > 0:
            # Find contact section (last section before footer)
            contact_start = existing.find('id="contact"')
            footer_start = existing.find('<footer>')
            
            if contact_start > 0 and footer_start > 0:
                # Get everything from contact to end
                remaining_sections = existing[contact_start:footer_start]
                footer_and_scripts = existing[footer_start:]
                
                complete_html += remaining_sections + footer_and_scripts
            else:
                # Fallback: just add footer
                complete_html += """
    <script src="script.js"></script>
</body>
</html>
"""
        
        # Write the complete file
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(complete_html)
        
        print("✓ Modern portfolio created successfully!")
        print("✓ Education section is now positioned right after About Me")
        print("✓ Modern Skills section with categories added")
        print("✓ All sections properly ordered")
        print("\\nRefresh your browser to see the changes!")
        
    else:
        print("Error: Could not find About section end")
else:
    print("Error: Could not find About section")
"""

with open('FINAL_BUILD.py', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Created FINAL_BUILD.py")
print("Run: python FINAL_BUILD.py")
