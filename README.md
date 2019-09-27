# codeFrame

codeFrame includes sequence, a python script, which has the aim to retrieve the first 50 nucleotides of a list of genes.

## General info 

The input file is an excel file containing the list of genes. <br />
In the fasta file is present the genome of the organism. <br />
In the genbank file includes information regarding the genes including the start position that is the information that I used. <br />
The code is generalized to work with the genbank file of different organisms. <br />
The output file is a fasta file containing the sequences of 50 nt of the genes. <br />

## Technologies

Implemented for Ubuntu
The version of Python used is 2.7

## Launch

Example execution: <br />
python sequence.py leaderlessNotOrthologues.xlsx 

## Libraries

'''Python
from Bio import SeqIO
import pandas as pd
import os, sys
'''



