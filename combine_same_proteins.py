import os
import re

def find_nth(full_string, substring, n):
    start = full_string.find(substring)
    while start >= 0 and n > 1:
        start = full_string.find(substring, start+len(substring))
        n -= 1
    return start

def get_protein_name(line):
    open_bracket = find_nth(line, '[', 3)
    close_bracket = find_nth(line, ']', 3)

    return line[open_bracket+9:close_bracket] # Pick out substring and remove '[protein ='

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
fromDirectory = 'Genomes/AlignedDopamineGenesSameSizeSequences/' # put / at the end of string
intoDirectory = 'Genomes/CombineDopamineGeneFiles/' # put / at the end of string 

listOfFiles = []
listOfProteins = ["1A", "1B", "2", "3", "4"]
 
# iterate over files in  directory
for filename in os.listdir(fromDirectory):
    f = os.path.join(fromDirectory, filename) # entire path to file
    
    # check if it is a file
    if os.path.isfile(f):
        listOfFiles.append(f) # add file to list of files to parse


for protein in listOfProteins:
    for direct in listOfFiles:
        file = open(direct)
        fileName = os.path.basename(direct) # pull file name from path
        
        parsed_file = parse_fasta_file(file, False) # parse fasta file, convert to dictionary

        if protein in fileName and "isoform X2" not in fileName and "isoform X3" not in fileName:
            # loop through all genes in parsed fasta file
            for key in parsed_file:
                # pull information to create file name for species' gene
                protein_name = get_protein_name(key)
                genus_name = fileName.rsplit('_',2)[0]
                species_name = fileName.rsplit('_',2)[1]

                new_line = key.replace('lcl', '>lcl')
                new_file_name = genus_name + '_' + protein_name + ".fna"

                print('Creating File: ' + "Protein(" + protein + ") - from " + fileName)

                # Create (if file doesn't exist) or append file with gene pulled from file
                with open(intoDirectory + "Protein(" + protein + ")", 'a+') as newFile:
                    newFile.write(new_line + '\n')
                    newFile.write(parsed_file[key] + '\n')

                newFile.close()


print('\nDeleting files with only 1 gene - AKA only one species in that genus has that gene, not both\n')