let historyContent = "";
let limitedFound = "";

const sectionHistory = document.getElementById('sec-history');

const historyBoard = document.getElementById('sec-history');

//limitedFound = found.slice(0, 10);

for(let history of found){
  historyContent +=
  `
  <p><span class="time-span">${history.date} :</span> <a href="${history.charLink}" target="_blank">${history.nick}</a> found <span class="boss-name">${history.boss}</span> on ${history.server}.</p>
  `

}
historyBoard.innerHTML += historyContent;

