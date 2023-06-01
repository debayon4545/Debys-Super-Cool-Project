from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        return None
    print(data)
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]


    return {
        "temperature": temperature,
        "humidity": humidity,
        "description": description
    }

@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form["city"]
        api_key = "4743f6f6ac6d1f9f395357138d3d8b32"  

        weather_data = get_weather(api_key, city)
        if weather_data is None:
            error_message = "City not found."
            return render_template("weather.html", error_message=error_message)

        return render_template("weather.html", weather_data=weather_data)

    return render_template("weather.html")

if __name__ == "__main__":
    app.run()
