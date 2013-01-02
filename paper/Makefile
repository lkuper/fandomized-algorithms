NAME=fandomized

$(NAME).pdf: $(NAME).tex $(NAME).bib
	pdflatex $(NAME)
	bibtex $(NAME)
	pdflatex $(NAME)
	pdflatex $(NAME)

clean:
	rm -f *.bbl *.blg *.out *.aux *.log *.Rout .RData $(NAME).pdf
