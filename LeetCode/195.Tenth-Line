#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.
for x in $(wc -l file.txt); do
    if [ "$x" -ge "10" ] ; then
        head -n 10 file.txt | tail -n 1
    fi
    break
done
