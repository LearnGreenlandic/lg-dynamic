#!/bin/bash
# Swap so analysis is before surface form, as analysis is the unique lookup key
# Delete all Der/* tags
# Delete all Gram/* tags, except Gram/Dem
# Sort and unique
perl -wpne 's/^([^:]+):(.+)$/$2\t$1/g; s@[+]Der/[^+]+@@g; s@Gram/Dem[+]@gram/dem+@g; s@[+]Gram/[^+]+@@g; s@gram/dem[+]@Gram/Dem+@g;' | LC_ALL=C sort | uniq
