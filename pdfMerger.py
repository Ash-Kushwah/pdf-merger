import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

# Getting the files from the current working directory
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        # merging the file 
        merger.append(file)
    # Giving name to the file 
    merger.write("combinedFiles.pdf")
    
    