import nltk
import joblib
palavrasunicas = joblib.load("palavrasunicas.pkl")
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')



def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

def aplicastemmer(texto):
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavrasteste) in texto.split():
        comstem = [p for p in palavrasteste.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))
    return testestemming

