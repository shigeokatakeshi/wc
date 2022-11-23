# import json
import requests
# from PIL import Image


def cat():
    url = 
    res = requests.get(url)
    response = json.loads(res.text)[0]["url"]
    return response


def dog():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    response = json.loads(res.text)["message"]
    return response


def fox():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    response = json.loads(res.text)["message"]
    return response