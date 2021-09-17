from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import pickle
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return redirect(f'/report?f_name={f.filename}')


@app.route('/report')
def solve():

    f_name = request.args.get('f_name')

    try:
        with open(f_name) as f:
            inp = f.readlines()
    except:
        return 'The report is missing'

    inp = [[float(feat.strip()) for feat in line.split(',')] for line in inp]

    model = pickle.load(open('model.pickle', 'rb'))
    res = model.predict(inp)
    os.remove(f_name)

    return render_template('report.html', text=res)


if __name__ == '__main__':
    app.run("0.0.0.0")
