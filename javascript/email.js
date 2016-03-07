//FUNZIONI DI CONVALIDA

//convalida il campo categoria nel fieldset categoria

function ValidateCategoria() {
	if(document.getElementById('tipoclprivato').checked)
		categoria = 'Privato';
	else if(document.getElementById('tipoclazienda').checked) {
		categoria = 'Azienda';
		nomeaz = document.getElementById('azienda').value;
		if(!nomeazienda) {
			document.getElementById('erroricateg').innerHTML = "Il campo NOME AZIENDA non &egrave; valido.";
			document.getElementById('azienda').focus();
			return false;
		}
	}
	else {
		document.getElementById('erroricateg').innerHTML = "Seleziona una CATEGORIA valida.";
		document.getElementById('tipoclprivato').focus();
		return false;
	}
	return true;
}

//convalida i campi obbligatori nel fieldset dati personali

function ValidateObbl(campo) {
	var inputcampo = campo.value;
	if(!inputcampo) {
		campo.focus();
		var campostring = campo.id.toUpperCase();
		document.getElementById('erroridatipers').innerHTML = "Il campo " + campostring + " non &egrave; valido.";
		return false;
	}
	return true;
}

//convalida il campo email obbligatorio nel fieldset dati personali

function ValidateEmail(campo) {
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(!campo.match(mailformat)) {
		document.getElementById('erroridatipers').innerHTML = "Il campo EMAIL non &egrave; valido.";
		document.getElementById('email').focus();
		return false;
	}
	return true;
}

//convalida i campi facoltativi nel fieldset dati personali

function ValidateFacolt(campo) {
	var inputcampo = campo.value;
	if(!inputcampo)
		return false;
	return true;
}

//include ed impagina gli eventuali campi dati facoltativi

function CreaFacoltativi() {
	var facolt = '';
	var campocitta = document.getElementById('citta');
	var citta = campocitta.value;
	if(ValidateFacolt(campocitta)) 
		facolt = facolt + "Citt\340: " + citta + "%0D%0A"; 
	/* nel mio programma email "à" viene visualizzata come "A tilde" */
	var campoindirizzo = document.getElementById('indirizzo');
	var indirizzo = campoindirizzo.value;
	if(ValidateFacolt(campoindirizzo)) 
		facolt = facolt  + "Indirizzo: " + indirizzo + "%0D%0A";
	var campotelefono = document.getElementById('telefono');
	var telefono = campotelefono.value;
	if(ValidateFacolt(campotelefono)) 
		facolt  = facolt + "Telefono: " + telefono + "%0D%0A";
	if(!facolt)
		return '';
	return facolt + "%0D%0A";
}

//convalida il campo tipologia nel fieldset messaggio

function ValidateTipologia() {
	if(document.getElementById('asstec').checked)
		tipologia = 'Assistenza Tecnica';
	else if(document.getElementById('difmalf').checked)
		tipologia = 'Difetto / Malfunzionamento';
	else if(document.getElementById('ricinfo').checked)
		tipologia = 'Richiesta Info';
	else if(document.getElementById('proplav').checked)
		tipologia = 'Proposta Lavorativa';
	else if(document.getElementById('altro').checked)
		tipologia = 'Altro';
	else {
		document.getElementById('erroritipo').innerHTML = "Seleziona la TIPOLOGIA del problema.";
		document.getElementById('asstec').focus();
		return false;
	}
	return true;
}

//convalida il campo messaggio nel fieldset messaggio

function ValidateMessaggio() {
	if(!messaggio) {
		document.getElementById('messaggio').focus();
		document.getElementById('errorimessaggio').innerHTML = "Scrivi un MESSAGGIO valido.";
		return false;
	}
	var l = messaggio.length;
	if(l < 10) {
		document.getElementById('messaggio').focus();
		document.getElementById('errorimessaggio').innerHTML = "Il MESSAGGIO &egrave; troppo breve.";
		return false;
	}
	return true;
}

//FUNZIONI AUSILIARIE

//cambia la visibilità del campo nome azienda in base allo stato del campo azienda

function Rivela() {
	if(document.getElementById('tipoclazienda').checked)
		document.getElementById('hiddenazienda').style.visibility = "visible";
	else {
		document.getElementById('hiddenazienda').style.visibility = "hidden";
		document.getElementById('azienda').value = "";
	}
}

//resetta i messaggi d'errore dopo aver premuto invia

function AzzeraErrori() {
	document.getElementById('erroricateg').innerHTML = "";
	document.getElementById('erroridatipers').innerHTML = "";
	document.getElementById('erroritipo').innerHTML = "";
	document.getElementById('errorimessaggio').innerHTML = "";
}

//FUNZIONE PRINCIPALE

//impagina (ed "invia") un'email controllando i vari campi richiesti e falcoltativi

function Email() {
	
	AzzeraErrori();
	
	//fieldset categoria
	
	nomeazienda = document.getElementById('azienda').value;
	if(!ValidateCategoria())
		return false;
	
	//fieldset dati personali (obbligatori)
	
	var camponome = document.getElementById('nome');
	var nome = camponome.value;
	if(!ValidateObbl(camponome))
		return false;
	var campocognome = document.getElementById('cognome');
	var cognome = campocognome.value;
	if(!ValidateObbl(campocognome))
		return false;
	
	var email = document.getElementById('email').value;	
	if(!ValidateEmail(email))
		return false;
	
	//fieldset dati personali (facoltativi)
	
	var facoltativi = CreaFacoltativi();
	
	//fieldset messaggio
	
	if(!ValidateTipologia())
		return false;
	
	messaggio = document.getElementById('messaggio').value; //var globale, serve a ValidateMessaggio()
	if(!ValidateMessaggio())
		return false;
	
	//impaginazione email
	
	var oggetto = tipologia + " - " + categoria;

	var obbligatori = "Nome: " + nome + "%0D%0A" + "Cognome: " + cognome + "%0D%0A"
	+ "Email: " + email + "%0D%0A";
	
	if(categoria == "Azienda")
		obbligatori = obbligatori + "Nome Azienda: " + nomeazienda + "%0D%0A";
	
	obbligatori = obbligatori + "%0D%0A" + messaggio;
	
	//"invio" email
	
	location.href = "mailto:contatti@imas.com" + "?Subject=" + oggetto 
	+ "&Body=" + facoltativi + obbligatori;
	
}