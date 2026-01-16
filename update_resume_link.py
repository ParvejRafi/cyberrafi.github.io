import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the resume button link
# We want to replace href="assets/resume.pdf" and the download attribute
pattern = r'href="assets/resume\.pdf"\s+download="[^"]*"'
replacement = 'href="assets/PARVEJ_RAFI_RESUME.pdf" download="PARVEJ_RAFI_RESUME.pdf"'

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated resume link.")
else:
    print("Could not find resume link to update.")
    # Debug: print the area where we expect it
    match = re.search(r'class="resume-btn"', content)
    if match:
        start = max(0, match.start() - 100)
        end = min(len(content), match.end() + 100)
        print(f"Context around resume-btn:\n{content[start:end]}")
