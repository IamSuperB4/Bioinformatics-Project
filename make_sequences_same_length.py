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
fromDirectory = 'Genomes/CombineDopamineGeneFiles'
intoDirectory = 'Genomes/CombinedDopamineFileSameLength/'

listOfFiles = []
    
# iterate over files in that directory
for filename in os.listdir(fromDirectory):
    f = os.path.join(fromDirectory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        listOfFiles.append(f)

for direct in listOfFiles:
    fileName = os.path.basename(direct)
    fileName_NoExtension = os.path.splitext(fileName)[0]

    file = open(direct)
    fileName = os.path.basename(direct)

    parsed_file = parse_fasta_file(file, False)
    file.close()

    newFileString = ""
    lenOfLongestSeq = 0

    for key in parsed_file:
        if len(parsed_file[key]) > lenOfLongestSeq:
            lenOfLongestSeq = len(parsed_file[key])

    for key in parsed_file:
        new_line = key.replace('lcl', '>lcl')

        if len(parsed_file[key]) < lenOfLongestSeq:
            addBlanks = '-' * (lenOfLongestSeq - len(parsed_file[key]))
            parsed_file[key] = parsed_file[key] + addBlanks
            
        newFileString += new_line + '\n' + parsed_file[key] + '\n'

    print("Creating File: " + intoDirectory + fileName)
    with open(intoDirectory + fileName, 'a+') as newFile:
        newFile.write(newFileString)
