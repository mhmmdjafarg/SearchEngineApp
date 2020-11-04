
from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET'])
def home():
  if(request.method == 'POST'):
        text = request.form['search']
        print(text)
  return render_template('home.html')


if __name__ == '__main__':
  app.run(debug=True)