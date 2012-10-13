all: talkpnwnas12.pdf

TIKZFIGURES=

talkpnwnas12.pdf: talkpnwnas12.tex ${TIKZFIGURES}
	pdflatex talkpnwnas12
	pdflatex talkpnwnas12

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *~

