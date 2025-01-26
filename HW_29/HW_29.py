"""
Домашнее задание №29
Рефакторинг кода для сжатия изображений с использованием принципов ООП.
"""
import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

QUALITY = 50

class ImageCompressor:
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
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
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
        pass

