import base64

fd = open('page1.svg', 'r')
data = fd.read()

image = open('pic.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)

print len(data)

print len(image_64_encode)

data = data.replace('id="image_1" xlink:href=""', 'id="image_1" xlink:href="data:image/jpeg;base64,' + image_64_encode + '"')

fw = open('test.svg', 'w')
fw.write(data)