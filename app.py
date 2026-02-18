from flask import Flask, render_template, request
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
            try:
                # Envia o e-mail para a planilha
                requests.post(GOOGLE_SCRIPT_URL, json={"email": email}, timeout=5)
                return "success", 200
            except:
                return "error", 500
    
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


