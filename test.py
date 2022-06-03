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
fromDirectory = 'Genomes\DopamineGenes\Camelus_D(2) dopamine receptor isoform X2.fna'

file = open(fromDirectory)
fileName = os.path.basename(fromDirectory)

parsed_file = parse_fasta_file(file, False)
file.close()

newFileString = ""

for key in parsed_file:
    new_line = key.replace('lcl', '>lcl')
    newFileString += new_line + '\n' + parsed_file[key]

print(newFileString)

'''
with open(file, 'a+') as newFile:
    newFile.write(new_line + '\n')
    newFile.write(parsed_file[key] + '\n')
'''