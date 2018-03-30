from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                resize:none;
            }}
        </style>
    </head>
    <body>
      <form action="/encrypt" method="POST">
        
            Rotate by: <input type="text" name="rot" value="0">
            <textarea name="text">{0}</textarea>
            <input type="submit"/>
        
      </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    return form.format(rotate_string(text, int(rot)))

@app.route("/")
def index():
    return form.format("")

app.run()