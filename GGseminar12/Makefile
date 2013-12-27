all: ggsem.pdf

TIKZFIGURES=validation_flowchart.tikz

ggsem.pdf: ggsem.tex ${TIKZFIGURES}
	(cd ../commonfigs/ && rm -rf animhalfar/ && tar -xzvf animhalfar.tar.gz)
	pdflatex ggsem
	pdflatex ggsem

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

