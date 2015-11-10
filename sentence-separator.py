import re

# Prompt user for filepath for input file. Try to read in its text as a single string. Reprompt as long as file is not found.

filein = raw_input('Enter the filepath for the file you want to modify (including file extension).\n')
while True:
    try:
        f = open(filein, 'r')
        filedata = f.read()
        f.close
        break
    except IOError:
        filein = raw_input('That file was not found. Please try again.\nEnter the filepath for the file you want to modify (including file extension).\n')

# Prompt user for filepath for desired output file. Reprompt once if output file is the same as input file.

fileout = raw_input('Enter the desired filepath for the output file (including file extension).\n')
if filein == fileout:
    fileout = raw_input('Overwriting the original file is not recommended. Enter the desired name of the output file (including file extension).\n')

# Find ends of sentences in filedata that are not already followed by newline characters, and insert newline characters.

# Notes: [.?!] is used as an indicator of the end of a sentence. It is preceded by [^.A-Z] and followed by [^.0-9] to avoid capturing ellipses, decimal numbers, 
# and initials. \'* is used to ensure that the the ends of quotations are captured. \s* captures widespace between sentences, which will be replaced
# with a newline character. [^\n] is used to ensure that the sentence is not already followed by a newline character, e.g. at the end of a paragraph.

filedata = re.sub(r'([^.A-Z][.?!][^.\w]\'*)(\s*)([^\n])', r'\1\n\3', filedata)

# Eliminate newlines after "e.g." and "i.e."

filedata = re.sub(r'(.[eg].\s)\n', r'\1', filedata)

# Write the result to the output file, and close that file.

f = open(fileout, 'w')
f.write(filedata)
f.close