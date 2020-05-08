from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/gym')
def test_world():
	return 'Gym Management System'  

@app.route('/signup')
def sign_up():
	return render_template("signup.html")	


@app.route('/register', methods = ['POST'])
def register():
	fullname = request.form['full_name']
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
	phone_number =request.form['phone_number'] 


	print(fullname)
	print(email)
	print(username)
	print(password)
	print(phone_number)

app.run()    
