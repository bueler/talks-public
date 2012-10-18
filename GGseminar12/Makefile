all: ggsem.pdf

# to make this stuff work, do
#   $ cd ~/karthaus
#   $ make
#   $ cd ~/talks-public/GGseminar12/
#   $ ln -s ~/karthaus/anim/

TIKZFIGURES=validation_flowchart.tikz

ggsem.pdf: ggsem.tex ${TIKZFIGURES}
	pdflatex ggsem
	pdflatex ggsem

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

