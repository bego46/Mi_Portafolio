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

document.addEventListener('DOMContentLoaded', function() {
    console.log("🚀 DOM listo!");

    // 💡 Efecto de escritura en el título
    const titleElement = document.getElementById('dynamic-title');
    if (titleElement) {
        typeWriter(titleElement, "{DB/}", 150);
    }

    // 🎨 Hover en tarjetas de proyectos
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px)';
            card.style.boxShadow = '0 0 25px rgba(13, 202, 240, 0.5)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
            card.style.boxShadow = '';
        });
    });

    // 🌙 Modo Oscuro con `localStorage`
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode-active');
            localStorage.setItem('darkMode', document.body.classList.contains('dark-mode-active'));
        });

        // Aplicar preferencia guardada
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark-mode-active');
        }
    }

    // 📷 Lightbox para imágenes
    const modal = document.getElementById("image-modal");
    const modalImg = document.getElementById("modal-img");
    const closeModal = document.querySelector(".close-modal");
    
    document.querySelectorAll(".card-img-top").forEach(img => {
        img.addEventListener("click", function() {
            modal.style.display = "flex";
            modalImg.src = this.src;
            modalImg.style.maxWidth = "90%";
            modalImg.style.maxHeight = "90%";
        });
    });

    // ❌ Cerrar el modal correctamente
    closeModal.addEventListener("click", function() {
        modal.style.display = "none";
    });

    modal.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
