import requests
cidade = input("digite o nome da cidade")
# 1. Localiazr a cidade
url_geocoding = "https://geocoding-api.open-meteo.com/v1/search"

parametros_geocoding = {
    "name": cidade,
    "count": 1,
    "language": "pt",
    "format": "json"
}
resposta = requests.get(
    url_geocoding,
    params=parametros_geocoding,
    timeout=10
)
dados = resposta.json()

resultado = dados["results"][0]

nome = resultado["name"]
latitude = resultado["latitude"]
longitude = resultado["longitude"]

# 2.Consultar clima
url_clima = "https://api.open-meteo.com/v1/forecast"

parametros_clima = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m",
    "timezone": "America/Sao_Paulo"
}
resposta_clima = requests.get(
    url_clima,
    params=parametros_clima,
    timeout=10
)

dados_clima = resposta_clima.json()

clima_atual = dados_clima["current"]

temperatura = clima_atual["temperature_2m"]
sensacao = clima_atual["apparent_temperature"]
umidade = clima_atual["relative_humidity_2m"]
vento = clima_atual["wind_speed_10m"]

# 3. Mostrar resultado
print()
print("==========================")
print("    MONITOR DE CLIMA")
print("==========================")
print(f"  Cidade: {nome}")
print(f"  Temperatura: {temperatura} °C")
print(f"  Sensação termica: {sensacao} °C")
print(f"  Umidade: {umidade} %")
print(f"  Vento: {vento} km/h")
print("===============================")


# resposta = requests.get(url, params=parametros, timeout=10)

# dados = resposta.json()
# resultado = dados["results"][0]

# nome = resultado["name"]
# latitude = resultado["latitude"]
# longitude = resultado["longitude"]
# estado = resultado["admin1"]
# pais = resultado["country"]

# print("===========================")
# print("        MONITOR DE CLIMA         ")
# print("===========================")
# print(f"Cidade; {nome}")
# print(f"estado: {estado}")
# print(f"País: {pais}")
# print(f"Latitude: {latitude}")
# print(f"Longitude: {longitude}")
# print("===========================")
