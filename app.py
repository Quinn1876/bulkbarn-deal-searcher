from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import re
import cv2
import pytesseract
import numpy as np
import azureApi

from pprint import pprint

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

@app.route('/')
def hello_world():
  response = requests.get('https://www.bulkbarn.ca/en/Deals/Ontario')
  soup = BeautifulSoup(response.content, 'html.parser')
  imgUrls = []

  for img in soup.find_all('img'):
    imgUrls.append(img.get('src'))

  for imgUrl in filter(lambda imgURL: re.search(r"[a-zA-Z0-9/._-]*Weekly-Specials[a-zA-Z0-9/_.-]*", imgURL) != None, imgUrls):
    response = requests.get('https://www.bulkbarn.ca' + imgUrl)
    img = response.content
    imgByteData = BytesIO(img)
    Image.open(imgByteData).show()
    azureResponse = azureApi.azureOCR(img)
    return jsonify(azureResponse)
  return 'Success'

app.run()
