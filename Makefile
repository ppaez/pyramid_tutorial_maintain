
RST2HTML = rst2html

index.html: index.rst
	$(RST2HTML) $< $@
