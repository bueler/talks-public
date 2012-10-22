all: ggsem.pdf

TIKZFIGURES=validation_flowchart.tikz

ggsem.pdf: ggsem.tex ${TIKZFIGURES}
	pdflatex ggsem
	pdflatex ggsem

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

