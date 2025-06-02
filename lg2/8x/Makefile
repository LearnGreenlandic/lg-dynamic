all: \
	$(patsubst %.py,%.sqlite,$(wildcard *.py))

%.sqlite: %.py 8x-corpus.txt.zst
	./$< >"$*.log"

clean:
	rm -fv *.sqlite *.log

.PHONY: all clean
