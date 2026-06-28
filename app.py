from flask import Flask, render_template, request
from prediction import predict_traffic

app = Flask(__name__)


# ---------------------------------
# Home Page
# ---------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------
# Prediction Page
# ---------------------------------
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        prediction = predict_traffic(

            day_of_week=request.form["day_of_week"],
            hour=int(request.form["hour"]),
            location=request.form["location"],
            road_type=request.form["road_type"],
            weather=request.form["weather"],
            temperature=float(request.form["temperature"]),
            humidity=int(request.form["humidity"]),
            rainfall=float(request.form["rainfall"]),
            traffic_signals=int(request.form["traffic_signals"]),
            lanes=int(request.form["lanes"]),
            large_vehicles=int(request.form["large_vehicles"]),
            landmark=request.form["landmark"],
            event=request.form["event"],
            traffic_density=int(request.form["traffic_density"])

        )

        # ----------------------------
        # Result Styling
        # ----------------------------
        if prediction == "Low":
            color = "success"
            message = "Traffic is smooth. Roads are clear."

        elif prediction == "Medium":
            color = "warning"
            message = "Moderate traffic. Expect slight delays."

        elif prediction == "High":
            color = "danger"
            message = "Heavy traffic detected. Plan your route carefully."

        else:
            color = "dark"
            message = "Very High traffic. Avoid this route if possible."

        return render_template(
            "result.html",
            prediction=prediction,
            color=color,
            message=message
        )

    return render_template("predict.html")


# ---------------------------------
# About Page
# ---------------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# ---------------------------------
# Dashboard Page
# ---------------------------------
import pandas as pd

@app.route("/dashboard")
def dashboard():

    df = pd.read_csv("dataset/traffic_data.csv")

    total_records = len(df)

    avg_temperature = round(df["temperature"].mean(),2)

    avg_density = round(df["traffic_density"].mean(),2)

    accuracy = 87.05

    traffic_counts = df["traffic_demand"].value_counts()

    return render_template(
        "dashboard.html",
        total_records=total_records,
        avg_temperature=avg_temperature,
        avg_density=avg_density,
        accuracy=accuracy,
        traffic_counts=traffic_counts
    )

# ---------------------------------
# Contact Section
# ---------------------------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------------------------
# Run Application
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)