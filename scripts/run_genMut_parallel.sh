#!/bin/bash

###########################################################
#                                                         #
#         run genMutModel in parallel on all VCFs         #
#                                                         #
###########################################################

# for each file ending in .tsv, run genMutModel with CDS only option to produce frequency matrices 
COUNTER=0

for file in *.vcf
do
	let COUNTER++
	if (( $COUNTER % 7 == 0 )) 
	then
		wait
	else
		nohup /usr/bin/python ~/neat-genreads/utilities/genMutModel.py -m $file -r ~/references/HG19_WholeGenome.fa -co ./matrices/"$file".csv -o ./pickles/"$file".p -bi ~/references/nodecoys_hg19.bed -C BRCA --csv > ./logs/progress_"$file".nohup &
		echo "$file processed."
		echo $COUNTER
	fi
done
