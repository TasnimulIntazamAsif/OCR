from PIL import Image

im_file = r"C:\Users\user\Downloads\image\pdfimg.png"

im = Image.open(im_file)
#im.rotate(90).show()
#im.show()
#print(im.size)
im.save("temp/pdfimg.png")
