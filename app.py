from flask import Flask, render_template, request
from google_trans_new import google_translator

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")
    

@app.route("/predict_sentence",methods=["POST","GET"])
def predict_sentence():
    return google_translator().translate(request.form.get("sentence"),lang_tgt='en')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)