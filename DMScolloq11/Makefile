all: talk.pdf

TIKZFIGURES=glacier-jump-conditions.tikz phase-change.tikz pillbox.tikz

talk.pdf: talk.tex ${TIKZFIGURES}
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *~

