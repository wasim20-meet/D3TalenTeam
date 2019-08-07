from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    

# @app.route('/sent', methods=['POST'])
# def sentI():
#     user = get_user(request.form['username'])
#     if user != None and user.verify_password(request.form["password"]):
#         login_session['name'] = user.username
#         login_session['logged_in'] = True
#         return logged_in()
#     else:
#         return home()


@app.route('/sent', methods=['POST'])
def sentI():
    #check that username isn't already taken
    add_user(request.form['name'],request.form['email'],request.form['subject'],request.form['message'])
    return render_template('thanksforsending.html')


# @app.route('/logged-in')
# def logged_in():
#     return render_template('logged.html')


# @app.route('/logout')
# def logout():
#     user = None
#     login_session['logged_in'] = False
#     return home()



if __name__ == '__main__':
    app.run(debug=True)

