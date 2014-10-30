from flask import Flask
from flask import request
from werkzeug import secure_filename
from flask import make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',202
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
