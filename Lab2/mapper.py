#!/usr/bin/env python

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    if line != "":
        try:
            obj = json.loads(line)
            text = obj["text"]
            # split the line into words
            words = text.split()
            # increase counters
            if "retweeted_status" not in obj:
                print "total\t1"
                for word in words:
                    # write the results to STDOUT (standard output);
                    # what we output here will be the input for the
                    # Reduce step, i.e. the input for reducer.py
                    #
                    # tab-delimited; the trivial word count is 1
                    word = word.lower()
                    if (word == "han") or (word == "hon") or (word == "den") or (word == "det") or (word == "denna") or (word == "denne") or (word == "hen"):
                        print '%s\t%s' % (word, 1)
        except:
            pass
