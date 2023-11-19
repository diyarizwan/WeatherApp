# Weather App
import requests
import json
def find_weather():
    api_key = "9b68b57f19b671079cffcabf46c00547"
    city = input("Enter city name: \n")

    # Find coordinates
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

    try :
        response = requests.get(url)
    except:
        print("Could not find the result")

    if response.status_code == 200:
        result = json.loads(response.text)[0]
        lat = result.get("lat")
        lon = result.get("lon")

    # Find weather
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    try :
        response = requests.get(weather_url)
    except:
        print("Could not find the result")

    if response.status_code == 200:
        result = json.loads(response.text)
        main = result.get("main")
        for item in main.keys():
            print(item.upper())
            if item != "pressure" and item != "humidity":
                # convert from kelvin to centigrade
                print(round(main.get(item) - 273))
            else:
                print(round(main.get(item)))


if __name__ == '__main__':
    find_weather()


