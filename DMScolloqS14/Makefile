all: talk.pdf

TIKZFIGURES=

convexvar.png: code/convex2var.py
	(cd code/ && python convex2var.py && mv convexvar.png ../)

talk.pdf: talk.tex ${TIKZFIGURES} convexvar.png
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~

