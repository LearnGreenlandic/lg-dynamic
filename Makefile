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
	rsync -avz lg2/1x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/1x/
	rsync -avz lg2/2x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/2x/
	rsync -avz lg2/3x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/3x/
	rsync -avz lg2/4x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/4x/
	rsync -avz lg2/5x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/5x/
	rsync -avz lg2/6x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/6x/
	rsync -avz lg2/7x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/7x/
	rsync -avz lg2/8x/*.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/8x/

release: all
	rsync -avz lg2/1x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/1x/
	rsync -avz lg2/2x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/2x/
	rsync -avz lg2/3x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/3x/
	rsync -avz lg2/4x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/4x/
	rsync -avz lg2/5x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/5x/
	rsync -avz lg2/6x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/6x/
	rsync -avz lg2/7x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/7x/
	rsync -avz lg2/8x/*.sqlite kal@learn.gl:public_html/online/d/lg2/sentence/8x/

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(CLEANDIRS)
.PHONY: all clean dev release
