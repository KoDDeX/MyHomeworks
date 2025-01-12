"""
HomeWork # 27.
Создание асинхронного клиента для работы с API VseGPT.
"""

import asyncio
from openai import AsyncOpenAI, RateLimitError
import csv


def loadConfig(fName: str) -> str:
    with open(fName, "r") as file:
        reader = csv.DictReader(file, delimiter=":")
        for row in reader:
            return row["api_key"]


API_KEY = loadConfig("HW_27\config.csv")

BASE_URL = "https://api.vsegpt.ru/v1"
MAX_CHUNK_SIZE = 2000  # Максимальная длина текста для 1 запроса к API
SLEEP_TIME = 1  # Задержка между запросами

client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)

# async def get_ai_request(prompt: str, model: str = "openai/gpt-4o-mini", max_tokens: int = 16000, temperature: float = 0.7) -> str:
#     response = await client.chat.completions.create(
#         model=model,
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=max_tokens,
#         temperature=temperature,
#     )
#     return response.choices[0].message.content


async def get_ai_request(prompt: str, max_retries: int = 3, base_delay: float = 2.0):
    """
    Отправляет запрос к API с механизмом повторных попыток
    base_delay - начальная задержка, которая будет увеличиваться экспоненциально
    """
    for attempt in range(max_retries):
        try:
            response = await client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=16000,
                temperature=0.7,
            )
            return response.choices[0].message.content

        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2**attempt)  # Экспоненциальное увеличение задержки
            await asyncio.sleep(delay)


async def main():
    prompt_cow = "Как кричит корова?"
    prompt_cat = "Как кричит кошка?"
    prompt_monkey = "Как кричит обезьяна?"

    prompts = [prompt_cow, prompt_cat, prompt_monkey]
    results = await asyncio.gather(*[get_ai_request(prompt) for prompt in prompts])

    print(results)


asyncio.run(main())
