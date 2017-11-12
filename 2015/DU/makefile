all: talk.pdf

TIKZFIGURES=

talk.pdf: talk.tex ${TIKZFIGURES}
	(cd ../../old/commonfigs/ && rm -rf animhalfar/ && tar -xzvf animhalfar.tar.gz)
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

