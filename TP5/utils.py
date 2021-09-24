import requests


def getPaises() -> list:
    PAISES = []
    response = requests.get("https://api.covid19api.com/countries")
    if response.status_code == 200:
        for pais in response.json():
            PAISES.append(pais["Slug"])
    PAISES.sort()
    return PAISES