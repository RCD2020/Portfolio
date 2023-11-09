from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True, port='5001', host='0.0.0.0')