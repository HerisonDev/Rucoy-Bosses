let historyContent = "";
let limitedFound = "";

const historyBoard = document.getElementById('sec-history');

limitedFound = found.slice(0, 5);

for(let history of limitedFound){
  historyContent +=
  `
  <p><span class="time-span">${history.date} :</span> <a href="${history.charLink}" target="_blank">${history.nick}</a> found <span class="boss-name">${history.boss}</span> on ${history.server}.</p>
  `


historyBoard.innerHTML += historyContent;
}
