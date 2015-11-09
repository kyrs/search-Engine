from flask import Flask,request
from flask import render_template
from kyrselastic import query_dsl
import unicodedata
from werkzeug import secure_filename
import os 
app =Flask(__name__)


# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png','doc','docx'])



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/personal')
def personal():
    return render_template('upload.html')

@app.route('/query', methods=['POST','GET'])
def handle_data():
    print "i got it "
    query = request.form['searched_text']
    query = unicodedata.normalize('NFKD', query).encode('ascii','ignore')
    print type(query)
    post = query_dsl(query=query)
    return render_template('page.html',
                           posts=post)
    
@app.route('/upload', methods=["POST"])
def upload():

    # Get the name of the uploaded files
    uploaded_files = request.files.getlist("file[]")
    print uploaded_files
    filenames = []
    for file in uploaded_files:
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to the upload
            # folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Save the filename into a list, we'll use it later
            filenames.append(filename)
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
    # Load an html page with a link to each uploaded file
    return "DONE !!!"
    #return render_template('upload.html', filenames=filenames)
    print filenames

if __name__ == "__main__":
    app.run(debug=True)