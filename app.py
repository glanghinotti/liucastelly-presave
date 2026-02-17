from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

LAUNCH_DATE = datetime(2026, 3, 6)
EMAIL_FILE = "emails.txt"

def save_email(email):
    emails = set()
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, "r") as f:
            emails = set(line.strip() for line in f)
    
    if email not in emails:
        with open(EMAIL_FILE, "a") as f:
            f.write(email + "\n")
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            save_email(email)
            # Agora redireciona para a função correta
            return redirect(url_for("obrigado"))
            
    return render_template("index.html", launch_date=LAUNCH_DATE)

@app.route("/obrigado")
def obrigado():
    # Agora abre o arquivo que você já tem na pasta templates
    return render_template("obrigado.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
