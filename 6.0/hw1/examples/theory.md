# Тестирование
1. Сложность алгоритмов
2. Тестирование собственной программы
3. Автоматизация решиния
4. Как подготовить тесты для задачи?

# RAW МАШИНА (упрощенно)
- Чтение/Запись/инициаализация ячейки памяти стоит одну операцию
- можно выполнять арифмитеческие и логические операции с одной ячейкой памяти, а так же переходы
- похоже на компьютер

# Сложность алгоритмов
# - Сложность алгоритма - порядок количества действий в зависимости от размра данных

### Какие бывают уровни тестирования
- Отстутсвие тестирования вообще (программа для себя)
- Покрытие тестами, нагрузочное тестирование и т.д. 
(основная часть промышленной разработки)
- формальная верификация программа
(микрокод процессора, финансы, космос)

### Что нужно протестировать
- Тесты из условия
- Общие случаи
- Особые случаи

### Советы по составлению тестов
- если есть примеры - реши их руками и сверь ответ. Если не совпадает, то либо  правильных ответов может
быть несколько, лобо ты неправильно понял задачу
- Сначала составь несколько примеров и реши задачу руками, чтобы лучше понять условие и чтобы потом было с чем сравнить
- Проверь последоватьельность из одного элемента и пустую последоватьельность
- "Краевые эффекты" - проверь, что программа работает корректно в начале и конце последовательности, сделай тесты, 
чтобы ответ находился на первом и на последнем месте последовательности
- Составь покрытие всех ветвлений, так чтобы был тест, который входит в каждый if и else
- Подбери тесты, чтобы не было ни одного входа в цикл
- Один тест - одна возможная ошибка.

### Как допуска меньше ошибок
- Написать 3-5 строк - запускаем программу и проверяем с помощью отладчика или оталадочного вывода все ли правильно
- Если что-то неправильно -ошибка, скорее всего в последних 3-5 строках
- Если написали много кода, то ошибку сложнее локализовать и вспомнить что там вообще написано

### Приёмы для тестирования
- Если использовать чтение из файла для ввода - не надо заново вводить тесты
- Тесты внутри файла можно просто переставлять
- После исправления ошибки нужно прогнать все тесты - возможно появились новые ошибки
- Решение можно оформить в виде функции и вызывать её с примерами из условия и вашими тестами

## Автоматизация тестирования

### Сертификат
Дополнительно к правильному ответу (стоимости в рублях) можно возвращать 