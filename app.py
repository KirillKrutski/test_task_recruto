from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():  # put application's code here
    name = request.args.get('name', 'name')
    message = request.args.get('message', 'message')
    return f"Hello {name}! {message}!"


if __name__ == '__main__':
    app.run(host='localhost', port= 5000)

