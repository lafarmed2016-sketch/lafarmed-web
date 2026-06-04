document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide icons
  lucide.createIcons();

  // Intersection Observer for scroll animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Select all elements with the animate-fade-up class
  const animatedElements = document.querySelectorAll('.animate-fade-up');
  animatedElements.forEach(el => observer.observe(el));

  // Hero Background Slider
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length > 0) {
    let currentSlide = 0;
    
    setInterval(() => {
      // Remove active class from current slide
      slides[currentSlide].classList.remove('active');
      
      // Move to next slide, loop back to start if at end
      currentSlide = (currentSlide + 1) % slides.length;
      
      // Add active class to new slide
      slides[currentSlide].classList.add('active');
    }, 3000); // 3 seconds
  }
});
