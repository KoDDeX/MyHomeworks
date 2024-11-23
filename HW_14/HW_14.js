const searchInput = document.querySelector('#searchInput');
const searchButton = document.querySelector('#searchButton');
const inputPoint = document.querySelector('#inputPoint');
const apiKey = '167349a6d42610462c6f5bd91a7c2e36';
let airPollutionDescriptionObj = {
    1: "Отличное",
    2: "Хорошее",
    3: "Умеренное",
    4: "Тревожное",
    5: "Ужасное"
}

// Асинхронная функция для получения локации по городу
async function getCityGeo (cityName, apiKey) {
    let url = `http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${apiKey}`;
    console.log(`Сделали запрос на локацию по городу ${cityName}: ${url}`);
    const response = await fetch(url);
    if (response.ok) {
        console.log(`Получен ответ с GeoData по городу ${cityName}:`);
        const data = await response.json();
        let geoData = {
            lat: data[0].lat,
            lon: data[0].lon
        }
        console.log(geoData);
        return geoData;
    }
    else {
        console.error(`Ошибка ${response.status}: ${response.statusText}`);
        throw new Error(`Ошибка получения геолокации по городу ${cityName} (${response.status}: ${response.statusText})`);
    }
}

// Функция для формирования запросов о погоде и состоянии воздуха
function getUrls(geoData, apiKey, cityName) {
    let units ='metric';
    let lang = 'ru';

    const urls = {
        // currentWeather: `http://api.openweathermap.org/data/2.5/weather?lat=${geoData.lat}&lon=${geoData.lon}&appid=${apiKey}&units=${units}&lang=${lang}`,
        currentWeather: `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=${units}&lang=${lang}`,
        airPollution: `http://api.openweathermap.org/data/2.5/air_pollution?lat=${geoData.lat}&lon=${geoData.lon}&appid=${apiKey}&units=${units}&lang=${lang}`,
        forecast: `http://api.openweathermap.org/data/2.5/forecast?lat=${geoData.lat}&lon=${geoData.lon}&units=${units}&appid=${apiKey}&lang=${lang}`
    }
    return urls;
} 

// Функция дл формирования запроса на иконку по размеру
function getIconUrl (iconCode, size) {
    if (size === undefined) {
        size = "";
    }
    else if (size === "4x") {
        size = "@4x";
    }
    else if (size === "2x") {
        size = "@2x";
    }
    else {
        throw new Error("Неизвестный размер");
    }
    return `http://openweathermap.org/img/wn/${iconCode}${size}.png`;
}

// Функция для парсинга ответа о погоде
function parseWeatherData(weatherData) {
    let cityName = weatherData.name;
    let description = weatherData.weather[0].description;
    let temperature = `${Math.floor(weatherData.main.temp)} °C`;
    let feelsLike = `${Math.floor(weatherData.main.feels_like)} °C`;
    let windSpeed = `${weatherData.wind.speed} м/с`;
    let humidity = `${weatherData.main.humidity}%`;
    let dateTime = new Date(weatherData.dt * 1000).toDateString();
    let icon = weatherData.weather[0].icon;

    return {cityName, description, temperature, feelsLike, windSpeed, humidity, dateTime, icon};
}    

// Функция для парсинга ответа о состоянии воздуха
function parseAirPollutionData(airPollutionData) {
    let airQuality = airPollutionData.list[0].main.aqi;
    let airQualityDescription = airPollutionDescriptionObj[airPollutionData.list[0].main.aqi];

    return {
        aqi: airQuality,
        aqiDesc: airQualityDescription
    }
}

// Функция для добавления города в LocalStorage
function insertIntoLocalStorage (cityName) {
    let cityStore = localStorage.getItem('city');
    if (cityStore) {
        cityStoreArray = cityStore.split(',');
        for (city of cityStoreArray) {
            if (city === cityName) {            
                return;                             //Город уже есть в списке, выходим без реализации
            }
        }
        cityStoreArray.push(cityName);
        localStorage.setItem('city', cityStoreArray.join(','));
        return;
    }
    localStorage.setItem('city', `${cityName}`);
}

// Функция для удаления города из LocalStorage
function deleteFromLocalStorage (cityName) {
    let cityStore = localStorage.getItem('city');
    if (cityStore) {
        cityStoreArray = cityStore.split(',');
        cityStoreArray = cityStoreArray.filter(city => city!== cityName);
        localStorage.setItem('city', cityStoreArray.join(','));
    }
}

// Общая функция для создания дочернего элемента с параметрами
function createChildFormElement(parentElement, elementName, elementClass, elementStyle, elementID, elementTextContent) {
    var childElement = document.createElement(elementName);
    parentElement.appendChild(childElement);
    elementClass.length > 0 ? childElement.className=elementClass : null;
    elementStyle.length > 0 ? childElement.style=elementStyle : null;
    elementName === 'button' ? childElement.onclick=closeWidget : null;    
    elementID.length > 0 ? childElement.id=elementID : null;
    elementTextContent.length > 0 ? childElement.textContent=elementTextContent : null;
    return childElement;
}

// Функция для закрытия информации о погоде в конкретном городе и удаления его из LocalStorage
function closeWidget(event) {
    event.preventDefault();
    let target = event.target;
    deleteFromLocalStorage(target.parentNode.nextElementSibling.firstElementChild.textContent);
    parentDiv = target.parentNode.parentNode.parentNode.parentNode;
    parentDiv.parentNode.removeChild(parentDiv);
}

// Функция для отображения результатов запроса погодных условий
function renderResult (weatherData) {
    let weatherDataParsed = parseWeatherData(weatherData.currentWeather);
    console.log(weatherDataParsed);
    let airPollutionParsed = parseAirPollutionData(weatherData.airPollution);
    console.log(airPollutionParsed);
        let element = document.createElement('div');
    // inputPoint.parentNode.insertBefore(element, inputPoint);
    inputPoint.after(element);
    element.className='col-md-6 col-lg-4 col-xl-3 mb-3';
    var childElement=createChildFormElement(element, 'div', 'card text-body widget', 'border-radius: 35px;','','');
    childElement=createChildFormElement(childElement, 'div', 'card-body p-4','','','');
    childElement=createChildFormElement(childElement, 'div', 'd-flex justify-content-end', '','','');
    createChildFormElement(childElement, 'button', 'btn btn-dark', '', '','X');
    childElement=createChildFormElement(childElement.parentNode, 'div', 'd-flex', '','','');
    createChildFormElement(childElement, 'h6', 'flex-grow-1','', "", weatherDataParsed.cityName);
    createChildFormElement(childElement, 'h6', '','','date', weatherDataParsed.dateTime);
    childElement=createChildFormElement(childElement.parentNode, 'div', 'd-flex flex-column text-center mt-5 mb-4', '', '', '');
    createChildFormElement(childElement, 'h6', 'display-4 mb-0 font-weight-bold', '', 'weatherTemp', weatherDataParsed.temperature);
    let iconImg = document.createElement("img");
    let iconID = weatherDataParsed.icon;
    iconImg.src = getIconUrl(iconID, '2x');
    childElement=createChildFormElement(childElement, 'span', 'small', '', '', '');
    childElement.appendChild(iconImg);
    createChildFormElement(childElement.parentNode, 'span', 'small', 'color: #868B94', 'weatherDesc', weatherDataParsed.description);
    createChildFormElement(childElement.parentNode, 'span', 'small', 'color: #868B94', 'feelsLike', 'Ощущается как ' + weatherDataParsed.feelsLike);
    childElement=createChildFormElement(childElement.parentNode.parentNode, 'div', 'd-flex align-items-center', '', '', '');
    childElement=createChildFormElement(childElement, 'div', 'flex-grow-1', 'font-size: 1rem;', '', '');
    childElement=createChildFormElement(childElement, 'div', 'd-flex justify-content-between', '', '', '');
    // createChildFormElement(childElement, 'i', 'fas fa-wind fa-fw', 'color: #868B94;', '','');
    createChildFormElement(childElement, 'span', 'ms-1', 'color: #868B94;', 'windSpeed',weatherDataParsed.windSpeed);
    createChildFormElement(childElement, 'span', 'ms-1', 'color: #868B94;', '', 'aqi: ' + airPollutionParsed.aqi);
    childElement=createChildFormElement(childElement.parentNode, 'div', 'd-flex justify-content-between', '', '', '');
    // createChildFormElement(childElement, 'i', 'fas fa-wind fa-fw', 'color: #868B94;', '','');
    createChildFormElement(childElement, 'span', 'ms-1', 'color: #868B94;', 'humidity',weatherDataParsed.humidity);
    createChildFormElement(childElement, 'span', 'ms-1', 'color: #868B94;', '', airPollutionParsed.aqiDesc);
    childElement=createChildFormElement(childElement.parentNode, 'hr', 'text-center mb-0', '', '', 'Прогноз погоды на 5 дней');
    childElement=createChildFormElement(childElement.parentNode.parentNode.parentNode, 'div', 'overflow-x-auto', 'color: #868B94', '', '');
    // Добавляем таблицу для отображения погоды на 5 дней
    childElement=createChildFormElement(childElement, 'table', 'table table-sm', 'table-layout: fixed', '','');
    childElement=createChildFormElement(childElement, 'thead', '', '', '', '');
    childElement=createChildFormElement(childElement, 'tr', '', '', '', '');
    
    // Добавляем заголовок
    createChildFormElement(childElement, 'th', 'text-center', 'font-size: .6rem; width: 70px', '', '');
    for (let i =0; i < weatherData.forecast.list.length; i++) {
        createChildFormElement(childElement, 'th', 'text-center', 'font-size: .6rem; width: 70px', '', weatherData.forecast.list[i].dt_txt);
    }
    childElement=createChildFormElement(childElement.parentNode.parentNode, 'tbody', '', '', '', '');
    childElement=createChildFormElement(childElement, 'tr', '', '', '', '');
    // Добавляем сроку с температурой
    createChildFormElement(childElement, 'th', '', 'font-size: .6rem; width: 70px', '', 'Температура');
    for (let i =0; i < weatherData.forecast.list.length; i++) {
        let forecastweatherDataParsed = parseWeatherData(weatherData.forecast.list[i])
        createChildFormElement(childElement, 'td', 'text-center', 'font-size: .6rem', '', forecastweatherDataParsed.temperature);
    }
    childElement=createChildFormElement(childElement.parentNode, 'tr', '', '', '', '');
    // Добавляем сроку с описанием погоды
    createChildFormElement(childElement, 'th', '', 'font-size: .6rem; width: 70px', '', 'Описание');
    for (let i =0; i < weatherData.forecast.list.length; i++) {
        let forecastweatherDataParsed = parseWeatherData(weatherData.forecast.list[i]);
        let childTd = document.createElement("td");
        let iconImg = document.createElement("img");
        let iconID = forecastweatherDataParsed.icon;
        iconImg.src = getIconUrl(iconID);
        (childElement.appendChild(childTd)).appendChild(iconImg);
        // createChildFormElement(childElement, 'td', 'text-center', 'font-size: .6rem', '', forecastweatherDataParsed.description);
    }
    childElement=createChildFormElement(childElement.parentNode, 'tr', '', '', '', '');
    // Добавляем сроку с ощущением температуры
    
    createChildFormElement(childElement, 'th', '', 'font-size: .6rem; width: 70px', '', 'Ощущается');
    for (let i =0; i < weatherData.forecast.list.length; i++) {
        let forecastweatherDataParsed = parseWeatherData(weatherData.forecast.list[i]);
        createChildFormElement(childElement, 'td', 'text-center', 'font-size: .6rem', '', forecastweatherDataParsed.feelsLike);
        // iconImg.style= "display:inline-block";

    }
    childElement=createChildFormElement(childElement.parentNode, 'tr', '', '', '', '');
    // Добавляем сроку с ветром
    createChildFormElement(childElement, 'th', '', 'font-size: .6rem; width: 70px', '', 'Ветер');
    for (let i =0; i < weatherData.forecast.list.length; i++) {
        let forecastweatherDataParsed = parseWeatherData(weatherData.forecast.list[i])
        createChildFormElement(childElement, 'td', 'text-center', 'font-size: .6rem', '', forecastweatherDataParsed.windSpeed);
    }
    childElement=createChildFormElement(childElement.parentNode, 'tr', '', '', '', '');
    // Добавляем сроку с влажностью
    createChildFormElement(childElement, 'th', '', 'font-size: .6rem; width: 70px', '', 'Влажность');
    for (let i =0; i < weatherData.forecast.list.length; i++) {
        let forecastweatherDataParsed = parseWeatherData(weatherData.forecast.list[i])
        createChildFormElement(childElement, 'td', 'text-center', 'font-size: .6rem', '', forecastweatherDataParsed.humidity);
    }
}

// Асинхронная функция для выполнения запроса на погоду
async function getWeather(url) {
    const response = await fetch(url);
    if (response.ok) {
        console.log(`Получен успешный ответ от URL: ${url}`);
        return await response.json(); // Преобразуем ответ в JSON
    }
    else {
        console.error(`Ошибка ${response.status}: ${response.statusText}`);
        throw new Error(`Ошибка получения даных ${response.status}: ${response.statusText}`);
    }
}

// Асинхронная функция для запроса информации по городу и отображения рузультатов запросов, с добавленеим в LocalStorage
async function getCityWeather (cityName) {
    // let weatherData = getCurrentWeather(cityName, apiKey)
    console.log(`Ищем погоду по городу ${cityName}`)
    let geoData = await getCityGeo(cityName, apiKey);
    console.log(`Получаем urls для погоды`);
    let urlsObject = getUrls(geoData, apiKey, cityName);
    let weatherData = await Promise.all([
        getWeather(urlsObject.currentWeather),
        getWeather(urlsObject.airPollution),
        getWeather(urlsObject.forecast)
    ])
    let resultWeatherData = {
        currentWeather: weatherData[0],
        airPollution: weatherData[1],
        forecast: weatherData[2]
    }
    console.log(`Получили погоду для города ${cityName}`);
    console.log(resultWeatherData)
    renderResult(resultWeatherData);
    insertIntoLocalStorage(cityName);
}

// Проверяем город на существование в LocalStorage
function isCityInStorage(cityName) {
    let cityStore = localStorage.getItem('city');
    if (cityStore) {
        let cityStoreArray = cityStore.split(',');
        return cityStoreArray.includes(cityName);
    }
    return false;
}

// Функция добавления новых городов к отображению с сохранением в LocalStorage (если город новый)
searchButton.addEventListener('click', function (event) {
    event.preventDefault()
    let cityNameArr = searchInput.value.trim().split(',');
    for (let cityName of cityNameArr) {
        cityName = cityName.trim();
        if (cityName.length > 0 && !isCityInStorage(cityName)) {
            getCityWeather(cityName);                         
        }
        else {
            alert(`Город ${cityName} уже добавлен к отображению.`);
        }
    }
    searchInput.value = '';
});

// Функция отображения погоды городов, записанных в LocalStorage.
document.addEventListener('DOMContentLoaded', function () {        
    let cityStore = localStorage.getItem('city');
    if (cityStore) {
        let cityStoreArray = cityStore.split(',');
        for (cityName of cityStoreArray) {
            getCityWeather(cityName);                         
        }
    }
})

