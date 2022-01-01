import time
import Image
import os
print "-----------------------------------------"
print "IMAGE RESIZER AND CONVERTER"
print  "Text mode version 1.0"
print "                      BY EL SONADOR"
print "-----------------------------------------"
imageFile = raw_input("file name {for example file.jpg] ~ ")
im1 = Image.open(imageFile)
width = input("width of image ~ ")
height = input("height of image ~ ")
im2 = im1.resize((width, height), Image.NEAREST)
ext = raw_input("File extension [for example .jpg] ~ ")
im2.save( "output" + ext)
print "thanks for using IMAGE RESIZER AND CONVERTER"
time.sleep(5)


