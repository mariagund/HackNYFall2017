from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from werkzeug import secure_filename
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import pyrebase

client = MongoClient("mongodb://kdingens:cleanbeach@localhost")
db = client['test-database']

appC = ClarifaiApp(api_key='ed78ccc5e8764fee8fc8c750ef421de2')
app = Flask(__name__)
Bootstrap(app)

config = {
    "apiKey": "AIzaSyDv8hQj5zBz_LK4dc81Tl8iB487LUaEl2k",
    "authDomain": "beachclean-60bfc.firebaseapp.com",
    "databaseURL": "https://beachclean-60bfc.firebaseio.com",
    "projectId": "beachclean-60bfc",
    "storageBucket": "",
    "messagingSenderId": "906697182839"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("kdingens@nd.edu","cleanbeach")
@app.route('/')
def welcome():
	return render_template('works.html')

@app.route('/cleanthebeach')
def cleanup():
	return render_template('cleanpage2.html', answer = 'Upload a picture of your trash above')


@app.route('/cleanthebeach', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		ans = determine(f.filename)
		beachnum = db.child("data").child("beaches").child("Hudson Bank").child(ans).get()
		beachnum = int(beachnum.val())+1
		setbeach = db.child("data").child("beaches").child("Hudson Bank").update({ans:beachnum})
		num = db.child("data").child(ans).child("number").get()
		num = int(num.val()) + 1
		set = db.child("data").child(ans).update({"number":num})
		ans = "Thank you for logging a " + ans
		return render_template('cleanpage2.html', answer = ans)
		#return 'file uploaded successfully'

@app.route('/trashlajolla')
def upload_graphic():
	return render_template('trashlajolla.html')

@app.route('/trashnewportbeach')
def upload_graphic1():
        return render_template('trashnewportbeach.html')

@app.route('/trashpensacola')
def upload_graphic2():
        return render_template('trashpensacola.html')

@app.route('/about')
def upload_about():
	return render_template('about.html')

def determine (image):

	# get the general model
	model = appC.models.get("Ocean Cleanup")
	image = ClImage(file_obj=open(image, 'rb'))
	output = str (model.predict([image]))

	#find concepts related to image
	index = output.find("u'name'") + 1
	conc = []
	for i in range(1, output.count("u'name'")):
		index = output.find("u'name'", index + 1)
		conc.append(output[index + 11:output.find("'", index + 13)])


	jsonTags = model.predict([image])

	i = jsonTags['outputs'][0]['data']['concepts'][0]['name']
	obj = "not found"
	if (i=="bottle" or i == "can" or i == "balloon" or i == "cigarette" or i == "plastic bag"):
		obj = i
	return obj

if __name__ == '__main__':
	app.run(debug=True)
