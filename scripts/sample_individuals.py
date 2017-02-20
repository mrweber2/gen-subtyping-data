#!/usr/bin/python

################################################################################################
#                                                                                              #
#                           Sample individual donors from ICGC TSVs                            #
#                           Matt Weber 2/17/2017                                               #
#                                                                                              #
################################################################################################

import argparse
import random

# set input options
parser = argparse.ArgumentParser(description='subsample.py')
parser.add_argument('-m',  type=str, required=True,  metavar='<str>',                  help="* mutations.tsv")
#parser.add_argument('-o',  type=str, required=True,  metavar='<str>',                  help="* output.tsv")
args = parser.parse_args()
(TSV) = (args.m)


# generate 955 integers, select 100 randomly
subset = random.sample(range(955), 100)

sample = []

################################################################################################
############################################  MAIN  ############################################
################################################################################################

def getLines():

	isFirst = True
	
	# convert donor name file to list
	IDs = open("/home/mrweber2/Cancer_Subtyping/pop_data/BRCA/ID.txt").readlines()

	for i in IDs:
		# if the index number of donor matches the random 100 numbers generated
		if IDs.index(i) in subset:
			# strip away newline character
			i = i.strip()
			# add donor ID to list
			sample.append(i)
	print sample


	# open tsv for reading, output file for writing
	with open(TSV, 'r') as input:
		for line in input:
			list = line.split('\t')
			if list[1] in sample:
				with open('BRCA_subsample1_{}.tsv'.format(list[1]), 'a') as output:
					output.write(line)

	input.close()
	output.close()

getLines()		
