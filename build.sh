#!/bin/bash
DIR=$(cd $(dirname $0);pwd)
cd "$DIR"

ls -1 lg2/*.py | xargs -n1 -IX bash -c 'echo X; ./X >/dev/null'
rsync -avz lg2/2*x.sqlite kal@learn.gl:public_html/online-dev/d/lg2/sentence/2x/
