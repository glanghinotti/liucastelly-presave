from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# URL da sua implantação do Google Sheets
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwPcMC0BfvGLvjHut0QorbDDxrVWMQOXs61icB7m300aDHnW-2ENanefkvziHrwsIpz6Q/exec"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            # Envia o e-mail para a sua Planilha Google em tempo real
            try:
                requests.post(GOOGLE_SCRIPT_URL, json={"email": email}, timeout=5)
            except:
                # Se houver erro na conexão com o Google, o site continua funcionando
                pass 
                
            return redirect(url_for("obrigado"))
            
    return render_template("index.html")

@app.route("/obrigado")
def obrigado():
    return render_template("obrigado.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

