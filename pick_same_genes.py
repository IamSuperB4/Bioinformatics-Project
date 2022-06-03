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
type_of_gene = "dopamine receptor"

fromDirectory = 'Genomes/Genes'
intoDirectory = 'Genomes/DopamineGenes/'

listOfFiles = []
 
# iterate over files in  directory
for filename in os.listdir(fromDirectory):
    f = os.path.join(fromDirectory, filename) # entire path to file
    
    # check if it is a file
    if os.path.isfile(f):
        listOfFiles.append(f) # add file to list of files to parse

for direct in listOfFiles:
    file = open(direct)
    fileName = os.path.basename(direct) # pull file name from path
    
    parsed_file = parse_fasta_file(file, False) # parse fasta file, convert to dictionary

    # loop through all genes in parsed fasta file
    for key in parsed_file:
        # only look at the gene we want to research
        if(type_of_gene in key):
            # pull information to create file name for species' gene
            protein_name = get_protein_name(key)
            genus_name = fileName.rsplit('_',2)[0]
            species_name = fileName.rsplit('_',2)[1]

            new_line = key.replace('lcl', '>lcl_' + species_name)
            new_file_name = genus_name + '_' + protein_name + ".fna"

            print('Creating File: ' + new_file_name)

            # Create (if file doesn't exist) or append file with gene pulled from file
            with open(intoDirectory + new_file_name, 'a+') as newFile:
                newFile.write(new_line + '\n')
                newFile.write(parsed_file[key] + '\n')

            newFile.close()


print('\nDeleting files with only 1 gene - AKA only one species in that genus has that gene, not both\n')


listOfFiles = []
 
# iterate over files in that directory
for fileName in os.listdir(intoDirectory):
    file_path = os.path.join(intoDirectory, fileName)
    # checking if it is a file
    if os.path.isfile(file_path):
        listOfFiles.append(file_path)


for direct in listOfFiles:
    file = open(direct)
    fileName = os.path.basename(direct)
    
    parsed_file = parse_fasta_file(file, False)

    file.close();

    # if parsed file does not have a pair of genes in it
    if(len(parsed_file) != 2):
        print("Deleting File: " + fileName + "")
        os.remove(direct)

