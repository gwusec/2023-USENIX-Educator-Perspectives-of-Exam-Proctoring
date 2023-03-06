#!/bin/bash

pushd ../../data/qualitative-data
find irr_inputs/ -iname "*primary*"| sort | while read f
do
    s=$(echo "$f" | sed s/primary/secondary/);
    name=$(echo "$f" | sed -n "s/^.* - \(.*\) .*/\1/p")
    irr=$(../../scripts/qualitative-analysis/irr.py "$f" "$s" | grep "irr:")
    
    echo "$name"
    echo -e "\t-- $irr"
done
popd

