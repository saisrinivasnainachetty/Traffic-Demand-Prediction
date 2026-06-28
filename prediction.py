import os
import joblib
import pandas as pd

# --------------------------------
# Load Model
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "saved_models",
    "lightgbm_model.pkl"
)

model = joblib.load(MODEL_PATH)

# --------------------------------
# Encoding Dictionaries
# --------------------------------

day_encoder = {
    "Monday":0,
    "Tuesday":1,
    "Wednesday":2,
    "Thursday":3,
    "Friday":4,
    "Saturday":5,
    "Sunday":6
}

road_encoder = {
    "Bridge":0,
    "Highway":1,
    "Junction":2,
    "Main Road":3,
    "Street":4
}

weather_encoder = {
    "Sunny":0,
    "Cloudy":1,
    "Rainy":2,
    "Foggy":3
}

event_encoder = {
    "No":0,
    "Yes":1
}

location_encoder = {
    "Airport":0,
    "Bus Stand":1,
    "Downtown":2,
    "Hospital":3,
    "IT Park":4,
    "Industrial Area":5,
    "Railway Station":6,
    "Residential Area":7,
    "Shopping Mall":8,
    "University":9
}

landmark_encoder = {
    "Hospital":0,
    "Mall":1,
    "Market":2,
    "Metro":3,
    "Office":4,
    "Park":5,
    "School":6
}

traffic_decoder = {
    0:"High",
    1:"Low",
    2:"Medium",
    3:"Very High"
}

# --------------------------------
# Prediction Function
# --------------------------------

def predict_traffic(
    day_of_week,
    hour,
    location,
    road_type,
    weather,
    temperature,
    humidity,
    rainfall,
    traffic_signals,
    lanes,
    large_vehicles,
    landmark,
    event,
    traffic_density
):

    input_data = pd.DataFrame([{

        "day_of_week": day_encoder[day_of_week],

        "hour": hour,

        "location": location_encoder[location],

        "road_type": road_encoder[road_type],

        "weather": weather_encoder[weather],

        "temperature": temperature,

        "humidity": humidity,

        "rainfall": rainfall,

        "traffic_signals": traffic_signals,

        "lanes": lanes,

        "large_vehicles": large_vehicles,

        "landmark": landmark_encoder[landmark],

        "event": event_encoder[event],

        "traffic_density": traffic_density

    }])

    prediction = model.predict(input_data)[0]

    return traffic_decoder[prediction]

