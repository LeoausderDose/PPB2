LaTeX-Template zum Erstellen einer Praktikumsauswertung
-------------------------------------------------------
(Wolfgang Schöpf, Januar 2013)


Dieses Paket enthält folgende Dateien, die Ordnerstruktur sollte beibehalten werden:

readme.txt:      diese Datei

Auswertung.tex:  Masterdatei zum Erstellen der Arbeit, welche folgende Dateien einliest:

                 Grundlagen.tex: Kapitel 2 der Arbeit
                 Aufbau.tex:     Kapitel 3 der Arbeit
                 Diskussion.tex: Kapitel 4 der Arbeit

Auswertung.bib:  Bibliotheksdatei, welche die Literaturzitate enthält

Auswertung.bst:  Stildatei, welche den verwendeten Zitierstil definiert

titel.eps:       Bild für die Titelseite

Auswertung.ps:   Postscriptausgabe des fertigen Dokumentes

Auswertung.pdf:  PDF-Ausgabe des fertigen Dokumentes

bilder:          Unterordner, welche folgende im Dokument verwendete Bilder enthält:
                 Fuss_Kernspin.eps
                 MM_MagnetischesMoment.eps
                 MM_Permanentmagnet.eps

Die Ausgaben wurden durch folgende Befehlsfolgen erstellt:
latex Auswertung
bibtex Auswertung
latex Auswertung
latex Auswertung
dvips Auswertung bzw. dvipdfm Auswertung

EDIT 20.09.2018:

Befehlsfolgen (als schnelles Übersetzen) für aktuelste Version von texmaker auf Windows 10:
	latex
	latex
	bibtex
	latex
	dvips
	ps2pdf


-um pdfs als Bilder einzubinden ---> Struktur für schnelles Übersetzen:
	pdflatex
	pdflatex
	bibtex
	pdflatex