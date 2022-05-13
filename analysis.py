from __future__ import division
from fractions import Fraction
from nose.tools import assert_equal, assert_almost_equal
from dnds import dnds, pnps, substitutions, dnds_codon, dnds_codon_pair, syn_sum, translate
import os



def parse_fasta_file(file, removeGaps):
    """Return a dict of {id:gene_seq} pairs based on the sequences in the input FASTA file
    input_file -- a file handle for an input fasta file
    removeGaps -- boolean to determine whether to remove "-" gaps in sequences
    """
    parsed_seqs = {}
    curr_seq_id = None
    curr_seq = []

    for line in file:
        line = line.strip()

        if line.startswith(">"):
            if curr_seq_id is not None:
                parsed_seqs[curr_seq_id] = ''.join(curr_seq)

            curr_seq_id = line[1:]
            curr_seq = []
            continue
        else:
            if(removeGaps):
                line = line.replace("-", "")

        curr_seq.append(line)

    #Add the final sequence to the dict
    parsed_seqs[curr_seq_id] = ''.join(curr_seq)
    return parsed_seqs


# assign directory
directory = 'Genomes\Aligned'

listOfFiles = []
 
# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        listOfFiles.append(f)




#dipodomys1 = 'Genomes\Aligned\Dipodomys_D(1A) dopamine receptor_aligned.fna'

for direct in listOfFiles:
    file = open(direct)
    fileName = os.path.basename(direct)
    
    parsed_file = parse_fasta_file(file, False)

    parsed_file_List = []

    for key in parsed_file:
        parsed_file_List.append(parsed_file[key])


    i = 0
    j = 0
    for f1 in parsed_file_List:
        for  f2 in parsed_file_List:
            if (("-" not in f1) and ("-" not in f2)) and i != j:
                #print(parsed_file_List[0] + "\n" + parsed_file_List[1] + "\n\n\n")
                print(fileName, "\n", round((dnds(f1, f2)), 3))
                
            j += 1
        i += 1