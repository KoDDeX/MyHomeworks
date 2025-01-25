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
        pass
    def process_directory(self, directory: str) -> None:
        """
        Метод для обработки всех изображений в указанной директории и её поддиректориях
        :param directory: str - путь к директории
        :return: None
        """
        pass
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

