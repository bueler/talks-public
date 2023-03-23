# list the targets for which we run a script to generate
# (there are additional .png and .pdf figs which are *not* re-generated)
pdfroots := NPplane NPplanestatic NPplaneweakstrong

pdfgens := $(addsuffix .pdf, $(pdfroots))

all: $(pdfgens)

NPplane.pdf NPplanestatic.pdf NPplaneweakstrong.pdf: NPplane.py
	python3 NPplane.py
	pdfcrop NPplane.pdf NPplane.pdf
	pdfcrop NPplanestatic.pdf NPplanestatic.pdf
	pdfcrop NPplaneweakstrong.pdf NPplaneweakstrong.pdf

.PHONY: clean

clean:
	@rm -f $(pdfgens)
	@rm -f *.pyc

