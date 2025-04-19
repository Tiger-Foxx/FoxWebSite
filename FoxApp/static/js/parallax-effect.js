// Effet de parallaxe pour la landing page
document.addEventListener("DOMContentLoaded", function() {
    const hero = document.querySelector('._hero');
    const floatingElements = document.querySelectorAll('._floating_element');
    
    if (hero && floatingElements.length > 0) {
        hero.classList.add('has-parallax');
        
        document.addEventListener('mousemove', function(e) {
            const x = e.clientX / window.innerWidth;
            const y = e.clientY / window.innerHeight;
            
            floatingElements.forEach(element => {
                const speed = element.classList.contains('_element1') ? 20 :
                              element.classList.contains('_element2') ? 30 :
                              element.classList.contains('_element3') ? 15 : 25;
                
                const xOffset = (x - 0.5) * speed;
                const yOffset = (y - 0.5) * speed;
                
                element.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
            });
        });
    }
    
    // Observer pour les animations au défilement
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('_visible');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('._hero, ._hero *').forEach(el => {
        observer.observe(el);
    });
});