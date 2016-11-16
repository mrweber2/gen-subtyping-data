#!/usr/bin/python

#
#       Generate Features CSV for Weka
#       Matthew Weber
#       10/26/2016
#

import sys
import os
import re
import argparse
import numpy as np

#################################################
#       Open TSV for reading, CSV for writing   #
#################################################

parser = argparse.ArgumentParser(description='generate_FeatureCSV.py')
parser.add_argument('-m',  type=str,        required=True,   metavar='<str>',                    help="* mutations.tsv")
parser.add_argument('-I',                   required=False,  action='store_true', default=False, help="only indels")
parser.add_argument('-o',  type=str,        required=True,   metavar='<str>',                    help="* output.csv")
parser.add_argument('-c',  type=str,        required=True,   metavar='<str>',                    help="tumor site")
parser.add_argument('-F',                   required=False,  action='store_true', default=False, help="generate frequencies")
args = parser.parse_args()
(TSV, OnlyIND, OUT, SITE, FREQ) = (args.m, args.I, args.o, args.c, args.F)

SITE = str(SITE)

print 'reading input variants...'
f = open(TSV, 'r')
isFirst = True

o = open(OUT, 'w')
o.write('m_id,d_id,indel_length,source,cancer_type')
o.write('\n')
o.close()

o = open(OUT, 'a')

features = 5*[0]

for line in f:

	if line[0] == '#':
		continued

	if isFirst:
		splt = line.strip().split('\t')
		(m1,m2,m3) = (splt.index('reference_genome_allele'),splt.index('mutated_from_allele'),splt.index('mutated_to_allele'))
		(d_id, m_id, source, qscore, conseq) = (splt.index('icgc_donor_id'),splt.index('icgc_mutation_id'),splt.index('project_code'),splt.index('quality_score'),splt.index('consequence_type'))

		isFirst = False
		#exit(1)
		continue


	splt = line.strip().split('\t')

	[allele_ref,allele_normal,allele_tumor] = [splt[m1].upper(),splt[m2].upper(),splt[m3].upper()]
	mut     = splt[m_id]
	donor   = splt[d_id]
	code    = splt[source]

	if ('-' not in allele_normal and '-' not in allele_tumor) and (len(allele_normal) > 1 or len(allele_tumor) > 1):
		print 'skipping a complex variant...'
		continue


	if '-' in allele_normal:
		len_normal = 0
	else:
		len_normal = len(allele_normal)
	if '-' in allele_tumor:
		len_tumor = 0
	else:
		len_tumor = len(allele_tumor)

	if OnlyIND:

		if len_normal != len_tumor:
			indel_len = len_tumor - len_normal

			features[0] = mut
			features[1] = donor
			features[2] = indel_len
			features[3] = code
			features[4] = SITE
			for n in features:
				if n != SITE:
					o.write("%s," % n)
				else:
					o.write("%s" % n)
			o.write("\n")

		else:
			continue
		features = 5*[0]
	else:
		exit(1)

f.close()
o.close()


