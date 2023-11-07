from flask import Flask, redirect, url_for,render_template, request,flash
app = Flask(__name__)

@app.route('/')
def connexion():
    return render_template("connexion.html")

@app.route('/accueil')
def accueil():
    return render_template('acceuil.html')



if __name__ == "__main__":  # Pour que la methode créée puisse s'éxécutée
    app.run(debug=True)