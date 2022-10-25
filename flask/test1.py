'''
test1.py
'''
from flask import Flask , render_template , request


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/' , methods=('GET','POST'))
def index():
    return 'test1.py index is good'
            

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True )