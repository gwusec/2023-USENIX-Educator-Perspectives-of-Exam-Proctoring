#!/usr/bin/env python3

import sys
import csv
import pprint
import textwrap


secondary_codes = True 


keys = []
def read_csv(fname):
    global keys
    l = []
    for row in  csv.reader(open(fname), delimiter=','):
        if not keys: 
            keys=row
            continue
        l.append(dict(zip(keys,row)))
    return l


if __name__ == "__main__":

    pri_f = sys.argv[1]
    sec_f = sys.argv[2]

    pri_l = read_csv(pri_f)
    sec_l = read_csv(sec_f)

    id_k = keys[0]
    q_k = keys[1]

    pri_d = {d[id_k]:d for d in read_csv(pri_f)[1:]}
    sec_d = {d[id_k]:d for d in read_csv(sec_f)[1:]}


    overlap = {}
    
    pri_used = {}
    sec_used = {}
    codes = ["Code 0","Code 1","Code 2","Code 3","Code 4","Code 5","Code 6","Code 7"]
    tot_pri = 0
    tot_sec = 0
    tot = 0
    for sk in sec_d:
        s = sec_d[sk]
        p = pri_d[s[id_k]] #get primary

#        print(s)
        sec_codes = set(s[c].strip() for c in codes if
                        c in s and s[c] != ''
                        and (not "->" in s[c] or secondary_codes)
        )
        
        pri_codes = set(p[c].strip() for c in codes if
                        c in p and p[c] != '' 
                        and (not "->" in p[c] or secondary_codes)
        )

#        print(pri_codes)
#        print(sec_codes)

        if any(sec_codes) and any(pri_codes):
            tot_sec += len(sec_codes)
            tot_pri += len(pri_codes)

            print(s[id_k])
            print(textwrap.indent(textwrap.fill('"'+s[q_k]+'"'),"\t"))
            print("pri_code:\t",pri_codes)
            print("sec_cod:\t",sec_codes)
            print()

            for c in sec_codes.intersection(pri_codes):
                overlap[c] = overlap.get(c,0)+1
                
            for sc in sec_codes:
                sec_used[sc] = sec_used.get(sc,0)+1

            for pc in pri_codes:
                pri_used[pc] = pri_used.get(pc,0)+1

    pri_used = {k:pri_used[k]/tot_pri for k in pri_used}
    sec_used = {k:sec_used[k]/tot_sec for k in sec_used}
    overlap = {k:overlap[k]/max(tot_pri,tot_sec) for k in overlap}

    for c in pri_used:
        if not c in overlap:
            overlap[c]=0.0
    
    for c in sec_used:
        if not c in overlap:
            overlap[c]=0.0

    print("Primary Coders Usage")
    pprint.pprint(pri_used)
    print()
    print("Secondary Coders Usage")
    pprint.pprint(sec_used)
    print()
    print("Overlapping Usage")
    pprint.pprint(overlap)

    print()
    p_a = sum(overlap.values())
    p_c = sum(pri_used.get(c,0.0)*sec_used.get(c,0.0) for c in set(pri_used.keys()).union(set(sec_used.keys())))
    
    #irr = p_a/(1-p_c)    
    irr = 1 - (1-p_a)/(1-p_c)

    print("p_a:",p_a)
    print("p_c:",p_c)
    print("irr:",irr)
    
