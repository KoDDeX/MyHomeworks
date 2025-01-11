'''
HomeWork # 27.
Создание асинхронного клиента для работы с API VseGPT.
'''

import asyncio
import openai
import csv

def loadConfig (fName: str) -> str:
    with open(fName, 'r') as file:
        reader = csv.DictReader(file, delimiter=':')
        for row in reader:
            return row['api_key']

API_KEY = loadConfig('HW_27\config.csv')