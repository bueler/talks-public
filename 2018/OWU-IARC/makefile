all: talk.pdf

TIKZFIGURES=

../../old/commonfigs/animhalfar/halfar0.png: ../../old/commonfigs/animhalfar.tar.gz
	(cd ../../old/commonfigs/ && rm -rf animhalfar/ && tar -xzvf animhalfar.tar.gz)

talk.pdf: talk.tex ${TIKZFIGURES} ../../old/commonfigs/animhalfar/halfar0.png
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

