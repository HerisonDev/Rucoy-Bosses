const menuButton = document.getElementById('menu-button');
const floatMenu = document.getElementById('float-menu');

menuButton.addEventListener('click', () => {
    // Toggle a classe 'hidden' para mostrar ou ocultar o menu
    floatMenu.classList.toggle('hidden');
});
