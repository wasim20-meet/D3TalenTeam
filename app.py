from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    


@app.route('/sent', methods=['POST'])
def sentI():
    #check that username isn't already taken
    add_user(request.form['name'],request.form['email'],request.form['subject'],request.form['message'])
    return render_template('thanksforsending.html')



if __name__ == '__main__':
    app.run(debug=True)

