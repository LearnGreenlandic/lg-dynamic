all: \
	$(patsubst %.py,%.sqlite,$(wildcard *.py)) \
	$(patsubst %.py,%.log,$(wildcard *.py))

%.sqlite %.log: %.py 2x-corpus.txt.zst
	./$< >"$*.log"

clean:
	rm -fv *.sqlite *.log

.PHONY: all clean
