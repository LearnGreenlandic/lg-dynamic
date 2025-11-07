DIRS = \
	lg2/*/
CLEANDIRS = $(DIRS:%=clean-%)

all: $(DIRS)

$(DIRS):
	$(MAKE) -j2 -C $@

clean: $(CLEANDIRS)
$(CLEANDIRS):
	$(MAKE) -j2 -C $(@:clean-%=%) clean

dev: all
	./scripts/upload.sh online-dev

release: all
	./scripts/upload.sh online

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(CLEANDIRS)
.PHONY: all clean dev release
