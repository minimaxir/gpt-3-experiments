import requests
import yaml
import json
import logging
import os
from tqdm.auto import trange

logger = logging.getLogger("gpt3-experiments")
logger.setLevel(logging.INFO)

logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)


def gpt3_generate(prompt: str, config_file: str = "config.yml",) -> None:
    """
    Generates texts via GPT-3 and saves them to a file.
    """
    with open("config.yml", "r", encoding="utf-8") as f:
        c = yaml.safe_load(f)

    # If prompt is a file path, load the file as the prompt.
    if os.path.exists(prompt):
        with open(prompt, "r", encoding="utf-8") as f:
            prompt = f.read()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {c['SECRET_KEY']}",
    }

    data = {
        "prompt": prompt,
        "max_tokens": c["max_tokens"],
    }

    for temp in c["temperatures"]:
        n = c["num_generate"] if temp != 0.0 else 1
        output_file = f"output_{str(temp).replace('.', '_')}.txt"
        logger.info(f"Writing {n} samples at temperature {temp} to {output_file}.")
        data.update({"temperature": temp})

        with open(output_file, "w", encoding="utf-8") as f:
            for _ in trange(n):
                r = requests.post(
                    f"https://api.openai.com/v1/engines/{c['model']}/completions",
                    headers=headers,
                    data=json.dumps(data),
                )

                gen_text = r.json()["choices"][0]["text"]
                f.write("{}\n{}".format(gen_text, "=" * 20 + "\n"))


if __name__ == "__main__":
    gpt3_generate("prompt.txt")
