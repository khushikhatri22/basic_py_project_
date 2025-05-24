'''pdf merger
pdf file shoudl be in same foulder'''
from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs=[]
n=int(input ("how many pdfs do you want to merge : "))

for i in range (0,n):
    name= input(f"Enter the name of pdf {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
