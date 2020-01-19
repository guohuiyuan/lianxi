import os
from PIL import Image,ImageDraw,ImageFont
import re
iphone5_width=400
iphone5_depth=300

if __name__ == '__main__':
    path="picture2"
    allfile = os.listdir(path)
    count=0
    for pic in allfile:
        print(pic)
    print("\n")
    for pic in allfile:
        pic =os.path.join(path,pic)
        im = Image.open(pic)
        w, h = im.size
        if w > iphone5_width:

            print("图片名称为" + pic + "图片被修改")
            h = iphone5_width * h // w
            w = iphone5_width
            count = count + 1

            out = im.resize((w, h), Image.ANTIALIAS)
            new_pic = re.sub(r'\.', '_new.', pic)
            print (new_pic)
            out.save(new_pic)
        elif h > iphone5_depth:

            print("图片名称为" + pic + "图片被修改")
            w = iphone5_depth * w // h

            h = iphone5_depth
            count = count + 1
            out = im.resize((w, h), Image.ANTIALIAS)
            new_pic = re.sub(r'\.', '_new.', pic)
            print (new_pic)
            out.save(new_pic)
    print("end")
    count = str(count)
    print("共有" + count + "张图片尺寸被修改")
