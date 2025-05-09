import requests
import json
import pyttsx3

if __name__=='__main__':
    engine = pyttsx3.init()
    engine.say("welcome to weather app")
    engine.runAndWait()
    engine.say("Enter City Name: ")
    engine.runAndWait()
    city=input("Enter City Name: ")
    url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

    r=requests.get(url)
    # print(r.text)
    wdict=json.loads(r.text)
    engine.say(wdict["location"]["name"])
    engine.runAndWait()
    print(wdict["location"]["name"])
    engine.say(wdict["location"]["region"])
    engine.runAndWait()
    print(wdict["location"]["region"])
    engine.say(wdict["location"]["country"])
    engine.runAndWait()
    print(wdict["location"]["country"])
    engine.say(wdict["current"]["temp_c"])
    engine.runAndWait()
    print(wdict["current"]["temp_c"])
    engine.say(wdict["current"]["wind_kph"])
    engine.runAndWait()
    print(wdict["current"]["wind_kph"])
    engine.say(wdict["current"]["humidity"])
    engine.runAndWait()
    print(wdict["current"]["humidity"])