from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def ola_mundo(): 
    """ return "<h1> Olá Mundo, Flask é Legal</h1> """
    return render_template("index.html")

@app.route("/quemsomos")
def quem():
    return render_template("quemsomos.html")

@app.route("/contatos")
def cadastro():
    return render_template("contatos.html")

if __name__ == "__main__":
    app.run(debug=True)