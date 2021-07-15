#!/usr/bin/python
from PIL import Image
from os import listdir
from os.path import isfile, join

DIR_PATH = "images"
NEW_DIR = "/opt/icons/"
images = [file for file in listdir(DIR_PATH) if isfile(join(DIR_PATH, file))]

for image in images:
    if image.startswith('ic_'):
       path = join(DIR_PATH,image)
       print(path)
       im = Image.open(path).convert('RGB')
       new_img = im.resize((128,128)).rotate(270)
       new_img.save(join(NEW_DIR,image), "JPEG")
