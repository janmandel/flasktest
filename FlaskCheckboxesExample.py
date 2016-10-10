from flask import Flask
from flask import request
import json
import pprint

conf = json.load(open('etc/conf.json'))
host = conf['host']
port=conf['port']
debug = conf['debug'] in ['T' 'True' 't' 'true']

app = Flask(__name__)

print 'Hello, World!'

#Normally FORM_PAGE would be an external file like object, but here
#it's inlined
FORM_PAGE = """
    <html>
        <head>
            <title>Flask Form</title>
        </head>
        <body>
            <form action="/process" method="POST">

                 <fieldset>
                    <legend>Drink preferences</legend>
                    <label>Choices: </label><br/>
                    <input type="checkbox" name="drink_type[]" value="coffee" /> Coffee  <br/>
                    <input type="checkbox" name="drink_type[]" value="tea" /> Tea  <br/>
                    <input type="checkbox" name="drink_type[]" value="water" /> Water  <br/>
                 </fieldset>

                 <input type="submit" />
            </form>
    </html>
"""

@app.route('/')
def home_form():
    print 'hello console output'
#     return 'hello web browser'
    return FORM_PAGE

@app.route("/process", methods = ["GET", "POST"] )
def process_form():
    formData = request.form.getlist('drink_type[]') if request.method == "GET" else request.form.getlist('drink_type[]')
    response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(formData)
    pprint.pprint(formData)
    return response

# use debug false when running on host other than localhost
app.run(host=host, debug=debug, port=port)
