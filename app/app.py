from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Emission factors (kg CO₂ per unit)
EMISSION_FACTORS = {
    "transportation": 2.5,  # kg CO₂ per kWh
    "meal": 25,    # kg CO₂ per liter
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    # Distance calculation
    distance_option = request.form["distance"]
    if distance_option == "other":
        km = float(request.form["custom_distance"])
    else:
        km = float(distance_option)
    
    # Vegetarian meal calculation
    meals_option = request.form["vegetarian_meals"]
    if meals_option == "other":
        meals = int(request.form["custom_meals"])
    else:
        meals = int(meals_option)
    
    # Calculate savings
    saved_emissions_from_transport = (km / 10) * EMISSION_FACTORS["transportation"] # kg CO₂ saved by walking, biking, or public transport
    saved_emissions_from_meals = meals * EMISSION_FACTORS["meal"]  # kg CO₂ saved from vegetarian meals

    total_saved = saved_emissions_from_transport + saved_emissions_from_meals

    return render_template("result.html", saved=total_saved)
# def calculate():
#     electricity = float(request.form["electricity"]) * EMISSION_FACTORS["electricity"]
#     gasoline = float(request.form["gasoline"]) * EMISSION_FACTORS["gasoline"]

#     total_emissions = electricity + gasoline

#     return render_template("result.html", total=total_emissions)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=False, host="0.0.0.0", port=port)
if __name__ == "__main__":
    app.run(debug=True)



#Intenta pedirle una app en Python con FastAPI, Bootstrap para el styling y el UI y HTML templates con jinja.