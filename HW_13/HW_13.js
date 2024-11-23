const searchInput = document.querySelector('#searchInput');
const searchButton = document.querySelector('#searchButton');
const inputPoint = document.querySelector('#inputPoint');
const body = document.querySelector('body');

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

function parseWeatherData(weatherData) {
    let cityName = weatherData.name;
    let description = weatherData.weather[0].description;
    let temperature = `${Math.floor(weatherData.main.temp)} °C`;
    let feelsLike = `Ощущается как ${Math.floor(weatherData.main.feels_like)} °C`;
    let windSpeed = `${weatherData.wind.speed} м/с`;
    let humidity = `${weatherData.main.humidity}%`;
    let dateTime = new Date(weatherData.dt * 1000).toDateString();

    return {cityName, description, temperature, feelsLike, windSpeed, humidity, dateTime};
}    

function renderWeatherData(cityName,weatherData) {
    let weatherDataParsed = parseWeatherData(weatherData);
    //Пока без проверки наличия города, просто выводим информацию о погоде
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
}

function createChildFormElement(parentElement, elementName, elementClass, elementStyle, elementID, elementTextContent) {
    var childElement = document.createElement(elementName);
    parentElement.appendChild(childElement);
    elementClass.length > 0 ? childElement.className=elementClass : null;
    elementStyle.length > 0 ? childElement.style=elementStyle : null;
    elementName === 'button' ? childElement.onclick=closeWidget : null;    
    elementID.length > 0 ? childElement.id=elementID : null;
    elementTextContent.length > 0? childElement.textContent=elementTextContent : null;
    return childElement;
}

function createFormElement (element, weatherDataParsed) {
    console.log(weatherDataParsed);
    inputPoint.parentNode.insertBefore(element, inputPoint);
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
    createChildFormElement(childElement, 'span', 'small', 'color: #868B94', 'weatherDesc', weatherDataParsed.description);
    createChildFormElement(childElement, 'span', 'small', 'color: #868B94', 'feelsLike',weatherDataParsed.feelsLike);
    childElement=createChildFormElement(childElement.parentNode, 'div', 'd-flex align-items-center', '', '', '');
    childElement=createChildFormElement(childElement, 'div', 'flex-grow-1', 'font-size: 1rem;', '', '');
    childElement=createChildFormElement(childElement, 'div', '', '', '', '');
    createChildFormElement(childElement, 'i', 'fas fa-wind fa-fw', 'color: #868B94;', '','');
    createChildFormElement(childElement, 'span', 'ms-1', '', 'windSpeed',weatherDataParsed.windSpeed);
    childElement=createChildFormElement(childElement.parentNode, 'div', '', '', '', '');
    createChildFormElement(childElement, 'i', 'fas fa-wind fa-fw', 'color: #868B94;', '','');
    createChildFormElement(childElement, 'span', 'ms-1', '', 'humidity',weatherDataParsed.humidity);
}

function getWeatherData (cityName) {
    let weatherDataParsed = parseWeatherData(weatherData);      //Получаем информацию о погоде
    var div = document.createElement('div');                    //Создаем элемент div
    createFormElement(div,weatherDataParsed);                   //Вызываем функцию для отрисовки div и вставки на страницу
}

searchButton.addEventListener('click', function (event) {
    event.preventDefault()
    cityName = searchInput.value.trim();
    let storageCity = localStorage.getItem('city');
    if (storageCity === cityName) {
        alert(`Город ${cityName} уже выбран!`)
        return;
    }
    if (cityName.length >0 && cityName==='Санкт-Петербург') {       //Если ввели наименование города. Пока только тот что есть
        getWeatherData(cityName);
        localStorage.setItem('city', cityName);
    }
    else {
        alert('Введите город Санкт-Петербург!');    //Пока только Санкт-Петербург
        searchInput.value = '';
    }

    // searchInput.value = '';
});

function closeWidget(event) {
    event.preventDefault();
    let target = event.target;
    parentDiv = target.parentNode.parentNode.parentNode.parentNode;
    parentDiv.parentNode.removeChild(parentDiv);
    localStorage.removeItem('city');
    searchInput.value = '';
}

document.addEventListener('DOMContentLoaded', function () {
    let cityName = localStorage.getItem('city');
    if (cityName) {
        searchInput.value = cityName;
        getWeatherData(cityName);
    }
})