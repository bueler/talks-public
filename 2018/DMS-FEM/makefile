all: talk.pdf

FIGURES=

TIKZ=

talk.pdf: talk.tex ${FIGURES} ${TIKZ}
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

