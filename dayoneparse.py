__author__ = 'user'
inputfile = 'input/entries.txt'
splittingtxt = 'Date:'
filenameformat = 'output/file#.txt'
replacementfilename = 'foo'


def output(filenum, line):
    filename = filenameformat.replace('file#',replacementfilename)
    fout = open(filename, 'w')
    fout.write(line)
    fout.close


file = open(inputfile)
lines = file.read().split(splittingtxt)


for i in range(0,len( lines ) ):
    currentline = lines[i]                                          # the first line is empty
    thisline =  currentline.splitlines(0)                           # extract the time and date for the file name
    extractedreplacement = thisline[0]                              # just grab the date and time
    extractedreplacement = extractedreplacement.replace(":","")     # remove the :
    extractedreplacement = extractedreplacement.replace("/","_",3)  # remove delimiters
    extractedreplacement = extractedreplacement.replace("\t","",3)  # remove the tab character
    replacementfilename = extractedreplacement                      # use the extracted replacement
    output(i, lines[i])                                             # move forward
