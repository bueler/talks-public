all: talkDMS11.pdf

TIKZFIGURES=glacier-jump-conditions.tikz phase-change.tikz pillbox.tikz

talkDMS11.pdf: talkDMS11.tex ${TIKZFIGURES}
	pdflatex talkDMS11
	pdflatex talkDMS11

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *~

