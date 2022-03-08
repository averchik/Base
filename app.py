
from unicodedata import name
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "doc/"

name = {}

def Save(b):
   print("save")
   global name
   name.update(b)
   print(name)

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        result = request.form.to_dict()
        Save(result)
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = file.read()
        
        
    return render_template('content.html', content=content, name = name) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

