import qrcode
name = ""
print('Enter the text')
name = input(name)
img = qrcode.make(name)
url =name + '.jpg'
print(url)
img.save(url)