from itertools import groupby
from PyPDF2 import PdfFileMerger
import base64
import os
import sys

templates_with_one_pic = ['p2.svg']
templates_with_two_pics = ['p5.svg']

pics_dir_list = os.listdir(sys.argv[1])
pics_dir_list = sorted(pics_dir_list)

pics_list_one = []
pics_list_two = []


def get_base64(image_file):
	""" 
		Input  : JPG or PNG Image
		Output : Encoded Base64 Data URI
	"""

	print image_file
	image = open( sys.argv[1] + '/' + str(image_file), 'rb')
	image_read = image.read()
	image_64_encode = base64.encodestring(image_read)
	image_64_encode = 'data:image/jpeg;base64,' + image_64_encode

	return image_64_encode

def update_svg(template_name, pics_list):
	fd = open(template_name, 'r')
	data = fd.read()

	for i in range(0, len(pics_list)):
		encoded_base64_data_uri = get_base64(pics_list[i])

		if(i == 0):
			data = data.replace('id="image" xlink:href=""', 'id="image" xlink:href="' + encoded_base64_data_uri + '"')
		else:
			data = data.replace('id="image' + str(i) + '" xlink:href=""', 'id="image" xlink:href="' + encoded_base64_data_uri + '"')

	fw = open('o_' + template_name, 'w')
	fw.write(data)

	print 'Updating ' + template_name

def svg2pdf(list):
    """Convert all svg files to pdf according to specified options"""

    options = '--without-gui --export-area-drawing'
    print '\nConverting, please wait...\n'
    for file in list:
        print 'Converting file: %s' %file
        pdf_abspath = file.split('.')[0]
        os.system('inkscape %s "%s" --export-pdf="pdfs/%s.pdf"' %(options, file, pdf_abspath))

def gen_svg(template_list_name, pics_list_name):
	for i in range(0, len(pics_list_name)):
		update_svg(template_list_name[i], pics_list_name[i])

def gen_pdf(template_list_name):
	a = []
	for i in range(0, len(template_list_name)):
		a.append('o_' + template_list_name[i])

	svg2pdf(a)


for i in range(0, len(pics_dir_list)):
	if(len(pics_dir_list[i].split('_')) <= 1):
		pics_list_one.append([pics_dir_list[i]])
	else:
		pics_list_two.append(pics_dir_list[i])


pics_list_two = [list(g) for k, g in groupby(pics_list_two, lambda s: s.partition('_')[0])]

gen_svg(templates_with_one_pic, pics_list_one)
gen_svg(templates_with_two_pics, pics_list_two)

gen_pdf(templates_with_one_pic)
gen_pdf(templates_with_two_pics)

merger = PdfFileMerger()

pdfs = os.listdir('./pdfs')
pdfs = sorted(pdfs)

new_pdfs = []

for i in range(0, len(pdfs)):
	new_pdfs.append('./pdfs/' + pdfs[i])

for pdf in new_pdfs:
    merger.append(pdf)

merger.write("result.pdf")