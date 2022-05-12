








'''
import os

fullGenome = 'Genomes\Genomes\Dipodomys_ordii_genomic.fna'
proteins = 'Genomes\Proteins\Dipodomys_ordii_protein.fna'


os.system("muscle -profile -in1 " + proteins + " -in2 " + fullGenome + " -out /Genomes/Aligned combinedAlignment.fasta -maxmb 15000")



from Bio.Align.Applications import MuscleCommandline
from io import StringIO

from Bio import AlignIO


#muscle_exe = "D:\Users\seaha\Downloads\muscle5.1.win64.exe" #specify the location of your muscle exe file
alignment = AlignIO.read("Genomes\Genomes\Dipodomys_ordii_genomic.fna", "fasta")
print(alignment)





input_sequences = "hiv_protease_sequences_w_wt.fasta"
output_alignment = "output_alignment.fasta"

def align_v1 (Fasta): 
    muscle_cline = MuscleCommandline(muscle_exe, input=Fasta, out=output_alignment)
    stdout, stderr = muscle_cline()
    MultipleSeqAlignment = AlignIO.read(output_alignment, "fasta") 
    print(MultipleSeqAlignment)

align_v1(input_sequences)








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

def compareSequences(largeSequence, smallSequence):
    for a in pairwise2.align.globalxx(largeSequence, smallSequence):
        print(format_alignment(*a))


#Normally this would be determined
#by user input via argparse. Hard-coded for now
dogChromosome = 'Genomes/Dog/sequence0.fasta'
humanGene = 'Genomes/Human/gene0.fna'
#dogChromosome = 'Genomes/test/dogtest.fasta'
#humanGene = 'Genomes/test/humantest.fna'

#dogFile = open(dogChromosome)
#humanFile = open(humanGene)

#parsed_dog = parse_fasta_file(dogFile, True)
#parsed_human = parse_fasta_file(humanFile, True)

allDogSequences = []
allHumanSequences = []

for i in (0,37):
    for j in (0,4):
        dogChromosome = 'Genomes/Dog/sequence' + str(i) + '.fasta'
        humanGene = 'Genomes/Human/gene' + str(j) + '.fna'

        dogFile = open(dogChromosome)
        humanFile = open(humanGene)

        allDogSequences.append(parse_fasta_file(dogFile, True))
        allHumanSequences.append(parse_fasta_file(dogFile, True))

for dogElement in allDogSequences:
    for humanElement in allHumanSequences:
        for key in dogElement:
            for key2 in humanElement:
                result = compareSequences(dogElement[key], humanElement[key2])

#print(parsed_seqs)
'''