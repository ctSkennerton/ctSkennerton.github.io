#!/usr/bin/env python
import sys, os, glob, re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fixed_re = re.compile('fxtract-(\w+)_random_(10{2,5})_(\d\d)bp_patterns_times\.txt')
norm_re = re.compile('fxtract-(\w+)_random_(10{2,5})_patterns_minus_small_times\.txt')

times_files = glob.glob("./fxtract*times.txt")
data = {}
for fn in times_files:
    match = fixed_re.search(fn)
    if match:
        pass
    else:
        match = norm_re.search(fn)
        if match:
            pass
        else:
            raise ValueError("Filename %s does not fit either form" % fn)
    with open(fn) as fp:
        first_line = True
        for line in fp:
            if first_line:
                first_line = False
                continue
            fields = line.rstrip().split(',')
            try:
                
            