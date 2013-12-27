all: talkpnwnas12.pdf

TIKZFIGURES=

talkpnwnas12.pdf: talkpnwnas12.tex ${TIKZFIGURES}
	(cd ../commonfigs/ && rm -rf animhalfar/ && tar -xzvf animhalfar.tar.gz)
	pdflatex talkpnwnas12
	pdflatex talkpnwnas12

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *~

