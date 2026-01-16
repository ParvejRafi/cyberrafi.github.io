# Update TryHackMe and PicoCTF logos to use actual images
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace TryHackMe logo
tryhackme_old = '''<div class="platform-logo">
                            <i class="fas fa-shield-alt" style="color: #00D26A;"></i>
                        </div>
                        <h4 class="platform-name">TryHackMe</h4>'''

tryhackme_new = '''<div class="platform-logo">
                            <img src="https://tryhackme.com/img/favicon.png" alt="TryHackMe" class="platform-logo-img">
                        </div>
                        <h4 class="platform-name">TryHackMe</h4>'''

# Find and replace PicoCTF logo
picoctf_old = '''<div class="platform-logo">
                            <i class="fas fa-flag-checkered" style="color: #E74C3C;"></i>
                        </div>
                        <h4 class="platform-name">PicoCTF</h4>'''

picoctf_new = '''<div class="platform-logo">
                            <img src="https://picoctf.org/img/logos/picoctf-logo-horizontal-white.svg" alt="PicoCTF" class="platform-logo-img">
                        </div>
                        <h4 class="platform-name">picoCTF</h4>'''

# Replace the logos
content = content.replace(tryhackme_old, tryhackme_new)
content = content.replace(picoctf_old, picoctf_new)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ TryHackMe logo updated to official favicon")
print("✓ PicoCTF logo updated to official logo")
print("\\nNow adding CSS for logo images...")
