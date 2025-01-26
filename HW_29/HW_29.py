"""
Домашнее задание №29
Рефакторинг кода для сжатия изображений с использованием принципов ООП.
"""
import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    """
    Класс для сжатия изображений с использованием принципов ООП, с возможностью сжатия в формате HEIF в требуемом качестве.
    """
    __quality = 50
    supported_formats = (".jpg", ".jpeg", ".png")

    def __init__(self, quality: int):
        """
        Конструктор класса, который принимает значение качества сжатия и инициализирует атрибут `__quality`
        :param quality: int - значение качества сжатия
        """
        self.__quality = quality

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Метод для сжатия изображения и сохранения его в формате HEIF
        :param input_path: str - путь к исходному изображению
        :param output_path: str - путь для сохранения сжатого изображения в формате HEIF
        :return: None
        """
        with Image.open(input_path) as img:
            img.save(output_path, format="HEIF", quality=self.__quality)
        print(f'Сжато: {input_path} -> {output_path}')

    def process_directory(self, directory: str) -> None:
        """
        Метод для обработки всех изображений в указанной директории и её поддиректориях
        :param directory: str - путь к директории для обработки
        :return: None
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.join(root, file)
                    self.compress_image(input_path, output_path)

    @property
    def quality(self) -> int:
        """
        Метод для получения значения качества сжатия
        :return: значение качества сжатия
        """
        return self.__quality
    @quality.setter
    def quality(self, quality: int) -> None:
        """
        Метод для установки значения качества сжатия
        :param value: int - новое значение качества сжатия
        :return: None
        """
        self.__quality = quality

def main(input_path: str) -> None:
    """
    Основаня функция программы. Обрабатывает входной путь и запускает сжатие изображений.
    :param input_path: str - путь к файлу или директории для обработки.
    :return: None
    """
    register_heif_opener()
    input_path = input_path.strip('"')

    if os.path.exists(input_path):
        img_compressor = ImageCompressor(50)
        if os .path.isfile(input_path):
            # Если указан путь к файлу, обрабатываем только этот файл
            print(f'Обрабатываем файл: {input_path}')
            output_path = os.path.splitext(input_path)[0] + '.heif'
            img_compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            # Если указан путь к директории, обрабатываем все файлы в ней и её поддиректориях
            print(f'Обрабатываем директорию: {input_path}')
            img_compressor.process_directory(input_path)
    else:
        print(f'Указанный путь/файл не существует: {input_path}')

if __name__ == '__main__':
    user_input = input('Введите путь к файлу или директории для обработки: ')
    main(user_input)
    