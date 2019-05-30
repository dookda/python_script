# pip install python-resize-image

import os
import os.path
import glob
import PIL
from PIL import Image
# from resizeimage import resizeimage

basewidth = 500
imgs = []
path = "./in/tungyang"
out = "./out/tungyang"
valid_images = [".jpg", ".gif", ".png", ".jpeg"]
for f in os.listdir(path):
    # print(f)
    ext = os.path.splitext(f)[1]
    # print(ext)
    if ext.lower() in valid_images:
        img = Image.open(os.path.join(path, f))
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save(os.path.join(out, f))
        print('ok', f)
