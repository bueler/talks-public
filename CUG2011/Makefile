all: talk.pdf

anim/g_csurf_frames_0.png:
	(cd anim/ && make)

talk.pdf: talk.tex anim/g_csurf_frames_0.png
	#rm -f figures
	#ln -s ../GGseminar2011/figures  # FIXME
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *.dvi

