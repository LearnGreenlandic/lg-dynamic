#!/bin/bash
for X in 1x 2x 3x 4x 5x 6x 7x 8x 9x; do
	if [ -d "lg2/$X" ]; then
		rsync -avz lg2/$X/*.sqlite kal@learn.gl:public_html/$1/d/lg2/sentence/$X/
	fi
	if [ -d "lg3/$X" ]; then
		rsync -avz lg3/$X/*.sqlite kal@learn.gl:public_html/$1/d/lg3/sentence/$X/
	fi
done
