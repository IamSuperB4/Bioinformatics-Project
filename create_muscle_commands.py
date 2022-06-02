import os

fromDirectory = 'Genomes/ACTN3_Genes/' # put / at the end of string
intoDirectory = 'Genomes/ACTN3_Aligned/' # put / at the end of string
pathToMuscleExe = './muscle5.1.win64.exe'

listOfFiles = []

for filename in os.listdir(fromDirectory):
    f = os.path.join(fromDirectory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        listOfFiles.append(f)

for direct in listOfFiles:
    file = open(direct)
    fileName = os.path.basename(direct)

    inputFileName  = os.path.join(fromDirectory, fileName)
    outputFileName = os.path.join(intoDirectory, fileName)

    print(pathToMuscleExe + " -verbose " +  " -align \"" + inputFileName + "\" -output \"" + outputFileName + "\"")
