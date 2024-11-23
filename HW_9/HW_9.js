// Секретное послание
const secretLetter = [
    ['DFВsjl24sfFFяВАДОd24fssflj234'],
    ['asdfFп234рFFdо24с$#afdFFтasfо'],
    ['оafбasdf%^о^FFжа$#af243ю'],
    ['afпFsfайFтFsfо13н'],
    ['fн13Fа1234де123юsdсsfь'],
    ['чFFтF#Fsfsdf$$о'],
    ['и$##sfF'],
    ['вSFSDам'],
    ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
    ['FFэasdfтDFsfоasdfFт'],
    ['FяDSFзFFsыSfкFFf']
];

  // Массив с маленькими русскими буквами
const smallRus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'];

// Создадим пустой массив для хранения расшифрованных слов
 let decodedWords = [];

// // Переменные для хранения текущего секретного слова, текущей буквы и расшифрованного слова
// let currentSecretWord = '';
// let currentLetter = '';
// let decodedWord = '';

// Запускаем цикл для каждого слова в секретном послании
// for (let i = 0; i < secretLetter.length; i++) {
//     decodedWord = ''; 
//     // // Вариант 1. Преобразуем в строку, ведь внутри массива secretLetter - одномерные массивы!
//     // currentSecretWord = secretLetter[i].join('');  
//     // // Запускаем цикл для каждой буквы в слове
//     // for (let j = 0; j < currentSecretWord.length; j++) {
//     //     currentLetter = currentSecretWord[j]; // Берем текущую букву из слова

//     // Вариант 2. Длинные (глубокие) обращения.
//     // Запускаем цикл для каждой буквы в слове
//     for (let j = 0; j < secretLetter[i][0].length; j++) {
//         currentLetter = secretLetter[i][0][j]; // Берем текущую букву из слова

//       // Запускаем цикл для поиска этой буквы в маленьком русском алфавите
//         for (let k = 0; k < smallRus.length; k++) {
//             if (currentLetter === smallRus[k]) { // Если нашли совпадение то добавляем букву к расшифрованному слову
//             decodedWord += smallRus[k]; // 
//             }
//         }
//     }
//       decodedWords.push(decodedWord); //Добавляем в массив расшифрованных слов последнее расшифрованное слово
// }

// Вариант 3. Обращения с использованием рекурсии.
for (let secretArray of secretLetter) {
  for (let secretWord of secretArray) {
    decodedWords.push(" "); 
    for (let letter of secretWord) {
      if (smallRus.includes(letter)) {
        decodedWords.push(letter);
      }
    }
  }
}

// Выводим расшифрованное секретное послание
// console.log(decodedWords.join("")); // Соединяем массив расшифрованных слов в одну строку и выводим на экран
//alert(`Зашифрованное послание: ${decodedWords.join(' ')}`)
let message = decodedWords.join('').trim(); // Соединяем массив расшифрованных слов в одну строку и обрезаем крайние пробелы
console.log("Расшифрованное послание:", message); // Выводим расшифорванное послание в console.log