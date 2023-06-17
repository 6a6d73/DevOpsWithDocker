from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<span style="white-space: pre-line">Hello, world!&#10;&#13;-Docker</span>'

@app.route('/hidden')
def hello_container():
    return '<span style="white-space: pre-line">Sometimes I am Docker, sometimes, I am Podman!\nIf you are unable to tell which is which...\nThen that is good for me.</span>'