all:
	jupyter nbconvert *.ipynb --to markdown
	rm -fr *_files
	python3 normalize.py
