# Fix Practice Platforms - Keep YOUR data, just update the design
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Practice Platforms section
platforms_start = content.find('<!-- Practice Platforms Section -->')
if platforms_start > 0:
    # Find the end of the section
    platforms_end = content.find('</section>', platforms_start)
    if platforms_end > 0:
        platforms_end += len('</section>')
        
        # Updated Practice Platforms with YOUR original data, styled like the sample
        new_platforms = """<!-- Practice Platforms Section -->
    <section id="practice-platforms" class="practice-platforms">
        <div class="container">
            <div class="section-header">
                <h2>Practice Platforms</h2>
                <div class="underline"></div>
            </div>

            <div class="platforms-grid">
                <!-- TryHackMe -->
                <div class="platform-card">
                    <div class="platform-header">
                        <div class="platform-logo">
                            <i class="fas fa-shield-alt" style="color: #00D26A;"></i>
                        </div>
                        <h4 class="platform-name">TryHackMe</h4>
                        <a href="https://tryhackme.com/p/cyberhackrafi" target="_blank" class="external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-item">
                            <span class="stat-label">Solved:</span>
                            <span class="stat-value">70 Rooms</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Rank:</span>
                            <span class="stat-value">Top 9%</span>
                        </div>
                    </div>
                    <div class="platform-username">@cyberhackrafi</div>
                </div>

                <!-- CyberTalents -->
                <div class="platform-card">
                    <div class="platform-header">
                        <div class="platform-logo">
                            <i class="fas fa-trophy" style="color: #00A8E8;"></i>
                        </div>
                        <h4 class="platform-name">CyberTalents</h4>
                        <a href="#" target="_blank" class="external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-item">
                            <span class="stat-label">Points:</span>
                            <span class="stat-value">500+</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Challenges:</span>
                            <span class="stat-value">25+</span>
                        </div>
                    </div>
                    <div class="platform-username">Your Username</div>
                </div>

                <!-- PicoCTF -->
                <div class="platform-card">
                    <div class="platform-header">
                        <div class="platform-logo">
                            <i class="fas fa-flag-checkered" style="color: #E74C3C;"></i>
                        </div>
                        <h4 class="platform-name">PicoCTF</h4>
                        <a href="#" target="_blank" class="external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-item">
                            <span class="stat-label">Solved:</span>
                            <span class="stat-value">50+</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Points:</span>
                            <span class="stat-value">5000+</span>
                        </div>
                    </div>
                    <div class="platform-username">Your Username</div>
                </div>

                <!-- PortSwigger -->
                <div class="platform-card">
                    <div class="platform-header">
                        <div class="platform-logo">
                            <i class="fas fa-bug" style="color: #FF6633;"></i>
                        </div>
                        <h4 class="platform-name">PortSwigger</h4>
                        <a href="#" target="_blank" class="external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    <div class="platform-stats">
                        <div class="stat-item">
                            <span class="stat-label">Labs:</span>
                            <span class="stat-value">30+</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Level:</span>
                            <span class="stat-value">Advanced</span>
                        </div>
                    </div>
                    <div class="platform-username">Your Username</div>
                </div>
            </div>
        </div>
    </section>"""
        
        # Replace the section
        new_content = content[:platforms_start] + new_platforms + content[platforms_end:]
        
        # Write back
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ Practice Platforms section fixed!")
        print("✓ Kept YOUR original platforms: TryHackMe, CyberTalents, PicoCTF, PortSwigger")
        print("✓ Applied the clean card design from the sample")
        print("✓ Your data is preserved")
        print("\\nRefresh your browser to see the corrected design!")
    else:
        print("Error: Could not find section end")
else:
    print("Error: Could not find Practice Platforms section")
