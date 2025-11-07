#!/bin/bash
for X in 1x 2x 3x 4x 5x 6x 7x 8x 9x; do
	rsync -avz lg2/$X/*.sqlite kal@learn.gl:public_html/$1/d/lg2/sentence/$X/
done
