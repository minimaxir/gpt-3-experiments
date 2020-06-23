import yaml
import json
import logging
import os
import asyncio
import fire
import httpx
import time
from tqdm import trange

logger = logging.getLogger("gpt3-experiments")
logger.setLevel(logging.INFO)

logging.basicConfig(
    format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)


def gpt3_query(headers: dict, data: str, model: str) -> str:
    r = httpx.post(
        f"https://api.openai.com/v1/engines/{model}/completions",
        headers=headers,
        data=data,
        timeout=None,
    )
    r_json = r.json()
    if "choices" not in r_json:
        return ""
    return r_json["choices"][0]["text"]


async def gpt3_query_async(headers: dict, data: str, model: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"https://api.openai.com/v1/engines/{model}/completions",
            headers=headers,
            data=data,
            timeout=None,
        )
    r_json = r.json()
    if "choices" not in r_json:
        return ""
    return r_json["choices"][0]["text"]


def prompt_md(prompt: str, gen_text: str) -> str:
    lines = prompt.split("\n")
    prompt_bold = "\n".join([f"**{line}**" if line != "" else line for line in lines])

    return f"{prompt_bold}{gen_text}"


def gpt3_generate(
    prompt: str = "prompt.txt",
    config_file: str = "config.yml",
    markdown: bool = True,
    query_async: bool = False,
) -> None:
    """
    Generates texts via GPT-3 and saves them to a file.
    """
    with open(config_file, "r", encoding="utf-8") as f:
        c = yaml.safe_load(f)

    # If prompt is a file path, load the file as the prompt.
    if os.path.exists(prompt):
        logger.info(f"Loading prompt from {prompt}.")
        with open(prompt, "r", encoding="utf-8") as f:
            prompt = f.read()
    else:
        logger.info(f"GPT-3 Model Prompt: {prompt}.")

    extension = "md" if markdown else "txt"
    sample_delim = "\n---\n" if markdown else ("=" * 20)

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
        data.update({"temperature": temp})

        n = c["num_generate"] if temp != 0.0 else 1
        n_str = "samples" if n > 1 else "sample"
        output_file = f"output_{str(temp).replace('.', '_')}.{extension}"
        logger.info(f"Writing {n} {n_str} at temperature {temp} to {output_file}.")

        if query_async:
            tasks = [
                gpt3_query_async(headers, json.dumps(data), c["model"])
                for _ in range(n)
            ]
            gen_texts = loop.run_until_complete(asyncio.gather(*tasks))
        else:
            gen_texts = []
            for _ in trange(n):
                gen_texts.append(gpt3_query(headers, json.dumps(data), c["model"]))
                time.sleep(30)

        with open(output_file, "w", encoding="utf-8") as f:
            for gen_text in gen_texts:
                if gen_text:
                    gen_text = prompt_md(prompt, gen_text) if markdown else gen_text
                    f.write("{}\n{}\n".format(gen_text, sample_delim))

    loop.close()


if __name__ == "__main__":
    fire.Fire(gpt3_generate)
