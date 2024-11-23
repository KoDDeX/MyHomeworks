// Запросим у пользователя список покупок разделенного пробелами

let userInput = prompt("Введите список покупок через пробел:");

// Преобразуем введенный список в массив

let shoppingList = userInput.split(" ");

// Выведем полученный массив в консоль

console.log(shoppingList);

// Сообщим пользователю сколько элементов содержится в его списке покупок при помощи alert

alert(`Ваш список покупок содержит ${shoppingList.length} элементов`);

// Запросим у пользователя номер элемента из списка (от 1 до N)

let userItemNumber = parseInt(prompt("Введите номер элемента списка (от 1 до " + shoppingList.length + "):"));

// Покажем пользователю выбранный элемент из списка

alert(`Вы выбрали "${shoppingList[userItemNumber - 1]}"`);

// Запросим у пользователя с помощью prompt, хочет ли он изменить выбранный элемент из списка

let userChange = prompt("Хотите заменить выбранный вами товар - " + shoppingList[userItemNumber-1] + "?" + 
    "Да - введите новое значение." + 
    "Нет - оставьте поле пустым.");

// Если ответ не пустой, то заменить старое значение новым

if (userChange !== "") {
    shoppingList[userItemNumber - 1] = userChange;
}

// Объединим массив обратно в строку, разделяя элементы запятыми

let newShoppingList = shoppingList.join(", ");

// Выведем новый список покупок с помощью alert

alert("Новый список покупок: " + newShoppingList);