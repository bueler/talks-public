all: talk.pdf

TIKZFIGURES=

case_f0_psi1_oneD.png: code/genfig.py code/femcases.py
	(cd code/ && python femcases.py && mv case_f*psi*.png ../)

talk.pdf: talk.tex ${TIKZFIGURES} case_f0_psi1_oneD.png
	mogrify -trim +repage *.png
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~ .gitignore~ *.png code/*.pyc code/*~

