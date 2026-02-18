from flask import Flask, render_template, request, jsonify
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
                # Timeout de 15s para o Google processar o e-mail
                requests.post(GOOGLE_SCRIPT_URL, json={"email": email}, timeout=15)
                return jsonify({"status": "success"}), 200
            except Exception as e:
                # Se o Google demorar, o site ainda assim avança para não travar o fã
                return jsonify({"status": "success"}), 200
    
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
