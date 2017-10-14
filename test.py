from flask import Flask, render_template, request
from werkzeug import secure_filename
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='ed78ccc5e8764fee8fc8c750ef421de2')
appF = Flask(__name__)

@appF.route('/upload')
def upload_file2():
	return render_template('upload.html')

@appF.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		#return determine(f.filename)
		return render_template('afterUpload.html', answer = determine(f.filename))
		#return 'file uploaded successfully'





def determine (image):

	# get the general model
	#model = app.models.get("general-v1.3")
	model = app.models.get("Ocean Cleanup")
	image = ClImage(file_obj=open(image, 'rb'))
	output = str (model.predict([image]))

	#find concepts related to image
	index = output.find("u'name'") + 1
	conc = []
	for i in range(1, output.count("u'name'")):
		index = output.find("u'name'", index + 1)
		conc.append(output[index + 11:output.find("'", index + 13)])
	#obj = "not found"
	#for i in conc:
	#	if (i == "bottle" or i == "can" or i == "balloon" or i == "cigarettes" or i == "plastic bag"):
	#		obj = conc[i]
	#		break


	jsonTags = model.predict([image])

	#print (jsonTags['outputs'][0]['data']['concepts'][0]['name'])
	names = []
	for tag in jsonTags['outputs'][0]['data']['concepts']:
		names.append(tag['name'])
	obj = "not found"
	for i in names:
		if (i == "bottle" or i == "can" or i == "balloon" or i == "cigarettes" or i == "plastic bag"):
			obj = i

	return obj



if __name__ == '__main__':
   appF.run(debug = True)






