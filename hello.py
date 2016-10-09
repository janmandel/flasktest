from flask import Flask

app = Flask(__name__)

print 'Hello, World!'

@app.route('/')
def hello_world():
    print 'Hello, World!'
    return 'Hello, World!'

app.run(debug=False)

