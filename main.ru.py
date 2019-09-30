import requests
from flask import Flask

#text = requests.get('https://gist.github.com/DanteOnline/f59d99d92202b32515e00155dad3d38c').text

app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('https://gist.github.com/DanteOnline/f59d99d92202b32515e00155dad3d38c').text
    return text
print(hello)

if __name__ == "__main__":
    app.run()