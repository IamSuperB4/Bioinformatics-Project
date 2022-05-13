from __future__ import division
from fractions import Fraction
from nose.tools import assert_equal, assert_almost_equal
from dnds import dnds, pnps, substitutions, dnds_codon, dnds_codon_pair, syn_sum, translate

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

dipodomys1 = 'Genomes\Aligned\Dipodomys_D(1A) dopamine receptor_aligned.fna'

dipodomys1File = open(dipodomys1)

dipodomys1_parsed = parse_fasta_file(dipodomys1File, False)

dipodomys1List = [];

for key in dipodomys1_parsed:
    dipodomys1List.append(dipodomys1_parsed[key])

print(dnds(dipodomys1List[0], dipodomys1List[1]))