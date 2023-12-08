import requests
import datetime
from utils.translate import to_latin
from config import OPENWEATHER_API_KEY

emoji_codes = {
    "Clear": "🌞 Quyoshli havo",
    "Clouds": "☁️ Bulutli havo",
    "Rain": "🌧️ Yomg'irli havo",
    "Drizzle": "🌧️ Yomg'irli havo",
    "Thunderstorm": "⚡ Chaqmoq",
    "Snow": "❄️ Qor",
    "Mist": "🌫️ Tuman"
}

def get_info(text):
    if text.isascii() is False:
        text = to_latin(text)
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={text}&appid={OPENWEATHER_API_KEY}&units=metric"
        )
        data = r.json()

        city = data["name"]
        temp = data["main"]["temp"]

        emoji = data["weather"][0]["main"]
        if emoji in emoji_codes:
            sm = emoji_codes[emoji]
        else:
            sm = "Bu yerdan ko'rinmayabdi :)"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        day_length = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        result = (f"<b>Xozirgi Vaqt Bo'yicha ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})\n\n"
                f"{city} Shahar ob-havosi!\nHarorat: {temp}°C  {sm}\n"
                f"Namlik: {humidity}%\nBosim: {pressure} mm sim. ust\nShamol: {speed} m/s\n"
                f"Quyosh Chiqishi: {sunrise}\nQuyosh Botishi: {sunset}\nKunning Uzunligi: {day_length}\n"
                f"\nSalomat bo'ling! 😊</b>")

        return result

    except:
        return "Ma\'lumot topilmadi"
