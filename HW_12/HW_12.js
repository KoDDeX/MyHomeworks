let weatherData = {
    "coord":{"lon":30.2642,"lat":59.8944},
    "weather":[{"id":800,"main":"Clear","description":"ясно","icon":"01n"}],
    "base":"stations",
    "main":{"temp":15.03,"feels_like":14.65,"temp_min":14.08,"temp_max":15.03,"pressure":1011,"humidity":79,"sea_level":1011,"grnd_level":1009},
    "visibility":10000,
    "wind":{"speed":3,"deg":150},
    "clouds":{"all":0},
    "dt":1727203506,
    "sys":{"type":2,"id":197864,"country":"RU","sunrise":1727149703,"sunset":1727193203},
    "timezone":10800,
    "id":498817,
    "name":"Санкт-Петербург",
    "cod":200};

// Функция очистки формы вывода
    function clearWeatherData() {
        document.querySelector('title').textContent = "Домашняя работа № 12";
        document.getElementById('cityName').textContent = "-";
        document.getElementById('weatherDesc').textContent = "-";
        document.getElementById('weatherTemp').textContent = "-";
        document.getElementById('feelsLike').textContent = "-";
        document.getElementById('windSpeed').textContent = "-";
        document.getElementById('humidity').textContent = "-";
        document.getElementById('date').textContent = "-";
        }

// Напишем функцию parseWeatherData(weatherData) принимающую данные о погоде и возвращающая массив с названием города, описанием погоды, температуры, ощущением температуры скорости ветра
function parseWeatherData(weatherData) {
    let cityName = weatherData.name;
    let description = weatherData.weather[0].description;
    let temperature = weatherData.main.temp;
    let feelsLike = weatherData.main.feels_like;
    let windSpeed = weatherData.wind.speed;
    let humidity = weatherData.main.humidity;
    let datetime = weatherData.dt;

    return [cityName, description, temperature, feelsLike, windSpeed, humidity, datetime];
}

// Напишем функцию renderWeatherData(weatherData) принимающую данные о погоде и выводящая результат в DOM страницы
function renderWeatherData(selectedCityName,weatherData) {
    let weatherDataParsed = parseWeatherData(weatherData);
    if (weatherDataParsed[0]==selectedCityName) {
    // Заменим заголовок страницы на наименование города
    document.querySelector('title').textContent = `Сейчас в г. ${selectedCityName}`;
    document.getElementById('cityName').textContent = selectedCityName;
    document.getElementById('weatherDesc').textContent = weatherDataParsed[1];
    document.getElementById('weatherTemp').textContent = `${Math.floor(weatherDataParsed[2])} °C`;
    document.getElementById('feelsLike').textContent = `Ощущается как ${Math.floor(weatherDataParsed[3])} °C`;
    document.getElementById('windSpeed').textContent = `${weatherDataParsed[4]} м/с`;
    document.getElementById('humidity').textContent = `${weatherDataParsed[5]}%`;
    document.getElementById('date').textContent = new Date(weatherDataParsed[6] * 1000).toDateString();
    }
    else {
        clearWeatherData();
    }
}

// Ищем select
const inputCity = document.getElementById('inputCity');
const newMetod = document.getElementById('newMetod');

// Функция добавляет города в select (пока только один город)
function setCityList(weatherData) {
    let option = document.createElement('option');
    option.value = weatherData.name;
    option.textContent = weatherData.name;
    document.querySelector('select').appendChild(option);
}

//  Слушатель на загрузку страницы
document.addEventListener('DOMContentLoaded', () => {
    // setCityList(weatherData);
    clearWeatherData();
    setInterval(() => {
        newMetod.classList.toggle('newMetod');
        console.log('newMetod');
    }, 300);
});

// Слушатель на изменение города в select
inputCity.addEventListener('input', function () {
    // выполнить вывод в консоль с задержкой в 3 секунды после ввода
    setTimeout(() => {
        if (inputCity.value === weatherData.name) {
            renderWeatherData(inputCity.value, weatherData)
        }
        else {
            clearWeatherData();
        }
    }, 2000);
    // renderWeatherData(this.options[this.selectedIndex].text, weatherData)
});