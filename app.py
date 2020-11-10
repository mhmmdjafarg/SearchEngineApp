import os
from flask import Flask, session, request, redirect, render_template, flash
from nltk.util import pr
from werkzeug.utils import secure_filename
import shutil
from fungsi import WordData, getFirstSentence, txtToString, Ranking

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
        # Siapkan semua string
        session['query'] = request.form['search']
        text = txtToString()

        try:
            if (len(text) == 0):
                return render_template('home.html')
        except ZeroDivisionError:
            return render_template('home.html')
        
        # Simpan first sentece
        array_first_sentence = [getFirstSentence(string) for string in text]

        # Pindahkan ke filtered_text
        filtered_text = []
        filtered_text.append(session['query'])
        for string in text:
            filtered_text.append(string)

        # array of filtered text
        word_data = WordData(filtered_text)
        #array of rank
        ranks, array_sim = Ranking(word_data)
        return render_template('home.html', ranks = ranks, word_data = word_data, array_first_sentence = array_first_sentence, doc_count = len(array_first_sentence), array_sim = array_sim)
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

        path = os.path.join(os.getcwd() , 'uploads')
        session['listfile'] = os.listdir(path) #menyimpan array nama2 filenya di session
        flash('File(s) successfully uploaded')
        return redirect('/')

@app.route('/flush')
def flush():
    if ('listfile' in session):
        for i in session['listfile']:
            os.remove(os.path.join(UPLOAD_FOLDER,i))
        session.pop('listfile' , None)
    return ("nothing")

if __name__ == '__main__':
  app.run(debug = True)
