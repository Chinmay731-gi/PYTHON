import PyPDF2

pdfiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfFileReader = PyPDF2.PdfReader(pdfFile)
    merger.append(filename)
pdfFile.close()
merger.write('merged.pdf')