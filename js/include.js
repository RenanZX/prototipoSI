window.onload = function(){
	var head = document.getElementById("header");
	if (head!= null){
		document.getElementById("header").innerHTML = '\
		\
		<title>Prototipo</title>\
		<link rel="stylesheet" type="text/css" href="css/estilo.css"/>\
		<link rel="stylesheet" href="css/circle.css">\
		<meta name="viewport" content="width=device-width, initial-scale=1">\
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\
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

	function move(id,limit) {
  		var elem = document.getElementById(id);   
  		var width = 0;
  		var id = setInterval(frame, 40);
  		function frame() {
    		if (width >= limit) {
      			clearInterval(id);
    		} else {
      			width++; 
     			elem.style.width = width + '%'; 
     			elem.innerHTML = width * 1  + '%';
    		}
  		}
	}

	for(var i=0;i<100;i++){
		move(i+"p",i);
	}

}