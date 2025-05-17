/*
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: scripts.js
Fecha de inserción: 2025-05-17

Este archivo es parte del repositorio oficial de Developments Berlad y está
protegido por derechos de autor. No está permitida su copia, modificación
ni redistribución sin autorización expresa.

This file is part of the official Developments Berlad repository.
It is protected by copyright and may not be copied, modified, or distributed
without express permission.

ℹ️ Para más información, consulte el archivo README (disponible en varios idiomas).
ℹ️ For more information, see the README file (available in multiple languages).
------------------------------------------------------------------------------

*/

// Efecto de escritura en el título (opcional)
function typeWriter(elementId, text, speed = 100) {
    let i = 0;
    const element = document.getElementById(elementId);
    if (!element) return;

    element.innerHTML = '';
    
    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }
    }
    typing();
}

// Activar efecto al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    // Efecto de escritura (ejemplo para el título)
    const title = document.querySelector('.neon-logo');
    if (title) {
        typeWriter('dynamic-title', '{DB/}', 150);
    }

    // Efecto hover en tarjetas de proyectos
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 0 25px rgba(13, 202, 240, 0.5)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });

    // Botón de "Modo Oscuro" (opcional)
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode-active');
            localStorage.setItem('darkMode', document.body.classList.contains('dark-mode-active'));
        });

        // Cargar preferencia guardada
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark-mode-active');
        }
    }
});

console.log("🔥 Scripts.js cargado correctamente!");
document.addEventListener('DOMContentLoaded', function() {
    console.log("🚀 DOM listo!");
    particlesJS.load('particles-js', 'particles.json', function() {
        console.log("💻 Partículas inicializadas!");
    });
});