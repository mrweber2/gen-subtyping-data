# gen-subtyping-data

This is the repository for generating cancer subtyping data

## format.sed

Formats header for output frequency matrices (output of genMutModel.py). Use with sed command.

```
sed -i -f format.sed file.csv
```

## genMutModel.py

Takes references genome and TSV file to generate mutation models. ***USE WITH neat-genreads REPO.

```
python genMutModel.py                                \
	-r hg19.fa                                   \
	-m inputVariants.tsv                         \
	--csv generate a mutation frequency matrix   \
	-co output.csv                               \
	-bi include_regions.bed                      \
	-be exclude_regions.bed                      \
	-o /home/me/models.p
```

Trinucleotides are identified in the reference genome and the variant file. Frequencies of each trinucleotide transition are calculated and output as a pickle (.p) file and matrix (.csv).

## run_genMut_subsampling.sh

Runs genMutModel.py on all TSVs/VCFs in current directory.

Needs to be edited for more general usage. Will update soon.

## sample_individuals.py

Parses out random 100 donors from population mutation file from ICGC

```
python sample_individuals.py                         \
	-m inputVariants.tsv                         
```

Needs to be edited for more general usage. Will update soon.

## To-Do
```
-improve useability of:
	1. run_genMut_subsampling.sh
	2. sample_individuals

-write visualization scripts

-keep up with documentation
```
