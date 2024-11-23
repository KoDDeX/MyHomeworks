proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

variants = [
			'кот',
			'шеф',
			'мозг',
			'лес',
			'фолк',
			'код',
			'рот',
			'мёд',
			'лук',
			'питон',
			'год',
			'час',
			'друг',
			'жена',
			'муж',
			'айфон',
			'работа',
]

const ulResult = document.getElementById("modified_proverbs");

// Задание № 1
function generateProverb(variants, proverbs) {
    // Вариант подробный
    let randProverb = proverbs.splice([Math.floor(Math.random() * proverbs.length)],1).toString();  // Выбираем случайную пословицу из массива proverb, удаляем ее и преобразуем в строку
    let randVariants = variants.splice([Math.floor(Math.random() * variants.length)],1); // Выбираем случайное слово из массива variants и удаляем его
    randProverb = randProverb.replace('Ум', randVariants); // Заменяем Ум в случайной пословице на случайное слово
    return randProverb;  // Возвращаем модифицированную строку

    // Вариант краткий но читать сложно как мне кажется
    // return (proverbs.splice([Math.floor(Math.random() * proverbs.length)],1).toString()).replace('Ум', variants.splice([Math.floor(Math.random() * variants.length)],1));
}

// console.log(generateProverb(variants, proverbs));

// Задание № 2
function generateMultipleProverbs(count, variants, proverbs) {
    let multipleProverbs = [];  // Объявляем массив куда будем складывать модифицированные строки
    for (let i = 0; i < count; i++) {
        multipleProverbs.push(generateProverb(variants, proverbs)); // В цикле размерностью в count запускаем функцию generateProverb
    }
    // return multipleProverbs;  // Возвращаем массив модифицированных строк
    displayProverbs(multipleProverbs)
}

// Задание № 3

function displayProverbs(proverbsList) {
    for (let modifiedProverb of proverbsList) {
        let liResult = ulResult.appendChild(document.createElement("li"));
        liResult.textContent = modifiedProverb;
    }
}

let provCount = parseInt(prompt(`Введите количество пословиц для генерации (1-${variants.length})`)); // Запрашиваем требуемое количество пословиц

if (provCount >= 1 && provCount <= variants.length) {
    let proverbsList= generateMultipleProverbs(provCount, variants, proverbs); // Если в пределах размера массива слов, то работаем
}
else {
    let liResult = ulResult.appendChild(document.createElement("li"));
    liResult.textContent = `Неверное число пословиц. Пожалуйста введите число от 1 до ${variants.length}.`; // Если нет, пусть работает пользователь над внимательным прочтением условий вопроса
}