from clarifai import rest
from clarifai.rest import ClarifaiAPp

app = ClarifaiApp(api_key=ed78ccc5e8764fee8fc8c750ef421de2)

# get the general model
model = app.models.get("general-v1.3")

def determine (image):

	image = ClImage(file_obj=open(f.filename, 'rb'))
	output = str (model.predict([image]))

	#find concepts related to image
	index = output.find("u'name'") + 1
	conc = []
	for i in range(1, output.count("u'name'")):
    	index = output.find("u'name'", index + 1)
    	conc.append(output[index + 11:output.find("'", index + 13)])

    for i in conc:
		if (i == "plastic bottle" or i == "can" or i == "balloon" or i == "cigarettes" or i == "plastic bag")
			obj = conc[i]
			break

	return obj






############
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method == 'POST':
		f = request.files['pic']
		f.save (secure_filename(f.filename))

    	response = determine(f)

	return render

app.run(debug=True)

