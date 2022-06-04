#!/usr/bin/env python3

__DESCRIPTION__ = """
Convert a FASTA alignment to Phylip format.
Dependenies: BioPython
fasta_to_phylip --input-fasta file.fasta --output-phy file.phy
"""

from Bio import SeqIO
import os

def main():
    fromDirectory = 'Genomes/CombinedDopamineFileSameLength/'
    intoDirectory = 'Genomes/AlignedPhy/'

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

        print(direct)
        print(intoDirectory + fileName_NoExtension + ".phy")

        records = SeqIO.parse(direct, "fasta")
        count = SeqIO.write(records, intoDirectory + fileName_NoExtension + ".phy", "phylip")
        print("Converted %i records" % count)


if __name__ == "__main__":
    main()

