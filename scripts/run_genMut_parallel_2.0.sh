#!/bin/bash

###################################################################
#                                                                 #
#         run genMutModel in parallel on all VCFs or TSVs         #
#                                                                 #
###################################################################

# for each vcf or tsv, run genMutModel with CDS only option to produce frequency matrices 

# full path to the reference genome
PATH_TO_REF="/home/ubuntu/references/HG19_WholeGenome.fa"

# full path to variant file directory
PATH_TO_MUT="/home/ubuntu/icgc-downloads/snps/"

# full path to bed file, for targeting coding regions
PATH_TO_BED="/home/ubuntu/references/nodecoys_hg19.bed"

# tumor site
SITE="BRCA"

# specify the number of nodes to use
NUMBER_OF_NODES=6

# are these tsv or vcf files?
FILE_SUFFIX=".vcf"

# start counter
COUNTER=0


# for each vcf or tsv, run genMutModel with CDS only option to produce frequency matrices 
for file in *$FILE_SUFFIX
do
	let COUNTER++
	if (( $COUNTER % ($NUMBER_OF_NODES+1) == 0 )) 
	then
		wait
	else
		nohup /usr/bin/python ~/neat-genreads/utilities/genMutModel.py -m $file -r "$PATH_TO_REF" -co "$PATH_TO_MUT"/matrices/"$file".csv -o "$PATH_TO_MUT"/pickles/"$file".p -C "$SITE" --csv > "$PATH_TO_MUT"/logs/progress_"$file".nohup &
		echo "$file processed."
		echo $COUNTER
	fi
done
