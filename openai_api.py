import yaml
import json
import logging
import os
import asyncio
import fire
from httpx import AsyncClient

logger = logging.getLogger("gpt3-experiments")
logger.setLevel(logging.INFO)

logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)


async def gpt3_query(headers: dict, data: str, model: str) -> str:
    async with AsyncClient() as client:
        r = await client.post(
            f"https://api.openai.com/v1/engines/{model}/completions",
            headers=headers,
            data=data,
            timeout=None,
        )
    return r.json()["choices"][0]["text"]


def gpt3_generate(prompt: str = "prompt.txt", config_file: str = "config.yml",) -> None:
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

    loop = asyncio.get_event_loop()

    for temp in c["temperatures"]:
        n = c["num_generate"] if temp != 0.0 else 1
        output_file = f"output_{str(temp).replace('.', '_')}.txt"
        logger.info(f"Writing {n} samples at temperature {temp} to {output_file}.")
        data.update({"temperature": temp})

        with open(output_file, "w", encoding="utf-8") as f:
            tasks = [
                gpt3_query(headers, json.dumps(data), c["model"]) for _ in range(n)
            ]

            gen_texts = loop.run_until_complete(asyncio.gather(*tasks))
            for gen_text in gen_texts:
                f.write("{}\n{}".format(gen_text, "=" * 20 + "\n"))

    loop.close()


if __name__ == "__main__":
    fire.Fire(gpt3_generate)
