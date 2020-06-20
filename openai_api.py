import requests
import yaml
import json


def gpt3_generate(prompt: str) -> None:
    """
    Generates texts via GPT-3 and saves them to a file.
    """
    with open("config.yml", "r", encoding="utf-8") as f:
        c = yaml.safe_load(f)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {c['SECRET_KEY']}",
    }

    data = {
        "prompt": prompt,
        "max_tokens": c["max_tokens"],
        "temperature": c["temperature"],
    }

    r = requests.post(
        f"https://api.openai.com/v1/engines/{c['model']}/completions",
        headers=headers,
        data=json.dumps(data),
    )

    gen_text = r.json()["choices"][0]["text"]

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(gen_text)


if __name__ == "__main__":
    gpt3_generate("Once upon a time")
