//aqui começa o hamburger menu 
var botaoMenuHamburguer = document.querySelector("#hamburgerMenu");

function abrirMenu() {
	this.classList.toggle("clicked");
	var menu = document.querySelector("#hamburgerList");
	menu.classList.toggle("visible");
}

botaoMenuHamburguer.onclick = abrirMenu;

//aqui começa o background durante o hamburger menu
var cover = document.querySelector(".cover");

botaoMenuHamburguer.addEventListener('click',function() {
    cover.classList.toggle("toggleCover");
});
