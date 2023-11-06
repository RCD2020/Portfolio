from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return send_from_directory('static', 'documents/resume.pdf')


if __name__ == '__main__':
    app.run(debug=True)