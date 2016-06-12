import csv
import sys

rowNumber = 1
filename = sys.argv[1]
newFilename = "new" + filename.capitalize()

def writeHeader() :
    colNames = ["row", "sentence", "wordIndex", "form", "lemma",
                "upostag", "xpostag", "feats", "head", "deprel", "deps", "misc"]
    with open(newFilename, 'w') as f:
        f.write("\t".join(colNames) + "\n")

def writeChunk(currSentence, lines) :
    with open(newFilename, 'a') as f:
        for line in lines :
            newLine = str(rowNumber) + "\t" + ' '.join(currSentence) + "\t" + line
            f.write(newLine)

with open(filename, 'r') as file :
    writeHeader()
    currSentence = []
    lines = []
    for line in file:
        cols = line[:-1].split("\t")
        if len(cols) == 1:
            # Reset sentence
            writeChunk(currSentence, lines)            
            currSentence = []
            lines = []
            rowNumber = rowNumber + 1
        else :
            currSentence.append(cols[1])
            lines.append(line)
