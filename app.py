import os

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32)

contas = {}


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")

        if contas.get(usuario) == senha:
            session["usuario"] = usuario
            return redirect(url_for("pagina2"))

        flash("Usuário ou senha incorretos.")

    return render_template("inicio.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    usuario = request.form.get("usuario", "").strip()
    senha = request.form.get("senha", "")

    if not usuario or not senha:
        flash("Preencha o usuário e a senha para se cadastrar.")
    elif usuario in contas:
        flash("Esse usuário já está cadastrado.")
    else:
        contas[usuario] = senha
        flash("Cadastro realizado. Agora você pode entrar.")

    return redirect(url_for("inicio"))


@app.route("/pagina2")
def pagina2():
    usuario = session.get("usuario")
    if usuario is None:
        flash("Faça login para acessar essa página.")
        return redirect(url_for("inicio"))

    return render_template("pagina2.html", usuario=usuario)


@app.route("/sair", methods=["POST"])
def sair():
    session.clear()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
