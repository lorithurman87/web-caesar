from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

from caesar import rotate_string

form = """
<!DOCTYPE HTML>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding:20px;
                margin: 0 auto;
                width:540px;
                font:16px sans-serif;
                border-radiusL 10px;
            }}
            textarea {{
                margin:10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label> Rotate by:
            
            <input type="text" value="0" name="rot"/>
            
            </label>

        <textarea name="text" {0}.format> </textarea>
        <input type="submit" value="Submit Query"/>            
      
    </body>
</html>


"""

@app.route("/", methods=['POST'])
def encrypt():
    rots = int(request.form['rot'])
    texts = request.form.get("text")
    var3 = rotate_string(texts, rots)
    return form.format("<h1>" + (var3) + "</h1>")
    


@app.route("/")
def index():
    return form.format('')

app.run()
