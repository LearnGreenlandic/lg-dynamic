DIRS = \
	lg2/2-1x \
	lg2/2-2x
CLEANDIRS = $(DIRS:%=clean-%)

all: $(DIRS)

$(DIRS):
	$(MAKE) -j -C $@

clean: $(CLEANDIRS)
$(CLEANDIRS):
	$(MAKE) -j -C $(@:clean-%=%) clean

dev: all
	rsync -avz lg2/*/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/2x/

release: all
	rsync -avz lg2/*/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/2x/

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(CLEANDIRS)
.PHONY: all clean dev release
