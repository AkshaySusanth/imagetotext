from PIL import Image
import pytesseract
from pytesseract import image_to_string
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/text/<name>')
def text(name):
        return '<html><head><link rel = "stylesheet" type="text/css" href="style.css"></head><body><textarea rows="50" cols="150"> %s </textarea></body></html>' % name

@app.route('/img2txt', methods = ['POST'])
def getvalue():
        user = request.form['fileToUpload']
        img = Image.open(user)
        text = pytesseract.image_to_string(img)
        return redirect(url_for('text',name = text))



if __name__ == '__main__':
    app.run(debug = True)