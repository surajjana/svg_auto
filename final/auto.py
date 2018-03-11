import base64
import sys

templates = ['p5.svg', 'p6.svg', 'p7.svg', 'p8.svg', 'p9.svg']
# pics = ['4.jpg', '1.jpg', '2.jpg', '5.jpg', '3.jpg']
pics = [['1.jpg','2.jpg'], ['3.jpg','4.jpg'], ['5.jpg','6.jpg']]

# for i in range(0, len(templates)):

# 	print 'Updating ' + templates[i]

# 	fd = open('templates/' + templates[i], 'r')
# 	data = fd.read()

# 	image = open('pics/' + pics[i], 'rb')
# 	image_read = image.read()
# 	image_64_encode = base64.encodestring(image_read)

# 	print len(data)

# 	print len(image_64_encode)

# 	data = data.replace('id="image" xlink:href=""', 'id="image" xlink:href="data:image/jpeg;base64,' + image_64_encode + '"')

# 	fw = open('o_templates/o_' + templates[i], 'w')
# 	fw.write(data)

for i in range(0, len(pics)):

	print 'Updating ' + templates[i]
	fd = open('templates/' + templates[i], 'r')
	data = fd.read()

	image1 = open('pics/' + pics[i][0], 'rb')
	image_read1 = image1.read()
	image_64_encode1 = base64.encodestring(image_read1)

	image2 = open('pics/' + pics[i][1], 'rb')
	image_read2 = image2.read()
	image_64_encode2 = base64.encodestring(image_read2)

	data = data.replace('id="image" xlink:href=""', 'id="image" xlink:href="data:image/jpeg;base64,' + image_64_encode1 + '"')
	data = data.replace('id="image1" xlink:href=""', 'id="image" xlink:href="data:image/jpeg;base64,' + image_64_encode2 + '"')


	fw = open('o_templates/o_' + templates[i], 'w')
	fw.write(data)