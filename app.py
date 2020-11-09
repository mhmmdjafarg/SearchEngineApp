import os
from flask import Flask, request, redirect, render_template, flash
from nltk.util import pr
from werkzeug.utils import secure_filename
import shutil
import fungsi

app = Flask(__name__)
app.secret_key = "tubesalgeo" #random secret key, can be anything
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #Max content length = 16 mb

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads') #the directory name will be 'uploads'

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods = ['POST', 'GET'])
def home():
    if(request.method == 'POST'):
        text = request.form['search']
        print(text)
    return render_template('home.html')

@app.route('/upload', methods=['POST' , 'GET'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return render_template('home.html')

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/')

# @app.route('/flush')
# def flush():
#     if (os.path.isdir(UPLOAD_FOLDER)):
#         shutil.rmtree(UPLOAD_FOLDER)
#         flash('File(s) succesfully flushed')
#     else:
#         flash('There are no uploads yet')
#     return redirect('/')

if __name__ == '__main__':
  app.run(debug = True)