#!/bin/bash

for file in *.csv
do
	echo "" >> $file
	sed '1d' $file > no_header_"$file"
	echo "$file processed."
done
