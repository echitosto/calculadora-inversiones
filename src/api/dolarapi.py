#!/usr/bin/env python3
import requests
import json

BASE_URL = "https://dolarapi.com/v1/dolares"

def get_mep():
    response = requests.get(BASE_URL + "/bolsa")
    return json.loads(response.text)["venta"]

def get_blue():
    response = requests.get(BASE_URL + "/blue")
    return json.loads(response.text)["venta"]