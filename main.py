
from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup', methods= ['GET', 'POST'])
def sign_up():

    has_errors= False

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        verifypassword = request.form['verify']
        email = request.form['email']
            
        username_error= ''
        password_error = ''
        verify_error = ''
        email_error = ''

        # username verifacatction
        if len(username) > 20 or len(username) < 3:
            username_error= 'Username must be between 3-20 characters'
            username= ''
            
            has_errors= True

        if ' ' in username:
            username_error= 'Username cannot have spaces'
            username= ''

            has_errors= True
        
        #password verifacation
        if len(password) > 20 or len(password) < 3:
            password_error= 'Password must be between 3-20 characters'
            password= ''

            has_errors= True
            
        if password != verifypassword:
            verify_error= 'Passwords must match'
            verifypassword= ''

            has_errors = True

        if len(verifypassword) < 1:
            verify_error= 'Cannot leave blank'
            verifypassword= ''

            has_errors= True

        if ' ' in password:
            password_error= 'Password cannot contain spaces'
            password= ''

            has_errors= True

        #email verifacation
        if len(email) > 0: 
            
            if email.count('@') > 1 or email.count('@') < 1:
                email_error= 'Invalid email'
                email= ''

                has_errors= True
                
            if email.count('.') > 1 or email.count('.') < 1:
                email_error= 'Invalid email'
                email= ''

                has_errors= True

            if ' ' in email:
                email_error= 'Email cannot contain spaces'
                email= ''

                has_errors= True

            if len(email) > 20 or len(email) < 3:
                email_error= 'Email must be between 3-20 characters'
                email= ''

                has_errors= True

        if has_errors == True:
            
            return render_template('home.html', username_error= username_error, 
                password_error= password_error, verify_error= verify_error, username= username,
                password = password, verifypassword= verifypassword,email_error= email_error,
                email= email, form= request.form)
        
        else:    
        
            if not username_error and not password_error and not verify_error:
                
                return redirect('/welcome/?username={0}'.format(username))   #success message

    if request.method == 'GET':
        return render_template('home.html', form= {})

    
        return redirect('/welcome/')

@app.route('/welcome/', methods= ['GET', 'POST'])
def welcome():
    if not request.args.get('username', None):
        return redirect('/signup/')
    first_name = request.args.get('username')
    return render_template('welcome.html', name= first_name + '!')

if __name__ == '__main__':
    app.run()

