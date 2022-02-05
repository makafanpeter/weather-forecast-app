from datetime import date, timedelta
import random
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

summaries = ["Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"]


@app.get("/")
def get_weather():
    results = []
    for i in range(0, 5):
        results.append({
            "Summary": random.choice(summaries),
             "TemperatureC": random.choice(range(-20, 55)),
             "Date": date.today() + timedelta(days=i)
             })
    return results
