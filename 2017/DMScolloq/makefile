all: talk.pdf

talk.pdf: talk.tex
	(cd figs/ && make)
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *.vrb *~
	(cd figs/ && make clean)

