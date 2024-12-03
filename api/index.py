# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__, template_folder="../templates", static_folder="../static")

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/process', methods=['POST'])
# def process():
#     data = request.json.get('data', '')
#     return jsonify({"message": f"You entered: {data}"})

# # Export app for Vercel
# app = app

# -----------------------------------------------------------------------------------------------------
# new

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            return "Login Successful"
        else:
            return "Invalid credentials"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)