# gen-subtyping-data

This is the repository for generating cancer subtyping data

## generate_indelCSV

Usage: python generate_indelCSV.py -m mutations.tsv -c cancer_type -o output.csv

Option: -I specify only insertions and deletions

Produces a CSV containing donor ID, mutation ID, indel length, and tumor site information.

