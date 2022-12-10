from flask import Flask,request,jsonify
from OCR_dictionary import getAadharDictionary 
from werkzeug.utils import secure_filename
import urllib.request
import os
import json

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER="Static/Upload"
DUMP_FOLDER="Static/Dump"

@app.get("/")
def home():
    return "Welcome to the baseURL"

@app.route('/processAadhar', methods=['POST','GET'])
def processAadhar():
    # check if the post request has the file part
    if 'img' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['img']

    success=False
    errors = {}

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        success = True
    else:
        errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

    if success:
        imgpath=os.path.join(UPLOAD_FOLDER, filename)
        dumppath=os.path.join(DUMP_FOLDER, filename)
        adhdict=getAadharDictionary(imgpath,dumppath)
        adhjson = json.dumps(adhdict)
        
        #Clearing the files after the task is complete
        os.remove(imgpath)
        os.remove(dumppath)

        return adhjson

    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

if __name__=="__main__":
    app.run(host="0.0.0.0", port=6000)