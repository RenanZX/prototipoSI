window.onload = function(){
	var head = document.getElementById("header");
	if (head!= null){
		document.getElementById("header").innerHTML = '\
		\
		<title>Prototipo</title>\
		<link rel="stylesheet" type="text/css" href="css/estilo.css"/>\
		<link rel="stylesheet" href="css/circle.css">\
		\
		';
	}

	document.getElementById("pagina").innerHTML += '\
	\
	<h1 style="color:white;">Protótipo Transparência Política</h1>\
    	<nav>\
			<ul class="menu">\
				<li id="active"><a href="./principal.html" id="current">Home</a></li>\
				<li><a href="#">Metas</a>\
				<ul>\
					<li><a href="./Metas_governador.html">Metas do Governador</a></li>\
					<li><a href="#">Metas do Deputado Federal</a></li>\
					<li><a href="#">Metas do Senador</a></li>\
				</ul>\
				</li>\
				<li><a href="./Impostometro.html">Impostômetro</a></li>\
				<li><a href="./Politica.html">Política Brasília</a></li>\
			</ul>\
		</nav>\
		</br></br></br>\
		<p style="color:white;" id="dep-information">\
			Dados do político</br></br>\
			<img src="dados/Rollemberg.jpg"/></br>Nome do Partido</br>Dados do governador Atual</p>\
	\
	';
}