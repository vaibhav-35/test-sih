from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'flask/upload'
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def myApp():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def uploadFile():

    img = request.files['img']
    imgname = secure_filename(img.filename)
    img.save(os.path.join(app.config['UPLOAD_FOLDER'],imgname))
    return render_template('index.html',f = img)

if __name__ == '__main__':
   app.run(debug =True)