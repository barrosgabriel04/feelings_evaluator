from flask import Flask, render_template, request
import joblib
import nltk
from auxilio import aplicastemmer, extratorpalavras
classificador = joblib.load("modelo_sentimentos.pkl")
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
palavrasunicas = joblib.load("palavrasunicas.pkl")
app = Flask(__name__)

@app.route("/")
def pag():
    return render_template("index.html")

@app.route("/classificacao", methods=['POST'])
def processar_dados():
    texto = request.form['texto']
    frase = aplicastemmer(texto)
    palavras = extratorpalavras(frase)
    classificaca = classificador.classify(palavras)
    return render_template("index.html", classificacao=classificaca )
if __name__ == "__main__":
    app.run(debug=True)

