all: talk.pdf

TIKZFIGURES=

convexvar.png: code/convex2var.py
	(cd code/ && python convex2var.py && mv convexvar.png ../)

oned-basecase.png: code/onedtwoviews.py
	(cd code/ && python onedtwoviews.py && mv oned-basecase.png ../)

talk.pdf: talk.tex ${TIKZFIGURES} convexvar.png oned-basecase.png
	mogrify -trim +repage *.png
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~ *.png

