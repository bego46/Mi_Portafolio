document.addEventListener('DOMContentLoaded', function() {
    particlesJS('particles-js', {
        "particles": {
            "number": {
                "value": 80,
                "density": {
                    "enable": true,
                    "value_area": 800
                }
            },
            "color": {
                "value": "#0dcaf0"  // Azul neón
            },
            "shape": {
                "type": "char",
                "character": "><>/{}=+-*"  // Símbolos de código
            },
            "opacity": {
                "value": 0.5,
                "random": true
            },
            "size": {
                "value": 14,
                "random": true
            },
            "line_linked": {
                "enable": true,
                "distance": 150,
                "color": "#0dcaf0",
                "opacity": 0.3,
                "width": 1
            },
            "move": {
                "enable": true,
                "speed": 2,
                "direction": "none",
                "random": true,
                "straight": false,
                "out_mode": "out"
            }
        },
        "interactivity": {
            "events": {
                "onhover": {
                    "enable": true,
                    "mode": "repulse"
                }
            }
        }
    });
});