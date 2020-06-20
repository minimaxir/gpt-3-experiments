import requests
import yaml
import json

with open("config.yml", "r") as f:
    c = yaml.safe_load(f)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {c['SECRET_KEY']}",
}

data = {
    "prompt": "Once upon a time",
    "max_tokens": c["max_tokens"],
    "temperature": c["temperature"],
}

r = requests.post(
    f"https://api.openai.com/v1/engines/{c['model']}/completions",
    headers=headers,
    data=json.dumps(data),
)

gen_text = r.json()["choices"][0]["text"]
print(gen_text)
