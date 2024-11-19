all: \
	$(patsubst %.py,%.sqlite,$(wildcard *.py)) \
	$(patsubst %.py,%.log,$(wildcard *.py))

%.sqlite %.log: %.py 1x-corpus.txt
	./$< >"$*.log"

clean:
	rm -fv *.sqlite *.log

.PHONY: all clean
