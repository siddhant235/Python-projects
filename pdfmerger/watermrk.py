import PyPDF2
template=PyPDF2.PdfFileReader(open('merged.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('original2.pdf','rb'))
output=PyPDF2.PdfFileWriter()
for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
with open('watermarked.pdf','wb') as myfile:
    output.write(myfile)
