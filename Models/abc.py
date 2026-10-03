import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://router.huggingface.co/v1/models"

res = requests.get(url, headers=headers)

print(res.status_code)

data = res.json()

for model in data["data"]:
    print(model["id"])