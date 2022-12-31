import unittest

from chatgpt3webserver.webserver import app
from chatgpt3webserver.reset_db import reset_db
from chatgpt3webserver.init_db import init_db


class TestWebServer(unittest.TestCase):
    def setUp(self):
        print("Setup done.....")
        reset_db()
        init_db()
        self.app = app.test_client()

    def test_signup(self):
        pass
        # Test signing up with a new user
        # rv = self.app.post('/signup', data={'username': 'testuser3', 'password': 'testpass'})
        # print(f'test signup reply {rv}')
        # assert b'signup' not in rv.data
        # Test signing up with an already-used username
        # rv = self.app.post('/signup', data={'username': 'testuser', 'password': 'testpass'})
        # assert b'signup' in rv.data

    def test_login(self):
        pass
        # Test logging in with correct credentials
        rv = self.app.post('/login', data={'username': 'testuser', 'password': 'testpass'})
        assert b'login' not in rv.data
        # Test logging in with incorrect credentials
        rv = self.app.post('/login', data={'username': 'testuser', 'password': 'wrongpass'})
        assert b'login' in rv.data


if __name__ == '__main__':
    unittest.main()