from flask import Flask, request, render_template_string
import main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index23.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    a=main.abc(user_input)
    return a
    # return f"Received input: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
