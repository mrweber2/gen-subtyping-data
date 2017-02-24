#!/bin/bash

###############################################
#                                             #
#         run genMutModel on all VCFs         #
#                                             #
###############################################

# for each file ending in .tsv, run genMutModel with CDS only option to produce frequency matrices 
for file in *.vcf
do
	nohup /usr/bin/python ~/neat-genreads/utilities/genMutModel.py -m $file -r ~/references/HG19_WholeGenome.fa -co ./matrices/"$file".csv -o ./pickles/"$file".p -bi ~/references/nodecoys_hg19.bed -C BRCA --csv > ./logs/progress_"$file".nohup
	echo "$file processed."
done
