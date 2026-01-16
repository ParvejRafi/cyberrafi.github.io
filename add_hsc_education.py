#!/usr/bin/env python3
"""Script to add HSC education to the Education section"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# HSC education HTML to add
hsc_education = '''
                <!-- HSC Education -->
                <div class="timeline-item">
                    <div class="timeline-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <div class="timeline-content">
                        <h3>Higher Secondary Certificate (HSC)</h3>
                        <h4>BAF Shaheen College</h4>
                        <span class="timeline-date">2020 – 2022</span>
                        <p>GPA: 5.00 / 5.00</p>
                    </div>
                </div>'''

# Find the position to insert (after the first timeline-item closing div)
# Look for the end of the B.Sc. timeline-item
search_pattern = '''                    </div>
                </div>
            </div>
        </div>
    </section>'''

# Check if HSC is already added
if 'BAF Shaheen College' in content:
    print("✓ HSC education already exists in the file")
else:
    # Replace with the new content including HSC
    replacement = '''                    </div>
                </div>
''' + hsc_education + '''
            </div>
        </div>
    </section>'''
    
    if search_pattern in content:
        content = content.replace(search_pattern, replacement)
        
        # Write back to file
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✓ Successfully added HSC education to the Education section")
        print("  - Institution: BAF Shaheen College")
        print("  - Period: 2020 – 2022")
        print("  - GPA: 5.00 / 5.00")
    else:
        print("✗ Could not find the insertion point in the file")
