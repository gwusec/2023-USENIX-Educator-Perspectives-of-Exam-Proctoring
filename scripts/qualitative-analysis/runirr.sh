#!/bin/bash

find ./data/ -iname "*primary*"| sort | while read f
do
    s=$(echo "$f" | sed s/primary/secondary/);
    name=$(echo "$f" | sed -n "s/^.* - \(.*\) .*/\1/p")
    irr=$(./irr.py "$f" "$s" | grep "irr:")
    
    echo "$name"
    echo -e "\t-- $irr"
done
