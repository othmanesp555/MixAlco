import requests
import json

url = "https://the-cocktail-db.p.rapidapi.com/filter.php"
print("input an ingredient")
alco = input()
querystring = {"i":alco}

headers = {
	"X-RapidAPI-Key": "Your-RapidAPI-Key",
	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
u = response.json()
i = 0
b = u["drinks"][i]["strDrink"]
for strDrink in u["drinks"]:
              print(strDrink)