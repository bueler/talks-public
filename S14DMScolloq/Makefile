all: talk.pdf

FIGURES=case_f0_psi1_oneD.png calcprob_bare.png proj_xy.png

calcprob_bare.png: code/calcfigs.py
	(cd code/ && python calcfigs.py && mv calcprob_*.png ../)

case_f0_psi1_oneD.png: code/femgenfig.py code/femcases.py
	(cd code/ && python femcases.py && mv case_f*psi*.png ../)

proj_xy.png: code/abstractfigs.py
	(cd code/ && python abstractfigs.py && mv proj_xy*.png ../)

talk.pdf: talk.tex ${FIGURES}
	mogrify -trim +repage *.png
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.synctex.gz *~ .gitignore~ *.png code/*.pyc code/*~

