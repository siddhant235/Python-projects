import sys
import PyPDF2

inputs=sys.argv[1:]
def pdf_merger(pdflist):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdflist:
        merger.append(pdf)
    merger.write('merged.pdf')
pdf_merger(inputs)

