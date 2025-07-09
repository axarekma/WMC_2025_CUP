        document.addEventListener('DOMContentLoaded', function () {
            const scoreElements = document.querySelectorAll('.score-hover[data-hover-image]');

            const hoverImg = document.createElement('img');
            hoverImg.className = 'hover-image';
            document.body.appendChild(hoverImg);

            scoreElements.forEach(element => {
                const hoverImageUrl = element.getAttribute('data-hover-image');

                element.addEventListener('mouseenter', () => {
                    hoverImg.src = hoverImageUrl;
                    hoverImg.style.opacity = '0.95';
                });

                element.addEventListener('mousemove', (e) => {
                    // Position relative to mouse
                    hoverImg.style.top = (e.clientY - 220) + 'px';
                    hoverImg.style.left = (e.clientX + 150) + 'px';
                });

                element.addEventListener('mouseleave', () => {
                    hoverImg.style.opacity = '0';
                });
            });
        });