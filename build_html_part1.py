"""
Script to rebuild the modern portfolio HTML with all sections
"""

html_content = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MD PARVEJ AHMED RAFI | Penetration Tester</title>
    <link rel="stylesheet" href="style.css?v=2.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"
        rel="stylesheet">
</head>

<body>
    <!-- Header Navigation -->
    <header>
        <div class="container">
            <nav>
                <div class="logo">
                    <a href="#home"><span>&lt;</span> PR <span>/&gt;</span></a>
                </div>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#education">Education</a></li>
                    <li><a href="#skills">Skills</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#experience">Experience</a></li>
                    <li><a href="#certifications">Certifications</a></li>
                    <li><a href="#writeups">Writeups</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
                <div class="hamburger">
                    <div class="line"></div>
                    <div class="line"></div>
                    <div class="line"></div>
                </div>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-text">
                    <div class="hero-text-wrapper">
                        <div class="tag-line">
                            <span class="bracket">&lt;</span>
                            <span class="tag-text">Penetration Tester</span>
                            <span class="bracket">/&gt;</span>
                        </div>
                        
                        <h1 class="glitch-text" data-text="MD PARVEJ AHMED RAFI">
                            MD PARVEJ AHMED RAFI
                        </h1>
                        
                        <div class="role-container">
                            <h2>
                                <span class="role-prefix">I'm a </span>
                                <span class="typing-text" id="typingText">Cybersecurity Student</span>
                                <span class="cursor">|</span>
                            </h2>
                        </div>
                        
                        <div class="description-box">
                            <div class="desc-icon"><i class="fas fa-terminal"></i></div>
                            <p>Cybersecurity student specializing in penetration testing and vulnerability assessment. Skilled in Linux, Python, networking, and offensive security tools with hands-on experience in identifying and exploiting vulnerabilities through real-world projects and bug bounty challenges.</p>
                        </div>
                        
                        <div class="stats-row">
                            <div class="stat-item">
                                <div class="stat-value">10+</div>
                                <div class="stat-label">CTF Challenges</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">5+</div>
                                <div class="stat-label">Certifications</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">3.58</div>
                                <div class="stat-label">GPA</div>
                            </div>
                        </div>
                        
                        <div class="cta-buttons">
                            <a href="#contact" class="btn primary-btn">
                                <span class="btn-text">Get In Touch</span>
                                <span class="btn-icon"><i class="fas fa-arrow-right"></i></span>
                            </a>
                            <a href="#projects" class="btn secondary-btn">
                                <span class="btn-text">View Projects</span>
                                <span class="btn-icon"><i class="fas fa-code"></i></span>
                            </a>
                        </div>
                        
                        <div class="social-section">
                            <div class="social-label">Connect with me</div>
                            <div class="social-icons">
                                <a href="https://www.linkedin.com/in/parvej-rafi-ba43a3301/" target="_blank" class="social-link linkedin">
                                    <i class="fab fa-linkedin"></i>
                                    <span class="social-tooltip">LinkedIn</span>
                                </a>
                                <a href="https://github.com/ParvejRafi" target="_blank" class="social-link github">
                                    <i class="fab fa-github"></i>
                                    <span class="social-tooltip">GitHub</span>
                                </a>
                                <a href="https://tryhackme.com/p/cyberhackrafi" target="_blank" class="social-link tryhackme">
                                    <i class="fas fa-shield-alt"></i>
                                    <span class="social-tooltip">TryHackMe</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="hero-image">
                    <div class="cyber-animation">
                        <canvas id="networkCanvas"></canvas>
                        <canvas id="particleCanvas"></canvas>
                        
                        <!-- 3D Rotating Rings -->
                        <div class="ring-container">
                            <div class="ring ring-1"></div>
                            <div class="ring ring-2"></div>
                            <div class="ring ring-3"></div>
                        </div>
                        
                        <!-- Radar Sweep -->
                        <div class="radar">
                            <div class="radar-sweep"></div>
                            <div class="radar-dot" style="top: 30%; left: 40%;"></div>
                            <div class="radar-dot" style="top: 60%; left: 70%;"></div>
                            <div class="radar-dot" style="top: 45%; left: 25%;"></div>
                            <div class="radar-dot" style="top: 70%; left: 50%;"></div>
                        </div>
                        
                        <!-- Code Rain -->
                        <div class="code-rain">
                            <span>0x4A7F</span>
                            <span>0xC3E9</span>
                            <span>0x8B2D</span>
                            <span>0xF1A6</span>
                        </div>
                        
                        <!-- Central Icon with Layers -->
                        <div class="central-icon">
                            <div class="icon-layer layer-1">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <div class="icon-layer layer-2">
                                <i class="fas fa-lock"></i>
                            </div>
                            <div class="pulse-ring"></div>
                            <div class="pulse-ring pulse-ring-delay-1"></div>
                            <div class="pulse-ring pulse-ring-delay-2"></div>
                        </div>
                        
                        <!-- Hexagonal Grid -->
                        <div class="hex-grid">
                            <div class="hex"></div>
                            <div class="hex"></div>
                            <div class="hex"></div>
                            <div class="hex"></div>
                            <div class="hex"></div>
                            <div class="hex"></div>
                            <div class="hex"></div>
                            <div class="hex"></div>
                        </div>
                        
                        <!-- Glitch Lines -->
                        <div class="glitch-line glitch-1"></div>
                        <div class="glitch-line glitch-2"></div>
                        
                        <!-- Data Streams -->
                        <div class="data-stream stream-left">
                            <span>► THREAT DETECTED</span>
                            <span>► FIREWALL ACTIVE</span>
                            <span>► SYSTEM SECURE</span>
                        </div>
                        
                        <div class="data-stream stream-right">
                            <span>◄ PORT SCAN: 443</span>
                            <span>◄ SSL/TLS: OK</span>
                            <span>◄ ENCRYPTION: AES-256</span>
                        </div>
                        
                        <!-- Status Indicators -->
                        <div class="status-indicators">
                            <div class="status-bar">
                                <div class="status-fill"></div>
                            </div>
                            <div class="status-text">SECURITY LEVEL: <span class="status-value">97%</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="section-header">
                <h2>About Me</h2>
                <div class="underline"></div>
            </div>

            <div class="about-main-content">
                <!-- Left: Profile Card -->
                <div class="about-profile-card">
                    <div class="profile-card-inner">
                        <div class="profile-header">
                            <div class="profile-avatar">
                                <div class="avatar-circle">
                                    <i class="fas fa-user-shield"></i>
                                </div>
                                <div class="status-indicator">
                                    <span class="status-dot"></span>
                                    <span class="status-text">Available for Work</span>
                                </div>
                            </div>
                        </div>

                        <div class="profile-info">
                            <h3>MD Parvej Ahmed Rafi</h3>
                            <p class="profile-role">Cybersecurity Specialist</p>

                            <div class="profile-stats">
                                <div class="profile-stat">
                                    <div class="stat-icon"><i class="fas fa-graduation-cap"></i></div>
                                    <div class="stat-detail">
                                        <span class="stat-label">Education</span>
                                        <span class="stat-value">B.Sc. Computer Science</span>
                                    </div>
                                </div>
                                <div class="profile-stat">
                                    <div class="stat-icon"><i class="fas fa-trophy"></i></div>
                                    <div class="stat-detail">
                                        <span class="stat-label">Achievement</span>
                                        <span class="stat-value">Dean's List 2024 & 2025</span>
                                    </div>
                                </div>
                                <div class="profile-stat">
                                    <div class="stat-icon"><i class="fas fa-map-marker-alt"></i></div>
                                    <div class="stat-detail">
                                        <span class="stat-label">Location</span>
                                        <span class="stat-value">Alor Setar, Malaysia</span>
                                    </div>
                                </div>
                            </div>

                            <div class="quick-contact">
                                <a href="mailto:mdparvej.ahmedrafi@student.aiu.edu.my" class="contact-btn">
                                    <i class="fas fa-envelope"></i>
                                    <span>Email Me</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right: Content -->
                <div class="about-content-right">
                    <!-- Bio Section -->
                    <div class="bio-section">
                        <div class="bio-header">
                            <i class="fas fa-user-circle"></i>
                            <h3>Who Am I?</h3>
                        </div>
                        <p>I am a <span class="highlight">passionate cybersecurity student</span> specializing in
                            penetration testing and vulnerability assessment. My expertise spans across offensive
                            security, web application testing, network security, and OSINT techniques.</p>
                        <p>Currently pursuing my <span class="highlight">B.Sc. in Computer Science</span> with a focus
                            on Cybersecurity at Al Bukhary International University, Malaysia, I am constantly expanding
                            my knowledge through hands-on projects, CTF challenges, and bug bounty programs.</p>
                    </div>

                    <!-- Expertise Areas -->
                    <div class="expertise-grid">
                        <div class="expertise-card">
                            <div class="expertise-icon">
                                <i class="fas fa-bug"></i>
                            </div>
                            <h4>Penetration Testing</h4>
                            <p>Expert in identifying and exploiting vulnerabilities in web applications and networks</p>
                        </div>

                        <div class="expertise-card">
                            <div class="expertise-icon">
                                <i class="fas fa-shield-virus"></i>
                            </div>
                            <h4>VAPT</h4>
                            <p>Comprehensive vulnerability assessment and penetration testing services</p>
                        </div>

                        <div class="expertise-card">
                            <div class="expertise-icon">
                                <i class="fas fa-search"></i>
                            </div>
                            <h4>OSINT</h4>
                            <p>Advanced open-source intelligence gathering and reconnaissance techniques</p>
                        </div>

                        <div class="expertise-card">
                            <div class="expertise-icon">
                                <i class="fas fa-trophy"></i>
                            </div>
                            <h4>Bug Bounty</h4>
                            <p>Active researcher on platforms like YesWeHack and HackerOne</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

'''

# Write to file
with open('index_part1.txt', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Part 1 created successfully")
