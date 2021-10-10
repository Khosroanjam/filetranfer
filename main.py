from flask import Flask, render_template, request, flash, url_for, redirect
from model import sqlUtil, makeUrl
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'upload'

app = Flask(__name__, template_folder='templates')
app.secret_key = 'kh0sr0@n0m'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/", methods=['GET', 'POST'])
def main():
    u = makeUrl()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('NO FILE')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('NO FILE SELECTED')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        s = sqlUtil(userid=1, filename = str(filename), urladdress = u.make(), haspassword=str('false'), password="", active=str('true'))
        s.insert()
        return redirect(url_for('success'))

    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)