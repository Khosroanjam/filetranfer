from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'upload'

app = Flask(__name__, template_folder='templates')
app.secret_key = 'kh0sr0@n0m'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    users = db.relationship('users', backref=db.backref('urls', lazy=True))
    filename = db.Column(db.Text)
    urladdress = db.Column(db.Text)
    haspassword = db.Column(db.Text)
    password = db.Column(db.Text)
    active = db.Column(db.Text)
    reserve1 = db.Column(db.Text)
    reserve2 = db.Column(db.Text)
    def __init__(self, userid , filename, urladdress, active, haspassword, password):
        self.userid = userid,
        self.filename = filename,
        self.urladdress = urladdress,
        self.haspassword = haspassword,
        self.password = password,
        self.active = active,
        self.reserve1 = "",
        self.reserve2 = ""
    def __repr__(self):
        return self.urladdress
    def __url__(self):
        return self.urladdress
    def __Str__(self):
        return self.filename


class  users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    family = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    active = db.Column(db.Boolean)
    def __username__(self):
        return str(self.username)

@app.route("/", methods=['GET', 'POST'])
def main():
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
        u = urls(userid=1, filename = str(filename), urladdress = "qwe", haspassword=str('false'), password="", active=str('true'))
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('success'))

    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)