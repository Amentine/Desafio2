from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#Fazer conexao com BD
app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yyyetygvg1#'
app.config['MYSQL_DB'] = 'Desafio'

mysql = MySQL(app)

@app.route('/')
def ola_mundo(): 
    """ return "<h1> Olá Mundo, Flask é Legal</h1> """
    return render_template("index.html")

@app.route("/quemsomos")
def quem():
    return render_template("quemsomos.html")

@app.route("/contatos", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) values (%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'sucesso'
    return render_template("contatos.html")

#rota usuarios para listar os usuarios do BD
@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)


if __name__ == "__main__":
    app.run(debug=True)