// Smooth scroll navigation
document.addEventListener('DOMContentLoaded', function() {
    // Get all navigation links
    const navLinks = document.querySelectorAll('.main-nav a');
    
    // Add click event to each link
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get the target section
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                e.preventDefault();
                const targetSection = document.querySelector(targetId);
                
                if (targetSection) {
                    // Smooth scroll to section
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // Update active nav on scroll
    const sections = document.querySelectorAll('.section');
    
    window.addEventListener('scroll', function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (pageYOffset >= sectionTop - 100) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });
    
    // Animate stats on scroll
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'all 0.6s ease-out';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe stat cards
    document.querySelectorAll('.stat-card').forEach(card => {
        observer.observe(card);
    });
    
    // Observe feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        observer.observe(card);
    });
    
    // Add page load animation
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
    
    // Console welcome message
    console.log('%c🌍 Global Disaster Response Analysis Dashboard', 'color: #0EA5E9; font-size: 20px; font-weight: bold;');
    console.log('%cProject by Shraddha Khandelwal', 'color: #14B8A6; font-size: 14px;');
    console.log('%cGitHub: https://github.com/shraddhakhandelwal/Global-Disaster-Response-Data-Generator-2018-2024-', 'color: #666; font-size: 12px;');
});

// Add fade-in on page load
document.body.style.opacity = '0';
document.body.style.transition = 'opacity 0.5s ease-in';

// Interactive checklist
document.addEventListener('click', function(e) {
    if (e.target.matches('.checklist li')) {
        e.target.style.textDecoration = e.target.style.textDecoration === 'line-through' ? 'none' : 'line-through';
        e.target.style.opacity = e.target.style.opacity === '0.5' ? '1' : '0.5';
        e.target.innerHTML = e.target.innerHTML.includes('☐') 
            ? e.target.innerHTML.replace('☐', '☑') 
            : e.target.innerHTML.replace('☑', '☐');
    }
});

// Add copy functionality for file paths
document.querySelectorAll('.file-list a').forEach(link => {
    link.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        const fileName = this.textContent;
        navigator.clipboard.writeText(fileName).then(() => {
            const originalText = this.textContent;
            this.textContent = '✓ Copied!';
            setTimeout(() => {
                this.textContent = originalText;
            }, 1000);
        });
    });
});

// Add keyboard navigation
document.addEventListener('keydown', function(e) {
    const sections = Array.from(document.querySelectorAll('.section'));
    const currentSection = sections.find(section => {
        const rect = section.getBoundingClientRect();
        return rect.top >= 0 && rect.top <= window.innerHeight / 2;
    });
    
    if (!currentSection) return;
    
    const currentIndex = sections.indexOf(currentSection);
    
    // Arrow Down - Next section
    if (e.key === 'ArrowDown' && e.ctrlKey) {
        e.preventDefault();
        if (currentIndex < sections.length - 1) {
            sections[currentIndex + 1].scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Arrow Up - Previous section
    if (e.key === 'ArrowUp' && e.ctrlKey) {
        e.preventDefault();
        if (currentIndex > 0) {
            sections[currentIndex - 1].scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Home - Scroll to top
    if (e.key === 'Home' && e.ctrlKey) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
});

// Add print functionality
function printPage() {
    window.print();
}

// Export stats as JSON (for developers)
function exportStats() {
    const stats = {
        totalDisasters: 500,
        countries: 50,
        casualties: 2702569,
        economicLoss: 206261730000,
        aidDistributed: 153777890000,
        timePeriod: '2018-2024'
    };
    
    const dataStr = JSON.stringify(stats, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = 'disaster_stats.json';
    link.click();
}

// Make functions available globally
window.printPage = printPage;
window.exportStats = exportStats;
