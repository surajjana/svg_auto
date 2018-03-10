from PyPDF2 import PdfFileMerger

pdfs = ['page1.pdf', 'test.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")