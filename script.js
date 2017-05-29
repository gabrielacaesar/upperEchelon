//aqui começa o hamburger menu 
var botaoMenuHamburguer = document.querySelector("#hamburgerMenu");

function abrirMenu() {
	this.classList.toggle("clicked");
	var menu = document.querySelector("#hamburgerList");
	menu.classList.toggle("visible");
}

botaoMenuHamburguer.onclick = abrirMenu;
