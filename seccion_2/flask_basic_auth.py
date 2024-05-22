from werkzeug.wrappers import Request, Response
from flask import Flask, request

class basic_auth_middleware():

    def __init__(self, app):
        self.app = app
        self.username = 'federico'
        self.password = 'securepass'

    def __call__(self, environ, start_response):
        request = Request(environ)
        username = request.authorization['username']
        password = request.authorization['password']

        if username == self.username and password == self.password:
            environ['user'] = { 'name': 'Federico' }
            return self.app(environ, start_response)

        response = Response(u'Authorization failed\n', mimetype= 'text/plain', status=401)
        return response(environ, start_response)
    


app = Flask('basic_auth_demo')
app.wsgi_app = basic_auth_middleware(app.wsgi_app)

@app.route('/protected_endpoint', methods=['GET'])
def some_view():
    user = request.environ['user']
    return f"Hi {user['name']}\n"

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)