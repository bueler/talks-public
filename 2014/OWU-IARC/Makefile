all: talk.pdf

TIKZFIGURES=

#FIXME  FigS8_Thwaites_anim.gif  is from supplementary material on Rignot et al 2014
#anim/thwaitesframes0.png: anim/FigS8_Thwaites_anim.gif
#	(cd anim/ && convert FigS8_Thwaites_anim.gif thwaitesframes%d.png)

../commonfigs/animhalfar/halfar0.png: ../../old/commonfigs/animhalfar.tar.gz
	(cd ../commonfigs/ && rm -rf animhalfar/ && tar -xzvf animhalfar.tar.gz)

#talk.pdf: talk.tex ${TIKZFIGURES} anim/thwaitesframes0.png ../commonfigs/animhalfar/halfar0.png
talk.pdf: talk.tex ${TIKZFIGURES} ../../old/commonfigs/animhalfar/halfar0.png
	pdflatex talk
	pdflatex talk

.PHONY: clean

clean:
	@rm -f *.out *.aux *.log *.bbl *.blg *.snm *.toc *.nav *~

