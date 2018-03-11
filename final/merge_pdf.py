from PyPDF2 import PdfFileMerger

pdfs = ['o_p2.pdf', 'o_p5.pdf']


merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")