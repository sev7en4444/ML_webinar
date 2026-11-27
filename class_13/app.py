from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("fare_model.pkl")      # loaded once at startup

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    ride = pd.DataFrame([{
        "distance_m":  float(data["distance_m"]),
        "vehicle":     data["vehicle"],
        "mode":        data["mode"],
        "time_of_day": data["time_of_day"],
        "people":      int(data["people"]),
        "bags":        int(data["bags"]),
        "is_tourist":  data["is_tourist"],
    }])
    fare = model.predict(ride)[0]
    fare = max(round(fare), 0)              # a fare can't be negative
    return render_template("index.html", fare=fare)

if __name__ == "__main__":
    app.run(debug=True)