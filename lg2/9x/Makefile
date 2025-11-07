all: \
	$(patsubst %.py,%.sqlite,$(wildcard *.py))

9-4x.sqlite: 9-4x.py 9x-corpus.txt.zst 9-2x.sqlite 9-3x.sqlite
	./$< >"9-4x.log"

%.sqlite: %.py 9x-corpus.txt.zst
	./$< >"$*.log"

clean:
	rm -fv *.sqlite *.log

.PHONY: all clean
