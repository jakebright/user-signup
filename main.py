
from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup', methods= ['GET', 'POST'])
def sign_up():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        verifypassword = request.form['verify']
        email = request.form['email']
            
        username_error= ''
        password_error = ''
        verify_error = ''
        email_error = ''

        has_errors= False

        # username verifacation
        if len(username) > 20 or len(username) < 3:
            username_error= 'Username must be between 3-20 characters'
            username= ''

            has_errors== True

            return render_template('home.html', username_error= username_error)

        
        #password verifacation
        elif len(password) > 20 or len(password) < 3:
            password_error= 'Password must be between 3-20 characters'
            password= ''

            has_errors== True
            

            return render_template('home.html', password_error= password_error)

        elif password != verifypassword:
            verify_error= 'Passwords must match'
            verifypassword= ''

            has_errors == True

            return render_template('home.html', verify_error= verify_error)

        elif has_errors == True:

            return render_template('home.html', username_error= username_error, 
                password_error= password_error, verify_error= verify_error, username= username,
                password = password, verifypassword= verifypassword)
        
        else:    
        
            if not username_error and not password_error and not verify_error:
                
                return redirect('/welcome/?username={0}'.format(username))   #success message


    else:
                
        return render_template('home.html')
    
    if request.method == 'GET':
        return render_template('home.html')

    
        return redirect('/welcome/')

@app.route('/welcome/', methods= ['GET', 'POST'])
def welcome():
    if not request.args.get('username', None):
        return redirect('/signup/')
    first_name = request.args.get('username')
    return render_template('welcome.html', name= first_name + '!')

if __name__ == '__main__':
    app.run()

