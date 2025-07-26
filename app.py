from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Registered user: {username}, {email}")
        return f"User {username} registered successfully"
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

