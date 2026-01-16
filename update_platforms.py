# Update Practice Platforms section to match the sample design
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Practice Platforms section
platforms_start = content.find('<!-- Cybersecurity Profiles Section -->')
if platforms_start > 0:
    # Find the end of the section
    platforms_end = content.find('</section>', platforms_start)
    if platforms_end > 0:
        platforms_end += len('</section>')
        
        # New Practice Platforms section matching the sample
        new_platforms = """<!-- Practice Platforms Section -->
    <section id="practice-platforms" class="practice-platforms">
        <div class="container">
            <div class="section-header">
                <h2>Practice Platforms</h2>
                <div class="underline"></div>
            </div>

            <!-- Coding Platforms -->
            <div class="platforms-category">
                <h3 class="category-title">Coding Platforms</h3>
                <div class="platforms-grid">
                    <!-- Codeforces -->
                    <div class="platform-card">
                        <div class="platform-header">
                            <div class="platform-logo">
                                <i class="fas fa-code" style="color: #1F8ACB;"></i>
                            </div>
                            <h4 class="platform-name">Codeforces</h4>
                            <a href="#" target="_blank" class="external-link">
                                <i class="fas fa-external-link-alt"></i>
                            </a>
                        </div>
                        <div class="platform-stats">
                            <div class="stat-item">
                                <span class="stat-label">Solved:</span>
                                <span class="stat-value">465+</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-label">Rating:</span>
                                <span class="stat-value">1112</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-label">Rank:</span>
                                <span class="stat-value">Newbie</span>
                            </div>
                        </div>
                        <div class="platform-username">@samdani1412 & @samdani333</div>
                    </div>

                    <!-- CodeChef -->
                    <div class="platform-card">
                        <div class="platform-header">
                            <div class="platform-logo">
                                <i class="fas fa-utensils" style="color: #5B4638;"></i>
                            </div>
                            <h4 class="platform-name">CodeChef</h4>
                            <a href="#" target="_blank" class="external-link">
                                <i class="fas fa-external-link-alt"></i>
                            </a>
                        </div>
                        <div class="platform-stats">
                            <div class="stat-item">
                                <span class="stat-label">Solved:</span>
                                <span class="stat-value">120+</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-label">Rating:</span>
                                <span class="stat-value">1542</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-label">Rank:</span>
                                <span class="stat-value">2★</span>
                            </div>
                        </div>
                        <div class="platform-username">@samdani1412</div>
                    </div>

                    <!-- LeetCode -->
                    <div class="platform-card">
                        <div class="platform-header">
                            <div class="platform-logo">
                                <i class="fas fa-laptop-code" style="color: #FFA116;"></i>
                            </div>
                            <h4 class="platform-name">LeetCode</h4>
                            <a href="#" target="_blank" class="external-link">
                                <i class="fas fa-external-link-alt"></i>
                            </a>
                        </div>
                        <div class="platform-stats">
                            <div class="stat-item">
                                <span class="stat-label">Solved:</span>
                                <span class="stat-value">106+</span>
                            </div>
                        </div>
                        <div class="platform-username">@samdani1412</div>
                    </div>

                    <!-- CSES -->
                    <div class="platform-card">
                        <div class="platform-header">
                            <div class="platform-logo">
                                <i class="fas fa-book" style="color: #0066CC;"></i>
                            </div>
                            <h4 class="platform-name">CSES</h4>
                            <a href="#" target="_blank" class="external-link">
                                <i class="fas fa-external-link-alt"></i>
                            </a>
                        </div>
                        <div class="platform-stats">
                            <div class="stat-item">
                                <span class="stat-label">Solved:</span>
                                <span class="stat-value">30+</span>
                            </div>
                        </div>
                        <div class="platform-username">@samdani1412</div>
                    </div>
                </div>
            </div>

            <!-- CTF Platforms -->
            <div class="platforms-category">
                <h3 class="category-title">CTF Platforms</h3>
                <div class="platforms-grid">
                    <!-- TryHackMe -->
                    <div class="platform-card featured">
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
                                <span class="stat-value">172</span>
                            </div>
                        </div>
                        <div class="platform-username">@samdani1412</div>
                        <!-- TryHackMe Badge -->
                        <div class="thm-badge">
                            <div class="badge-content">
                                <div class="badge-avatar">
                                    <span class="rank-text">bsse1412</span>
                                    <span class="rank-icon">★</span>
                                </div>
                                <div class="badge-stats">
                                    <div class="badge-stat">
                                        <i class="fas fa-fire"></i>
                                        <span>51803</span>
                                    </div>
                                    <div class="badge-stat">
                                        <i class="fas fa-calendar"></i>
                                        <span>0 days</span>
                                    </div>
                                    <div class="badge-stat">
                                        <i class="fas fa-trophy"></i>
                                        <span>5</span>
                                    </div>
                                    <div class="badge-stat">
                                        <i class="fas fa-flag"></i>
                                        <span>30</span>
                                    </div>
                                </div>
                                <div class="badge-url">tryhackme.com</div>
                            </div>
                        </div>
                    </div>

                    <!-- PicoCTF -->
                    <div class="platform-card">
                        <div class="platform-header">
                            <div class="platform-logo">
                                <i class="fas fa-flag-checkered" style="color: #E74C3C;"></i>
                            </div>
                            <h4 class="platform-name">picoCTF</h4>
                            <a href="#" target="_blank" class="external-link">
                                <i class="fas fa-external-link-alt"></i>
                            </a>
                        </div>
                        <div class="platform-stats">
                            <div class="stat-item">
                                <span class="stat-label">Solved:</span>
                                <span class="stat-value">172</span>
                            </div>
                        </div>
                        <div class="platform-username">@samdani1412</div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
        
        # Replace the section
        new_content = content[:platforms_start] + new_platforms + content[platforms_end:]
        
        # Write back
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ Practice Platforms section updated to match sample design!")
        print("✓ Separated into Coding Platforms and CTF Platforms")
        print("✓ Clean card layout with stats")
        print("✓ TryHackMe featured card with badge")
        print("\\nNow adding CSS styling...")
    else:
        print("Error: Could not find section end")
else:
    print("Error: Could not find Practice Platforms section")
