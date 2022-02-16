from array import array
import os
from PIL import Image
import sys
import time
import dotenv
import requests

dotenv.load_dotenv()

# Add your Computer Vision subscription key to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# Add your Computer Vision endpoint to your environment variables.
if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

# https://{endpoint}/vision/v2.0/ocr[?language][&detectOrientation]

OCR_URL = f'{endpoint}/vision/v2.0/ocr'

def azureOCR(imgData) -> dict:
  header = {
    "Content-Type": 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
  }
  response = requests.post(OCR_URL, headers=header, data=imgData)
  if response.ok:
    return response.json()
  else:
    return {}

# body = {
#   "url": 'https://tesseract.projectnaptha.com/img/eng_bw.png'
# }

# img = requests.get('https://tesseract.projectnaptha.com/img/eng_bw.png').content
# print(img)

# header = {
#   "Content-Type": 'application/octet-stream',
#   'Ocp-Apim-Subscription-Key': subscription_key
# }

# print(requests.post(OCR_URL, headers=header, data=img).content)
