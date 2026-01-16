import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove .carousel-dots styles
# This is a bit tricky with regex for CSS blocks, but since we know the structure from previous edits
# We can try to remove specific blocks or just leave it as it doesn't harm anything.
# However, to be thorough, let's try to remove the block we added earlier.

# The block added earlier was:
# .hero-image .carousel-dots {
#     margin-top: 1rem;
# }

content = re.sub(r'\.hero-image \.carousel-dots\s*\{[^}]*\}', '', content)
content = re.sub(r'\.carousel-dots\s*\{[^}]*\}', '', content)
content = re.sub(r'\.dot\s*\{[^}]*\}', '', content)
content = re.sub(r'\.dot\.active\s*\{[^}]*\}', '', content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed carousel CSS styles.")
