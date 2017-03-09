#!/usr/bin/python


############################################
#                                          #
#        Retrieve donor clinical           #
#       data for further analysis          #
#                                          #
#          Author: Matt Weber              #
#          Date: 03/09/17                  #
#                                          #
############################################

import os
import sys
import argparse
import time

parser = argparse.ArgumentParser(description='retrieve_donor_data.py')
parser.add_argument('-i',            type=str, required=True,  metavar='<str>',                help="* mutation_matrix.csv")
parser.add_argument('-d',            type=str, required=True,  metavar='<str>',                help="* donor_data.tsv")
args = parser.parse_args()
(CSV,D_DATA) = (args.i,args.d)


#############  Read in mutation matrix and donor data  ###############

print 'reading input mutation frequency dataset...'
m = open(CSV,'r')
C_isFirst = True
time.sleep(3)

print 'reading input donor clinical data file(s)...'
d = open(D_DATA,'r')
D_isFirst = True
