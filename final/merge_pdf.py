from PyPDF2 import PdfFileMerger

pdfs = ['o_pdfs/o_p1.pdf', 'o_pdfs/o_p2.pdf', 'o_pdfs/o_p3.pdf', 'o_pdfs/o_p4.pdf', 'o_pdfs/o_p5.pdf', 'o_pdfs/o_p6.pdf', 'o_pdfs/o_p7.pdf', 'o_pdfs/o_p9.pdf', 'o_pdfs/o_p10.pdf', 'o_pdfs/o_p11.pdf', 'o_pdfs/o_p12.pdf']


merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")