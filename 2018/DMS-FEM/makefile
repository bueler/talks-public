all: talk.pdf

TIKZFIGURES=

talk.pdf: talk.tex ${TIKZFIGURES}
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

