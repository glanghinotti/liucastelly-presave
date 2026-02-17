from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

LAUNCH_DATE = datetime(2026, 3, 6)

EMAIL_FILE = "emails.txt"

def save_email(email):
    emails = set()

    # Se arquivo existir, carrega emails existentes
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, "r") as f:
            emails = set(line.strip() for line in f)

    # Se não existir ainda no arquivo, salva
    if email not in emails:
        with open(EMAIL_FILE, "a") as f:
            f.write(email + "\n")
        return True
    
    return False


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        @app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            save_email(email)
            # Corrigido para o nome da função abaixo
            return redirect(url_for("obrigado")) 
            
    return render_template("index.html", launch_date=LAUNCH_DATE)

@app.route("/obrigado")
def obrigado():
    # Em vez de redirecionar para si mesma, 
    # ela deve renderizar uma página de agradecimento.
    return render_template("obrigado.html")
