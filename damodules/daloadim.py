import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
def loadImage():
	testApp = True
	if testApp == True:
		img = Image.open("/opt/deepapp/work/dog.jpeg")
	else:
		BASE_URL = "http://localhost:8080/getCurrentImageUrl/"
		applicationId = "catDog"
		# api-endpoint 
		URL = BASE_URL + applicationId
		# sending get request and saving the response as response object 
		r = requests.get(url = URL) 
		data = r.text
		print("Response : " + data) 
		response = requests.get(data)
		img = Image.open(BytesIO(response.content))
	
	
	return img
def serveImage(changedImage):
	testApp = True
	if testApp == True:
		plt.imshow(changedImage)
	else:
		BASE_URL = "localhost:8080/sendCurrentImageUrlToJava/"
		image_file = BytesIO()
		changedImage.save(image_file, "jpeg")
		image_file.seek(0)
		applicationId = "catDog"
		# api-endpoint 
		URL = BASE_URL + applicationId

		# sending get request and saving the response as response object 
		
		
		files = {'files': image_file}
		response = requests.post(URL, files=files)
		print(response)

