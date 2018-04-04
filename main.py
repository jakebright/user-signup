
from flask import Flask, request, redirect, render_template, url_for
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/welcome/', methods= ['GET'])
def welcome():
    import pdb; pdb.set_trace()       
    
    if not request.args.get('username', None):
        return redirect('/signup/')
    first_name = request.form['username']
    return render_template('welcome.html', name= '')


#@app.route('/signup/', methods= ['GET', 'POST'])
#def display_signup_form():
    
@app.route('/signup/', methods= ['GET', 'POST'])
def sign_up():
    import sys

    error= ''
    try: 

        if request.method == 'POST':
            sys.stderr.write('this shit is confusing\n')

            username = request.form['username']
            password = request.form['password']
            verifypassword = request.form['verify password']

            username_error= ''
            password_error= ''
            print('verify username or password')      
            if password == verifypassword:
                _url = '/welcome/?username=%s' %username
                import pdb; pdb.set_trace()       

                return redirect(_url)

            else:
                error = 'passwords must match'
        if request.method == 'GET':
            return render_template('home.html')

    except:
        return redirect('/welcome/')

app.run()


