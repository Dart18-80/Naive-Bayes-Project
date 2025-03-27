from flask import Flask, request, render_template
from model.preprocess import preprocess
from model.naive_bayes import NaiveBayesClassifier

app = Flask(__name__)
model = NaiveBayesClassifier.load("model/trained_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    input_text = ""
    result_message = ""

    if request.method == "POST":
        input_text = request.form["text"]
        tokens = preprocess(input_text)
        prediction = model.predict(tokens)

        # Mensajes personalizados
        messages = {
            "CG": "✅ La reseña parece genuina. ¡Gracias por compartir una opinión auténtica!",
            "OR": "⚠️ Esta reseña podría ser falsa. Procede con precaución."
        }
        result_message = messages.get(prediction, "Resultado desconocido.")

    return render_template("index.html", prediction=prediction, result_message=result_message, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)