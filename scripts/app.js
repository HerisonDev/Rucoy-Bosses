const menuButton = document.getElementById('menu-button');
const floatMenu = document.getElementById('float-menu');

const sectionHistory = document.getElementById('sec-history');

let historyContent = "";

menuButton.addEventListener('click', () => {
    // Toggle a classe 'hidden' para mostrar ou ocultar o menu
    floatMenu.classList.toggle('hidden');
});

// Função para ordenar os jogadores por pontos (descendente)
function ordenarPorPontos(a, b) {
    return b.pontos - a.pontos;
  }
  
  // Função para obter os 5 melhores jogadores
  function getTop5(jogadores) {
    return jogadores.sort(ordenarPorPontos).slice(0, 10);
  }
  
  // Exemplo de uso:
  const top5 = getTop5(jogadores);
  
  // Exibir o ranking (você pode personalizar a exibição)
  console.log("Ranking dos 5 melhores jogadores:");
  top5.forEach((jogador, index) => {
    console.log(`${index + 1}º lugar: ${jogador.nick} - ${jogador.pontos} pontos`);
  });
  
  // ... (seu código JavaScript anterior)
  
  // Função para calcular a soma total dos pontos
  function calcularSomaTotal(jogadores) {
    return jogadores.reduce((total, jogador) => total + jogador.pontos, 0);
  }
  
  // Calcular a soma total
  const somaTotal = calcularSomaTotal(jogadores);
  
  // Exibir o ranking com a soma total
  console.log("Ranking dos 5 melhores jogadores:");
  console.log("----------------------------------");
  top5.forEach((jogador, index) => {
    console.log(`${index + 1}º lugar: ${jogador.nick} - ${jogador.pontos} pontos`);
  });
  console.log("----------------------------------");
  console.log(`Soma total de pontos: ${somaTotal}`);


const rankingTable = document.getElementById('ranking');
top5.forEach((jogador, index) => {
    const row = rankingTable.insertRow();
    row.insertCell().textContent = index + 1;
    row.insertCell().textContent = jogador.nick;
    row.insertCell().textContent = jogador.pontos;
});

const totalRow = rankingTable.insertRow();
totalRow.insertCell().textContent = "Total: ";
totalRow.insertCell().colspan = "1";
totalRow.insertCell().textContent = `${somaTotal}`;
