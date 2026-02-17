from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime # Importante caso o seu HTML use a data
import requests
import os

app = Flask(__name__)

# Data do lançamento da Liu Castelly
LAUNCH_DATE = datetime(2026, 3, 6)

# URL da sua implantação do Google Sheets (O link que termina em /exec)
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwPcMC0BfvGLvjHut0QorbDDxrVWMQOXs61icB7m300aDHnW-2ENanefkvziHrwsIpz6Q/exec"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            try:
                # Envia para a planilha com um tempo limite de 5 segundos
                requests.post(GOOGLE_SCRIPT_URL, json={"email": email}, timeout=5)
            except:
                pass 
            return redirect(url_for("obrigado"))
            
    # Passamos o launch_date para evitar erros no index.html
    return render_template("index.html", launch_date=LAUNCH_DATE)

@app.route("/obrigado")
def obrigado():
    return render_template("obrigado.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

