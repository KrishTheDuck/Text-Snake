from caterpillar import Caterpillar
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def home():
    # don't touch <> they're there for code maintenance and to make sure a new line doesn't happen
    return f'''
<!DOCTYPE html>
<html lang="en">
<div style="white-space: pre-wrap;text-align:center">
<title>Snake</title
><h1 style="color:blue;text-align:center">Welcome to Snake.</h1
><h3><b><u>Endpoints:</b></u></h3
><ol style="list-style-position: inside"
><li>Linear Text Snake: {escape("/linear/<w>/<level>/<o>")}</li
><li>Sine Test Snake: {escape("/sine/<w>/<x_scale>/<amp>/<level>")}</li
><li>Helix Test Snake: {escape("/helix/<w>/<x_scale>/<amp>/<level>")}</li
></ol>
</div>
<body>
<p style="text-align:left;color:red">
<u>Key:</u><ul>
<li>w → the word to be snakified
<li>level → the highest number of spaces
<li>o → the number of oscillations
<li>x_scale → vertical stretch
<li>amp → amplitude (of sine)
</ul>
</p>
</body> 
<p style="text-align:left;color:green">
<u>Our githubs:<u
>&nbsp&nbsp<a href="https://github.com/KrishTheDuck" title="Krish" style="font-size:15px">KrishTheDuck</a>
<a href="https://github.com/colinhartigan" title="Colin" style="font-size:15px">Colin Hartigan</a>
</p>
</html>
'''


@app.route('/sine/<w>/<x_scale>/<amp>/<level>', methods=["GET"])
def sine(w, x_scale, amp, level):
    text = Caterpillar.sin_print(str(w), int(x_scale), int(amp), int(level))
    return f'<!DOCTYPE html><div style="white-space: pre-wrap">{text}</div>'


@app.route('/linear/<w>/<level>/<o>', methods=["GET"])
def linear(w, level, o):
    text = Caterpillar.linear_print(str(w), int(level), int(o))
    return f'<!DOCTYPE html><div style="white-space: pre-wrap">{text}</div>'


@app.route('/helix/<w>/<x_scale>/<amp>/<level>', methods=['GET'])
def helix(w, x_scale, amp, level):
    text = Caterpillar.helix_print(str(w), int(x_scale), int(amp), int(level))
    return f'<!DOCTYPE html><div style="white-space: pre-wrap">{text}</div>'


def run():
    app.run(host='0.0.0.0', port=8080)
