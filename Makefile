
RST2HTML = rst2html

README.html: README.rst
	$(RST2HTML) $< $@
