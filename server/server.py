from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify
import random
import os
from werkzeug import secure_filename

import content, ocr

app = Flask(__name__)
CORS(app, support_credentials=True)

UPLOAD_FOLDER = os.getcwd() + '/uploads/'
print ("folder is ", UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/api/text/", methods=["OPTIONS", "POST"])
@cross_origin(supports_credentials=True)
def text():
    try:
        data = request.json
        text = data['text']
        print ("text received is ", text)
        # Call the function here and the response send in return statement
        resp1,resp2,resp3 = content.get_text(text)
        return jsonify({'status':'success', 'response1':resp1,'response2':resp2,'response3':resp3})
        # Comment the below line when the function is ready
        #return j1,resp2,resp3atus':'success', 'response':'response from text summary'+ str(random.random())})
    except Exception as e:
        print ("Exception ", e)
        return "failed"

@app.route("/api/image/", methods=["OPTIONS", "POST"])
@cross_origin(supports_credentials=True)
def image():
    try:
        print ('file received is --> ',request.files['file'])
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        imagePath = app.config['UPLOAD_FOLDER'] + filename
        print ("file name is ", imagePath)
        # Call the function here and the response send in return statement
        resp1,resp2,resp3 = ocr.get_string(imagePath)
        return jsonify({'status':'success', 'response1':resp1,'response2':resp2,'response3':resp3})
        #return jsonify({'status':'success', 'response':'response from image summary'+ str(random.random())})
    except Exception as e:
        print ("Exception ", e)
        return "failed"

if __name__ == "__main__":
    print ("listening on port 3000")
    app.run(port=3000)
