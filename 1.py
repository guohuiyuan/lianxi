from PIL import Image,ImageDraw,ImageFont
path="C:\\Users\艾玛\Desktop\QQ图片20191209194145.jpg"
im=Image.open(path)
text='3'
w,h=im.size
draw= ImageDraw.Draw(im)
myfont=ImageFont.truetype("C:\Windows\Fonts\simhei.ttf",int(w/5))
draw.ellipse([w-w/5,0,w,w/5],fill="red")
draw.text([545,0],text,"white",myfont)
im.show()
img=im.resize((128,128))
img.save("0000.jpg")
