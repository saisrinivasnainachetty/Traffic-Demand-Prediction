import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# Reproducibility
# -----------------------------

np.random.seed(42)
random.seed(42)

ROWS = 120000

print("Generating Traffic Dataset...")

# -----------------------------
# Possible Values
# -----------------------------

locations = [
    "Downtown",
    "Airport",
    "Railway Station",
    "Residential Area",
    "Industrial Area",
    "Shopping Mall",
    "University",
    "Hospital",
    "Bus Stand",
    "IT Park"
]

road_types = [
    "Highway",
    "Main Road",
    "Street",
    "Bridge",
    "Junction"
]

weather_conditions = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Foggy"
]

landmarks = [
    "Mall",
    "School",
    "Hospital",
    "Metro",
    "Office",
    "Park",
    "Market"
]

# -----------------------------
# Date Range
# -----------------------------

start_date = datetime(2024, 1, 1)

records = []

# -----------------------------
# Generate Records
# -----------------------------

for i in range(ROWS):

    random_days = random.randint(0, 365)

    current_date = start_date + timedelta(days=random_days)

    hour = random.randint(0, 23)

    timestamp = current_date.replace(
        hour=hour,
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )

    day_of_week = timestamp.strftime("%A")

    location = random.choice(locations)

    road_type = random.choice(road_types)

    weather = np.random.choice(
    weather_conditions,
    p=[0.55, 0.20, 0.20, 0.05]
)

    landmark = random.choice(landmarks)

    lanes = random.randint(2, 6)

    traffic_signals = random.randint(0, 8)

    large_vehicles = random.randint(0, 30)

    event = np.random.choice(
    ["Yes", "No"],
    p=[0.08, 0.92]
)

    temperature = round(np.random.normal(30, 6), 1)

    humidity = random.randint(35, 95)

    rainfall = 0

    if weather == "Rainy":

        rainfall = round(random.uniform(5, 60), 1)

    elif weather == "Cloudy":

        rainfall = round(random.uniform(0, 8), 1)

    traffic_density = random.randint(15, 100)

    # ---------------------------------
# Traffic Demand Calculation
# ---------------------------------

    traffic_score = traffic_density

    # Peak hours
    if hour in [7, 8, 9, 17, 18, 19]:
        traffic_score += 30

    # Weekend effect
    if day_of_week in ["Saturday", "Sunday"]:
        traffic_score -= 15

    # Weather impact
    if weather == "Rainy":
        traffic_score += 20

    elif weather == "Cloudy":
        traffic_score += 8

    # Events
    if event == "Yes":
        traffic_score += 25

    # Heavy vehicles
    traffic_score += large_vehicles * 0.8

    # Number of signals
    traffic_score += traffic_signals * 2

    # Road type

    if road_type == "Highway":
        traffic_score += 18

    elif road_type == "Urban":
        traffic_score += 12

    elif road_type == "Residential":
        traffic_score -= 5

    # Temperature effect

    if temperature > 38:
        traffic_score -= 5

    # Small random variation
    traffic_score += random.randint(-8, 8)

    # ---------------------------------
    # Convert Score into Category
    # ---------------------------------

    if traffic_score >= 120:
        traffic_demand = "Very High"

    elif traffic_score >= 90:
        traffic_demand = "High"

    elif traffic_score >= 60:
        traffic_demand = "Medium"

    else:
        traffic_demand = "Low"

    records.append({

        "timestamp": timestamp,

        "day_of_week": day_of_week,

        "hour": hour,

        "location": location,

        "road_type": road_type,

        "weather": weather,

        "temperature": temperature,

        "humidity": humidity,

        "rainfall": rainfall,

        "traffic_signals": traffic_signals,

        "lanes": lanes,

        "large_vehicles": large_vehicles,

        "landmark": landmark,

        "event": event,

        "traffic_density": traffic_density,

        "traffic_demand": traffic_demand

    })

df = pd.DataFrame(records)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(BASE_DIR, "dataset", "traffic_data.csv")

df.to_csv(output_path, index=False)
print("Dataset Generated Successfully!")

print(df.head())