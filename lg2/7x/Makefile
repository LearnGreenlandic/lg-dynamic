all: \
	$(patsubst %.py,%.sqlite,$(wildcard *.py))

7-2x.sqlite: 7-2x.py 7x-corpus.txt.zst 7-1-1x.sqlite 7-1-2x.sqlite 7-1-3x.sqlite 7-1-4x.sqlite 7-1-5x.sqlite 7-1-6x.sqlite
	./$< >"7-2x.log"

%.sqlite: %.py 7x-corpus.txt.zst
	./$< >"$*.log"

clean:
	rm -fv *.sqlite *.log

.PHONY: all clean
