let historyContent = "";
let limitedFound = "";
const menuButton = document.getElementById('menu-button');
const floatMenu = document.getElementById('float-menu');

const sectionHistory = document.getElementById('sec-history');

const historyBoard = document.getElementById('sec-history');

menuButton.addEventListener('click', () => {
    // Toggle a classe 'hidden' para mostrar ou ocultar o menu
    floatMenu.classList.toggle('hidden');
});


//limitedFound = found.slice(0, 10);

for (let history of found) {
    historyContent +=
        `
  <p><span class="time-span">${history.date} :</span> <a href="${history.charLink}" target="_blank">${history.nick}</a> found <span class="boss-name">${history.boss}</span> on ${history.server}.</p>
  `

}
historyBoard.innerHTML += historyContent;

