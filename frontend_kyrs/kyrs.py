from flask import Flask,request
from flask import render_template
from kyrselastic import query_dsl
import unicodedata

app =Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST','GET'])
def handle_data():
    print "i got it "
    query = request.form['searched_text']
    query = unicodedata.normalize('NFKD', query).encode('ascii','ignore')
    print type(query)
    post = query_dsl(query=query)
    return render_template('page.html',
                           posts=post)
    

if __name__ == "__main__":
    app.run(debug=True)