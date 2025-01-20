"""
HomeWork # 27.
Создание асинхронного клиента для работы с API VseGPT.
"""
import csv
import asyncio
import json
from openai import AsyncOpenAI, RateLimitError
from hw_27_data import DATA

def loadConfig(fName: str) -> str:
    with open(fName, "r") as file:
        reader = csv.DictReader(file, delimiter=":")
        for row in reader:
            return row["api_key"]


API_KEY = loadConfig("HW_27\config.csv")
# API_KEY = ''

BASE_URL = "https://api.vsegpt.ru/v1"
MAX_CHUNK_SIZE = 3000  # Максимальная длина текста для 1 запроса к API
SLEEP_TIME = 1  # Задержка между запросами
OUTPUT_FILE = "output_file.md"

PROMPT_THEME = """
Привет!

Определи общую тему  текста. И постарайся максимально полно и точно описать её,
с использованием пунктов и подпунктов.

Не додумывай того, чего там небыло.
Исключи small talks.
"""

PROMPT_TIMESTAMPS = """
Привет!

Ты - ассистент по созданию таймкодов для видео.
Тебе будет предоставлен текст с таймкодами из видео.
Твоя задача - создать краткое описание каждого смыслового блока.
Ты не должен использовать полное цитирование. Создай краткое описание для блока.
Каждый блок должен начинаться с таймкода в формате чч:мм:сс.
Описание должно быть одним предложением, передающим суть начинающегося отрезка.
Игнорируй слишком короткие фрагменты или паузы.
Объединяй связанные по смыслу части в один большой блок.
Описания должны быть в стиле, как это обычно делают на youtube.

ВАЖНО.
СТРОГИЕ ПРАВИЛА:
1. Для видео длительностью:
   - до 30 минут: максимум 5 таймкодов
   - 30-60 минут: максимум 8 таймкодов
   - 1-2 часа: максимум 10 таймкодов
   - 2+ часа: максимум 15 таймкодов

2. Минимальный интервал между таймкодами:
   - для коротких видео (до 30 мин): 3-5 минут
   - для длинных видео: 10-15 минут

3. Объединяй близкие по смыслу темы в один таймкод

ВАЖНО: Если ты превысишь количество таймкодов - твой ответ будет отклонён!

В твоём ответе должны быть только таймкоды и описания.
Никаких других комментариев или пояснений.

КАК ПИСАТЬ?

Ты не пишешь описательные, длинные предложения. 
Вроде: "Пояснение адаптивного подхода к верстке на примере Visual Studio Code, где контент перестраивается в зависимости от размера экрана. "

Ты пишешь короткий, ёмкий вариант.
"Адаптивный подход к вёрстке. Пример в Visual Studio Code. Контент перестраивается в зависимости от размера экрана."
Или даже ещё немного короче.

Спасибо!
"""

PROMPT_CONSPECT_WRITER = """
Привет!
Ты опытный технический писатель. Ниже, я предоставляю тебе полный текст лекции а так же ту часть,
с которой ты будешь работать.

Ты великолепно знаешь русский язык и отлично владеешь этой темой.

Тема занятия: {topic}

Полный текст лекции:
{full_text}

Сейчас я дам тебе ту часть, с котороый ты будешь работать. Я попрошу тебя написать конспект лекции.
А так же блоки кода.

Ты пишешь в формате Markdown. Начни с заголовка 2го уровня.
В тексте используй заголовки 3го уровня.

Используй блоки кода по необходимости.

Отрезок текста с которым ты работаешь, с которого ты будешь работать:
{text_to_work}
"""


client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)


def seconds_to_timecode(seconds: float) -> str:
    """ Конвертация секунд в таймкоды"""
    if seconds is None:
        return "00:00:00"
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = int(seconds % 60)
    return f'{hours:02d}:{minutes:02d}:{sec:02d}'

def add_timestamp_text(data: list[dict]) -> list[dict]:
    """ Добавляет в словарь ключ timestamp_text"""
    for item in data:
        start_time = seconds_to_timecode(item["timestamp"][0])
        end_time = seconds_to_timecode(item["timestamp"][1])
        item["timestamp_text"] = [start_time, end_time]
    return data

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

def split_text_to_chunks(data: list) -> list:
    """Делит текст на чанки размером не более MAX_CHUNK_SIZE"""
    chunks = []
    current_chunk = ""
    for item in data:
        text = item["text"]
        if len(current_chunk) + len(text) <= MAX_CHUNK_SIZE:
            current_chunk += text
        else:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = text
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def save_to_markdown(timestamps: str, theme: str, chunks: list) -> None:
    """Сохраняет результаты в markdown файле"""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Таймкоды\n\n")
        f.write(timestamps)
        f.write("\n\n---\n\n")
        f.write("# Краткое содержание\n\n")
        f.write(theme)
        f.write("\n\n---\n\n")
        f.write("# Конспект\n\n")
        for chunk in chunks:
            f.write(chunk)
            f.write("\n\n---\n\n")

async def main():
    # prompt_cow = "Как кричит корова?"
    # prompt_cat = "Как кричит кошка?"
    # prompt_monkey = "Как кричит обезьяна?"

    # prompts = [prompt_cow, prompt_cat, prompt_monkey]
    # results = await asyncio.gather(*[get_ai_request(prompt) for prompt in prompts])
    # print(results)

    full_data = add_timestamp_text(DATA)
    full_data_json_string = json.dumps(full_data)
    timestamps_task = asyncio.create_task(get_ai_request(PROMPT_TIMESTAMPS + json.dumps(full_data_json_string)))
    theme_task = asyncio.create_task(get_ai_request(PROMPT_THEME + json.dumps(full_data_json_string)))

    chunks = split_text_to_chunks(full_data)
    timestamps = await timestamps_task
    theme = await theme_task
    chunk_tasks = []
    for chunk in chunks:
        prompt = PROMPT_CONSPECT_WRITER.format(
            topic=theme,
            full_text=full_data_json_string,
            text_to_work=chunk,
        )
        task = asyncio.create_task(get_ai_request(prompt))
        chunk_tasks.append(task)
    results = await asyncio.gather(*chunk_tasks)
    save_to_markdown(timestamps, theme, results)

if __name__ == "__main__":
    asyncio.run(main())