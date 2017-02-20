#!/bin/bash

###############################################
#                                             #
#         run genMutModel on all TSVs         #
#                                             #
###############################################

# for each file ending in .tsv, run genMutModel with CDS only option to produce frequency matrices 
for file in *.tsv
do
	nohup python ~/neat-genreads/utilities/genMutModel.py -m $file -r ~/oicr/reference/HG19_WholeGenome.fa -co ./matrices/"$file".csv -o ./pickles/"$file".p -bi /shared/HG19_Data/nodecoys_hg19.bed -C BRCA_US --csv > ./logs/progress_"$file".nohup
	echo "$file processed."
done
