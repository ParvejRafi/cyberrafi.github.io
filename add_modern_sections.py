# Add modern Skills section with categories
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to insert the modern skills section (after Education)
education_end = content.find('</section>', content.find('id="education"'))

if education_end > 0:
    education_end += len('</section>')
    
    # Modern Skills Section with categories
    modern_skills = """

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

    <!-- Cybersecurity Profiles Section -->
    <section id="cybersecurity-profiles" class="cybersecurity-profiles">
        <div class="container">
            <div class="section-header">
                <h2>Practice Platforms</h2>
                <div class="underline"></div>
                <p class="section-description">My active profiles on cybersecurity challenge platforms</p>
            </div>

            <div class="profile-cards-grid">
                <!-- TryHackMe -->
                <a href="https://tryhackme.com/p/cyberhackrafi" target="_blank" class="profile-card">
                    <div class="card-header">
                        <div class="platform-logo">
                            <img src="https://tryhackme.com/img/favicon.png" alt="TryHackMe" class="logo-img">
                        </div>
                        <h4 class="platform-name">TryHackMe</h4>
                        <i class="fas fa-external-link-alt card-link-icon"></i>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-row">
                            <span class="stat-label">Solved:</span>
                            <span class="stat-value">70 Rooms</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Rank:</span>
                            <span class="stat-value">Top 9%</span>
                        </div>
                    </div>
                </a>

                <!-- CyberTalents -->
                <a href="#" target="_blank" class="profile-card">
                    <div class="card-header">
                        <div class="platform-logo">
                            <i class="fas fa-trophy" style="color: #00A8E8;"></i>
                        </div>
                        <h4 class="platform-name">CyberTalents</h4>
                        <i class="fas fa-external-link-alt card-link-icon"></i>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-row">
                            <span class="stat-label">Points:</span>
                            <span class="stat-value">500+</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Challenges:</span>
                            <span class="stat-value">25+</span>
                        </div>
                    </div>
                </a>

                <!-- PicoCTF -->
                <a href="#" target="_blank" class="profile-card">
                    <div class="card-header">
                        <div class="platform-logo">
                            <img src="https://picoctf.org/img/logos/picoctf-logo-horizontal-white.svg" alt="PicoCTF" class="logo-img">
                        </div>
                        <h4 class="platform-name">PicoCTF</h4>
                        <i class="fas fa-external-link-alt card-link-icon"></i>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-row">
                            <span class="stat-label">Solved:</span>
                            <span class="stat-value">50+</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Points:</span>
                            <span class="stat-value">5000+</span>
                        </div>
                    </div>
                </a>

                <!-- PortSwigger -->
                <a href="#" target="_blank" class="profile-card">
                    <div class="card-header">
                        <div class="platform-logo">
                            <i class="fas fa-bug" style="color: #FF6633;"></i>
                        </div>
                        <h4 class="platform-name">PortSwigger</h4>
                        <i class="fas fa-external-link-alt card-link-icon"></i>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-row">
                            <span class="stat-label">Labs:</span>
                            <span class="stat-value">30+</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Level:</span>
                            <span class="stat-value">Advanced</span>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- CTF Participations & Achievements Section -->
    <section id="ctf-achievements" class="ctf-achievements">
        <div class="container">
            <div class="section-header">
                <h2>CTF Participations & <span class="highlight-text">Achievements</span></h2>
                <div class="underline"></div>
                <p class="section-description">Competing as: <span class="handle-name">LizardXCipher</span> 🦎⚡</p>
            </div>

            <!-- Achievement Cards Grid -->
            <div class="achievements-grid">
                <!-- AIU CTF 2026 - Winner -->
                <div class="achievement-card">
                    <div class="card-top-border" style="background: linear-gradient(90deg, #3B82F6, #2563EB);"></div>
                    <div class="card-icon">
                        <i class="fas fa-trophy"></i>
                    </div>
                    <a href="#" class="card-external-link" target="_blank">
                        <i class="fas fa-external-link-alt"></i>
                    </a>

                    <h3 class="achievement-name">AIU CTF Competition 2026</h3>

                    <div class="achievement-badge winner">
                        <i class="fas fa-medal"></i> 1st Place
                    </div>

                    <div class="achievement-details">
                        <div class="detail-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span>7 January 2026</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>On-site</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-users"></i>
                            <span>Albukhary International University</span>
                        </div>
                    </div>

                    <p class="achievement-summary">Winner among 10 teams with 210 points. Awarded RM 1,500 prize.</p>
                </div>

                <!-- Curtin CTF Hackathon v3.0 -->
                <div class="achievement-card">
                    <div class="card-top-border" style="background: linear-gradient(90deg, #10B981, #059669);"></div>
                    <div class="card-icon">
                        <i class="fas fa-flag-checkered"></i>
                    </div>
                    <a href="#" class="card-external-link" target="_blank">
                        <i class="fas fa-external-link-alt"></i>
                    </a>

                    <h3 class="achievement-name">Curtin CTF Hackathon v3.0</h3>

                    <div class="achievement-badge first-team">
                        <i class="fas fa-star"></i> 1st AIU Team
                    </div>

                    <div class="achievement-details">
                        <div class="detail-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span>6–7 Dec 2025</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-laptop"></i>
                            <span>24-hour Online</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-university"></i>
                            <span>Curtin University Malaysia</span>
                        </div>
                    </div>

                    <p class="achievement-summary">1st among AIU teams, 31st nationwide with 5,476 points.</p>
                </div>

                <!-- Integrated Hawkers CTF -->
                <div class="achievement-card">
                    <div class="card-top-border" style="background: linear-gradient(90deg, #E91E63, #C2185B);"></div>
                    <div class="card-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <a href="#" class="card-external-link" target="_blank">
                        <i class="fas fa-external-link-alt"></i>
                    </a>

                    <h3 class="achievement-name">Integrated Hawkers CTF</h3>

                    <div class="achievement-badge top-rank">
                        <i class="fas fa-award"></i> 55th Place
                    </div>

                    <div class="achievement-details">
                        <div class="detail-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span>2025</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-laptop"></i>
                            <span>Online</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-users"></i>
                            <span>Integrated Hawkers</span>
                        </div>
                    </div>

                    <p class="achievement-summary">55th out of 139 participants with 535 points.</p>
                </div>
            </div>
        </div>
    </section>
"""
    
    # Find old skills section and remove it
    old_skills_start = content.find('id="skills"')
    if old_skills_start > 0:
        # Find the end of old skills section
        old_skills_end = content.find('</section>', old_skills_start)
        if old_skills_end > 0:
            old_skills_end += len('</section>')
            # Remove old skills section
            content = content[:old_skills_start - 20] + content[old_skills_end:]
    
    # Insert new sections after education
    education_end = content.find('</section>', content.find('id="education"'))
    if education_end > 0:
        education_end += len('</section>')
        new_content = content[:education_end] + modern_skills + content[education_end:]
        
        # Write updated content
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ Modern Skills section added with categories!")
        print("✓ Practice Platforms section added!")
        print("✓ CTF Participations & Achievements section added!")
        print("\\nRefresh your browser to see all the new sections!")
    else:
        print("Error: Could not find education section end")
else:
    print("Error: Could not find education section")
