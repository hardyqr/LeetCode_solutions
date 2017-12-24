#!/bin/bash

for file in * ; do
	echo "${file}" "${file%%.*}.${file##*.}"
	mv "${file}" "${file%%.*}.${file##*.}"
done
