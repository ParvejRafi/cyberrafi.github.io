#!/usr/bin/env python3
"""Script to add carousel JavaScript functionality"""

# JavaScript code for carousel
carousel_js = '''
// Profile Image Carousel
document.addEventListener('DOMContentLoaded', function() {
    const dots = document.querySelectorAll('.carousel-dots .dot');
    const profileImg = document.getElementById('profileImg');
    
    // Array of profile images (you can add more images here)
    const images = [
        'assets/profile.jpg',
        'assets/profile2.jpg',
        'assets/profile3.jpg',
        'assets/profile4.jpg',
        'assets/profile5.jpg',
        'assets/profile6.jpg',
        'assets/profile7.jpg',
        'assets/profile8.jpg'
    ];
    
    let currentSlide = 0;
    
    // Function to change image
    function changeImage(index) {
        if (profileImg && images[index]) {
            // Add fade effect
            profileImg.style.opacity = '0';
            
            setTimeout(() => {
                profileImg.src = images[index];
                profileImg.style.opacity = '1';
            }, 300);
            
            // Update active dot
            dots.forEach(dot => dot.classList.remove('active'));
            if (dots[index]) {
                dots[index].classList.add('active');
            }
            
            currentSlide = index;
        }
    }
    
    // Add click event to dots
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            changeImage(index);
        });
    });
    
    // Auto-rotate carousel every 5 seconds
    setInterval(() => {
        currentSlide = (currentSlide + 1) % images.length;
        changeImage(currentSlide);
    }, 5000);
    
    // Add smooth transition to profile image
    if (profileImg) {
        profileImg.style.transition = 'opacity 0.3s ease, transform 0.5s ease';
    }
});
'''

# Read the current script.js file
try:
    with open('script.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
except FileNotFoundError:
    js_content = ''

# Check if carousel code already exists
if 'Profile Image Carousel' in js_content:
    print("✓ Carousel JavaScript already exists")
else:
    # Append the carousel code
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write('\n' + carousel_js)
    
    print("✓ Successfully added carousel JavaScript")
    print("  - Auto-rotate every 5 seconds")
    print("  - Click dots to change image")
    print("  - Smooth fade transitions")
    print("  - Supports up to 8 profile images")
