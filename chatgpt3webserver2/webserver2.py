from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import unittest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')


class TestWebServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_signup(self):
        # Test signing up with a new user
        rv = self.app.post('/signup', data={'username': 'testuser', 'password': 'testpass'})
        assert b'signup' not in rv.data
        # Test signing up with an already-used username
        rv = self.app.post('/signup', data={'username': 'testuser', 'password': 'testpass'})
        assert b'signup' in rv.data

    def test_login(self):
        # Test logging in with correct credentials
        rv = self.app.post('/login', data={'username': 'testuser', 'password': 'testpass'})
        assert b'login' not in rv.data
        # Test logging in with incorrect credentials
        rv = self.app.post('/login', data={'username': 'testuser', 'password': 'wrongpass'})
        assert b'login' in rv.data


if __name__ == '__main__':
    unittest.main()
