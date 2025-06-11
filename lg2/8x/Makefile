all: \
	$(patsubst %.py,%.sqlite,$(wildcard *.py))

8-1-9x.sqlite: 8-1-9x.py 8x-corpus.txt.zst 8-1-1x.sqlite 8-1-2x.sqlite 8-1-3x.sqlite 8-1-4x.sqlite 8-1-5x.sqlite 8-1-6x.sqlite 8-1-7x.sqlite 8-1-8x.sqlite
	./$< >"8-1-9x.log"

%.sqlite: %.py 8x-corpus.txt.zst
	./$< >"$*.log"

clean:
	rm -fv *.sqlite *.log

.PHONY: all clean
