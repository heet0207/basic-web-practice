// Smooth scrolling for navbar links
document.querySelectorAll('.menu li a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        target.scrollIntoView({ behavior: 'smooth' });
    });
});

// Simple contact form alert (simulate form submission)
document.getElementById('contactForm').addEventListener('submit', function(e){
    e.preventDefault();
    alert("Thank you " + document.getElementById('name').value + "! Your message has been sent.");
    this.reset();
});
