from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
                resize:none;
            }
        </style>
    </head>
    <body>
      <form action="/encrypt" method="POST">
        <label for="user-text">
            Rotate by: <input type="text" name="rot" value="0">
            <textarea name="text"></textarea>
            <button type="submit">Submit Query</button>
        </label>
      </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encrypted = ''
   
    for char in text:
        encrypted = encrypted + rotate_string(text, rot)
        user_content = "<h1>" + encrypted + "</h1>"
    return user_content  

@app.route("/")
def index():
    return form

app.run()