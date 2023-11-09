from flask import Flask, render_template, abort

app = Flask(__name__)


# Main Pages
@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/projects/<project>')
def projectView(project):
    try:
        return render_template(f'{project}.html')
    except:
        abort(404)


@app.errorhandler(404)
def error404(e):
    return render_template('notFound.html')


# Simulated Pages



# run
if __name__ == '__main__':
    app.run(debug=True, port='5001', host='0.0.0.0')