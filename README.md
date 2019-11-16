# SteganographyInAction
Use processing to learn Steganography

In questo modulo lavoreremo sul concetto di steganografia. 
Nella cartella Code dovrai inserire un codice in ambiente processing che implementi i seguenti punti:
# Cartella CODE
- Prendere in input il file input.txt
- Costruire un'immagine formata da quadrati di lato 50 pixel. L'immagine sarà larga 10 quadrati.
- Ogni quadrato andrà colorato utilizzando tre caratteri prelevati dal file che costituiranno le componenti RBG del colore
- Se il numero dei caratteri non è multiplo di tre, utilizzare il valore 255 per le relative componenti
- Completare l'immagine con quadrati neri (RGB=0,0,0) in maniera da renderla rettangolare.
- Salvare l'immagine nel file Mistery.tiff

Nella cartella Decode dovrai inserire il codice in ambiente processing che implementi i seguenti punti:
# Cartella Decode
- Prendere in input il file Mistery.tiff
- L'immagine sarà formata da quadrati di lato 50 pixel. L'immagine sarà larga 10 quadrati.
- Prelevare un pixel da ogni quadrato.
- Per ogni pixel, estrarre le componenti RGB e calcolare il relativo codice ASCII
- Stampare a video il messaggio ottenuto.

Scadenza 30 novembre
