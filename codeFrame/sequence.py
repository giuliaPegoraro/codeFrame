from Bio import SeqIO
import pandas as pd
import os, sys

doc = sys.argv[1]  
xls = pd.ExcelFile(doc) #file contains the names of the organisms 
df = xls.parse("orthologuesLeaderless") #name of the sheet in the excel file
cols = list(df.columns.values)
error = 0

def get_feature_location(features, id, tags=["locus_tag", "old_locus_tag"]):
    """ return the start location of the definied gene from the genome"""
    for f in features:
        for key in tags:
            #tag may not be present in this feature
            for x in f.qualifiers.get(key, []):
                if x == id:		
                     return f.location
    return None

for j in range(len(cols)):
	col = cols[j]
	orgn = " ".join(col.split('_')[1].split(" ")[0:2]) #retrieve the name of the organism

	f = open(col+".fasta", "w+")
	
	#print orgn 
	for i in range(int(col.split(" ")[2])):
		genbank = SeqIO.read(""+orgn+".genbank", "genbank")
		genome = SeqIO.read(""+orgn+".fasta", "fasta")

		#print i, counter check
		locus_tag = df[col][i]

		location = get_feature_location(genbank.features, locus_tag)
		if not location:
			""" some genes are not found because they are annotated with "RS" in their"""
			locus_tag = locus_tag.split("_")[0]+"_RS"+locus_tag.split("_")[1]
			location = get_feature_location(genbank.features, locus_tag)
			if not location:
				error = error +1
				break
		f.write( ">"+locus_tag +" "+ orgn +"\r\n")
		f.write(str(genome.seq[location.start:location.start+50])+"\r\n")

print("Skipped"+str(error)) #print number of skipped genes
		
