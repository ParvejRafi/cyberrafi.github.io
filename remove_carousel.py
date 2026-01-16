import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to remove the carousel dots section
pattern = r'\s*<!-- Carousel Dots -->\s*<div class="carousel-dots">.*?</div>'

# Remove the section
new_content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully removed carousel dots section.")
