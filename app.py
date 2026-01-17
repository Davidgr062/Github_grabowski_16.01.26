from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github_definition')
def github_definition():
    return render_template('Github_definition.html')


if __name__ == '__main__':
    app.run(debug=True)