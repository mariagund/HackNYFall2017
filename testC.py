from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json


app = ClarifaiApp()

model = app.models.get("general-v1.3")

image = ClImage(url='https://www.travelalaska.com/~/media/Images/TravelAlaska/Content/ThingToDo/Fishing/video-thumb-ff.jpg')

jsonTags = model.predict([image])

print (jsonTags['outputs'][0]['data']['concepts'][0]['name'])

for tag in jsonTags['outputs'][0]['data']['concepts']:
    print(tag['name'])