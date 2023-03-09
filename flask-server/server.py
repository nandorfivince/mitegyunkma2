from flask import Flask, request
from datetime import datetime
import random
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Console API Route
@app.route("/console", methods=["POST"])
def console():
    text = request.data.decode('utf-8')
    print(text)
    return text

@app.route("/current-date")
def get_current_date():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")  # YYYY-MM-DD formátumban adja vissza a dátumot
    return date

@app.route("/current-time")
def get_current_time():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")  # ÓÓ:PP:MM formátumban adja vissza az időt
    return time

# Endpoint for menu items
@app.route("/menu")
def get_menu():
    df = pd.read_excel('resources/input.xlsx')
    leves = df['Leves'].tolist()
    foetel = df['Főétel'].tolist()
    desszert = df['Desszert'].tolist()
    random_leves = random.choice(leves)
    random_foetel = random.choice(foetel)
    random_desszert = random.choice(desszert)
    return {
        "random_leves": random_leves,
        "random_foetel": random_foetel,
        "random_desszert": random_desszert,
    }

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
