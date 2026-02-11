// Hide empty sidebar badges (badges with only whitespace)
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('nav a span.min-w-\\[18px\\]').forEach(function(badge) {
        if (badge.textContent.trim() === '') {
            badge.style.display = 'none';
        }
    });
});
