# Update CTF Achievements section to match the compact card design
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the CTF Achievements section
ctf_start = content.find('<!-- CTF Participations & Achievements Section -->')
if ctf_start > 0:
    # Find the end of the section
    ctf_end = content.find('</section>', ctf_start)
    if ctf_end > 0:
        ctf_end += len('</section>')
        
        # New CTF section with YOUR data, styled like the sample
        new_ctf = """<!-- CTF Participations & Achievements Section -->
    <section id="ctf-achievements" class="ctf-achievements">
        <div class="container">
            <div class="section-header">
                <h2>CTF Participations & Achievements</h2>
                <div class="underline"></div>
            </div>

            <div class="ctf-cards-grid">
                <!-- AIU CTF 2026 - 1st Place -->
                <div class="ctf-card">
                    <div class="ctf-card-header">
                        <div class="ctf-icon" style="background: linear-gradient(135deg, #3B82F6, #2563EB);">
                            <i class="fas fa-trophy"></i>
                        </div>
                        <a href="#" target="_blank" class="ctf-external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    
                    <h3 class="ctf-title">AIU CTF Competition 2026</h3>
                    
                    <div class="ctf-info-grid">
                        <div class="ctf-info-item">
                            <i class="fas fa-medal"></i>
                            <span>1st Place</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span>January 2026</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>On-site</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-users"></i>
                            <span>Individual</span>
                        </div>
                    </div>
                    
                    <p class="ctf-description">Winner among 10 teams with 210 points. Awarded RM 1,500 prize at Al Bukhary International University.</p>
                </div>

                <!-- Curtin CTF Hackathon v3.0 -->
                <div class="ctf-card">
                    <div class="ctf-card-header">
                        <div class="ctf-icon" style="background: linear-gradient(135deg, #10B981, #059669);">
                            <i class="fas fa-flag-checkered"></i>
                        </div>
                        <a href="#" target="_blank" class="ctf-external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    
                    <h3 class="ctf-title">Curtin CTF Hackathon v3.0</h3>
                    
                    <div class="ctf-info-grid">
                        <div class="ctf-info-item">
                            <i class="fas fa-star"></i>
                            <span>1st AIU Team</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span>Dec 2025</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-laptop"></i>
                            <span>Online</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-users"></i>
                            <span>Team</span>
                        </div>
                    </div>
                    
                    <p class="ctf-description">1st among AIU teams, 31st nationwide with 5,476 points in 24-hour online competition organized by Curtin University Malaysia.</p>
                </div>

                <!-- Integrated Hawkers CTF -->
                <div class="ctf-card">
                    <div class="ctf-card-header">
                        <div class="ctf-icon" style="background: linear-gradient(135deg, #E91E63, #C2185B);">
                            <i class="fas fa-shield-alt"></i>
                        </div>
                        <a href="#" target="_blank" class="ctf-external-link">
                            <i class="fas fa-external-link-alt"></i>
                        </a>
                    </div>
                    
                    <h3 class="ctf-title">Integrated Hawkers CTF</h3>
                    
                    <div class="ctf-info-grid">
                        <div class="ctf-info-item">
                            <i class="fas fa-award"></i>
                            <span>55th Place</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span>2025</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-laptop"></i>
                            <span>Online</span>
                        </div>
                        <div class="ctf-info-item">
                            <i class="fas fa-users"></i>
                            <span>Individual</span>
                        </div>
                    </div>
                    
                    <p class="ctf-description">Secured 55th position out of 139 participants with 535 points in this competitive cybersecurity challenge.</p>
                </div>
            </div>
        </div>
    </section>"""
        
        # Replace the section
        new_content = content[:ctf_start] + new_ctf + content[ctf_end:]
        
        # Write back
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ CTF Achievements section updated to compact card design!")
        print("✓ Kept YOUR data: AIU CTF 2026, Curtin CTF, Integrated Hawkers")
        print("✓ Applied compact card layout from sample")
        print("\\nNow adding CSS styling...")
    else:
        print("Error: Could not find section end")
else:
    print("Error: Could not find CTF Achievements section")
