#!/bin/bash
find * -name '*.py' -executable | xargs -n1 -IX bash -c './X >/dev/null'
rsync -avz lg2/2*x.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/2x/
