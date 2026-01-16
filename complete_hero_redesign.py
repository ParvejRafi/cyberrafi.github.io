#!/usr/bin/env python3
"""Script to completely redesign hero section - clean and professional"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Brand new clean hero design
new_hero_design = '''            <div class="hero-content">
                <!-- Left Side: Text Content -->
                <div class="hero-left">
                    <!-- Name -->
                    <h1 class="hero-main-name">
                        <span class="name-line">MD PARVEJ</span>
                        <span class="name-line">AHMED</span>
                        <span class="name-line name-highlight">RAFI</span>
                    </h1>

                    <!-- Role Badge -->
                    <div class="hero-role-badge">
                        <span>Penetration Tester</span>
                    </div>

                    <!-- Description -->
                    <p class="hero-desc">
                        Currently pursuing B.Sc. in Computer Science with a focus on Cybersecurity at Al Bukhary International University, Malaysia. Passionate about building innovative solutions and exploring cybersecurity.
                    </p>

                    <!-- Location -->
                    <div class="hero-location-info">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Al Bukhary International University, Malaysia</span>
                    </div>

                    <!-- Action Buttons -->
                    <div class="hero-actions">
                        <a href="#contact" class="hero-btn hero-btn-primary">
                            Get In Touch
                            <i class="fas fa-arrow-right"></i>
                        </a>
                        <a href="#projects" class="hero-btn hero-btn-secondary">
                            View Projects
                            <i class="fas fa-code"></i>
                        </a>
                    </div>
                </div>

                <!-- Center: Stats Cards -->
                <div class="hero-center">
                    <div class="stat-card">
                        <div class="stat-number">5+</div>
                        <div class="stat-label">CERTIFICATIONS</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">3.58</div>
                        <div class="stat-label">GPA</div>
                    </div>
                </div>

                <!-- Right Side: Profile Image -->
                <div class="hero-right">
                    <div class="profile-image-container">
                        <div class="profile-gradient-border">
                            <div class="profile-image-wrapper">
                                <img src="assets/profile.jpg" alt="MD Parvej Ahmed Rafi" class="profile-img" id="profileImg">
                            </div>
                        </div>
                    </div>
                    <!-- Carousel Dots -->
                    <div class="carousel-dots">
                        <span class="dot active" data-slide="0"></span>
                        <span class="dot" data-slide="1"></span>
                        <span class="dot" data-slide="2"></span>
                        <span class="dot" data-slide="3"></span>
                        <span class="dot" data-slide="4"></span>
                        <span class="dot" data-slide="5"></span>
                        <span class="dot" data-slide="6"></span>
                        <span class="dot" data-slide="7"></span>
                    </div>

                    <!-- Connect Section -->
                    <div class="hero-connect">
                        <div class="connect-label">CONNECT WITH ME</div>
                        <div class="connect-icons">
                            <a href="https://www.linkedin.com/in/parvej-rafi-ba43a3301/" target="_blank" class="connect-icon">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="https://github.com/ParvejRafi" target="_blank" class="connect-icon">
                                <i class="fab fa-github"></i>
                            </a>
                            <a href="https://tryhackme.com/p/cyberhackrafi" target="_blank" class="connect-icon">
                                <i class="fas fa-shield-alt"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>'''

# Find and replace the entire hero-content section
import re

# Pattern to match from hero-content opening to its closing
pattern = r'<div class="hero-content">.*?</div>\s*</div>\s*</div>'

# First, let's find just the hero-content section more precisely
hero_pattern = r'(<div class="hero-content">)(.*?)(</div>\s*<!-- Scroll Indicator -->)'

if re.search(hero_pattern, content, re.DOTALL):
    content = re.sub(hero_pattern, new_hero_design + r'\n\n            \3', content, flags=re.DOTALL)
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Completely redesigned hero section")
    print("  - Clean 3-column layout (left: text, center: stats, right: image)")
    print("  - Large cyan name with highlight")
    print("  - Role badge and description")
    print("  - Action buttons")
    print("  - Stats cards")
    print("  - Profile image with carousel")
    print("  - Connect with me section")
else:
    print("✗ Could not find hero-content section")
    print("  Trying alternative approach...")
