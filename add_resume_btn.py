import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# HTML for the resume button
resume_btn = '''
                    <!-- Resume Button -->
                    <div class="resume-container" style="margin-top: 1.5rem;">
                        <a href="assets/resume.pdf" download="MD_Parvej_Ahmed_Rafi_Resume.pdf" class="resume-btn">
                            <i class="fas fa-download"></i>
                            Download Resume
                        </a>
                    </div>'''

# Find the closing div of connect-icons and insert after it
# We look for the connect-icons div and its closing tag
pattern = r'(<div class="connect-icons">.*?</div>)'

if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, r'\1' + resume_btn, content, flags=re.DOTALL, count=1)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added resume button.")
else:
    print("Could not find connect-icons section.")
