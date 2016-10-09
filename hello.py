from flask import Flask
import json

"""
1. install anaconda python in your account
2. Create etc/conf.json from the etc/conf-template.json
2. Run as:  python hello.py
3. Put in your web browser: http://<host>:<port>

Of course you need to have access to the host, so you need to be behind the firewall or run VPN
"""

conf = json.load(open('etc/conf.json'))
host = conf['host']
port=conf['port']
debug = conf['debug'] in ['T' 'True' 't' 'true']

app = Flask(__name__)

print 'Hello, World!'

@app.route('/')
def hello_world():
    print 'hello console output'
    return 'hello web browser'

# use debug false when running on host other than localhost
app.run(host=host, debug=debug, port=port)

