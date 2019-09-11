from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageDraw
import requests
from damodules import daloadim
from io import BytesIO

model = load_model('dogcat_model_bak.h5')
imgOriginal = daloadim.loadImage()
img1 = imgOriginal.resize((64, 64), Image.ANTIALIAS)


#img1 = image.load_img('cat_image.jpeg', target_size=(64, 64))
img = image.img_to_array(img1)
img = img/255
# create a batch of size 1 [N,H,W,C]
img = np.expand_dims(img, axis=0)
prediction = model.predict(img, batch_size=None,steps=1) #gives all class prob.
d = ImageDraw.Draw(imgOriginal)
if(prediction[:,:]>0.5):
    value ='Dog :%1.2f'%(prediction[0,0])
    d.text((0,62), value, fill=(255,0,0))
else:
    value ='Cat :%1.2f'%(1.0-prediction[0,0])
    d.text((0,62), value, fill=(255,0,0))
daloadim.serveImage(imgOriginal)
"""plt.imshow(img1)
plt.show()
"""