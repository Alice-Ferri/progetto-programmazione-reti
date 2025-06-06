# Realizzazione di un Web Server minimale in Python e pubblicazione di un sito statico

## Obiettivo del Progetto

Progettare un server HTTP in Python utilizzando il modulo `socket`, capace di gestire richieste `GET` e servire un sito statico con HTML/CSS. Il sito web realizzato rappresenta la "**Pizzeria da Michele**" e comprende cinque pagine informative dedicate alla storia, al menù, agli eventi settimanali e ai contatti della pizzeria. Queste sono collegate da un menu di navigazione responsive, oltre al link dell'header che porta alla home.

## Struttura del Progetto

* `server.py`: codice del server HTTP.
* `www/`: directory contenente il sito statico.

  * `index.html`: home page con la storia della pizzeria.
  * `menu.html`: lista delle pizze con immagini.
  * `eventi.html`: pagina con eventi.
  * `recensioni.html`: recensioni degli utenti.
  * `contatti.html`: contatti e informazioni.
  * `style.css`: stile condiviso.
  * `img/`: cartella immagini.
  
  ### Pagine Implementate

- **index.html** – _Homepage_  
  Racconta la storia della Pizzeria da Michele.

- **menu.html** – _Menù delle pizze_  
  Elenco dettagliato di pizze classiche e speciali con descrizione e prezzi, affiancato da relative immagini.

- **eventi.html** – _Eventi settimanali_  
  Presenta le iniziative settimanali come karaoke, musica dal vivo, quiz a premi, offerte “all you can eat”, compleanni.

- **recensioni.html** – _Recensioni degli utenti_  
  Presenta alcune delle testimonianze degli utenti.

- **contatti.html** – _Contatti e servizi_  
  Include indirizzo con link a maps, numero di telefono con link click-to-call, e informazioni sulle consegne a domicilio.


## Funzionamento del Server

Il server si avvia su `localhost` alla porta `8080` e gestisce richieste HTTP `GET`. Cerca il file richiesto nella directory `www/`.

#### Comportamenti previsti:
* Risponde con `200 OK` se il file esiste.
* Risponde con `404 Not Found` se il file non esiste.

## Funzionalità Implementate

* Gestione richieste HTTP `GET`
* Risposta 200 OK
* Risposta 404 Not Found
* 5 pagine HTML
* Layout responsive con menu hamburger
* Immagini servite correttamente
* Separazione HTML / CSS

## Estensioni Implementate

* Gestione dei MIME types (html, css, jpg, ecc.)
* Logging console delle richieste ricevute
* Animazioni e design responsive via CSS

## Conclusioni

Il progetto mostra il funzionamento di un server HTTP realizzato interamente in Python, sfruttando la libreria socket per la gestione delle connessioni.
È stato sviluppato un sito web statico completo, con HTML e CSS, ospitato sul server creato, offrendo così una panoramica sulle richieste HTTP.
