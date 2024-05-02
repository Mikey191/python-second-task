# Python.
# Второй урок.

### План на урок:
1. Работа со **строками**. Основные **методы строк**.
2. **Срезы** в Python.
3. Условный оператор **if**. Конструкция **if-elif-else**.
4. Циклы **while** и **for**
5. Операторы **break**, **continue**.
6. Цикл **for** и функция **range**.

## 1. Работа со строками. Основные методы строк.
**Строка** - это последовательность символов, заключенных в одинарные или двойные кавычки. Строки в Python являются **неизменяемыми**, что означает, что после создания строки ее нельзя изменить.

Python также предлагает различные способы записи строк:
1. **Обычные строки**: Обычные строки в Python заключаются в одинарные или двойные кавычки.
```python
str_1 = 'Привет'
str_2 = "Мир"
```

2. **Сырые строки**: Сырые строки в Python обозначаются с помощью префикса r перед открывающей кавычкой. В сырых строках символы экранирования не интерпретируются.
```python
path = r'C:\Users\Username\Documents'
```

3. **F-строки**: F-строки (от "formatted strings") представляют собой способ форматирования строк, в которых можно вставлять значения переменных или выражений. F-строки обозначаются с помощью префикса f перед открывающей кавычкой и могут содержать выражения в фигурных скобках.
```python
name = "Алиса"
age = 25
message = f"Меня зовут {name} и мне {age} лет."

```
### Индексы.
В Python строки являются **последовательностями символов**, и каждый символ в строке имеет свой **индекс**. Индексы в строках начинаются с 0 для первого символа и увеличиваются на 1 для каждого следующего символа. Индексы также могут быть отрицательными, где -1 соответствует последнему символу в строке, -2 - предпоследнему символу и так далее.
```python
s = "Hello, World!"
print(s[0])  # "H"
print(s[7])  # "W"
print(s[-1])  # "!"
```
Обращение по индексу в строках в Python похоже на обращение по индексу в списках. В обоих случаях индексы начинаются с **0**, и вы можете получить доступ к отдельным элементам, используя **квадратные скобки** и **индекс**.
```python
my_str_1 = "zero_index"
my_str_2 = "first_index"
my_str_3 = "second_index"
my_list = [my_str_1, my_str_2, my_str_3]
print(my_list[0])
print(my_list[-1])
print(my_list[0][3])
print(my_list[-1][0])
```
## 2. Срезы в Python
**Срезы** в Python - это способ получения **подстроки** из **строки** или **подсписка** из **списка**. С помощью срезов вы можете **извлекать части данных** из последовательностей, таких как строки и списки, на основе их **индексов**.

1. Синтаксис срезов для строк и списков выглядит следующим образом: s[a:b], где **s** - строка или список, **a** - индекс начала среза (включительно), **b** - индекс конца среза (не включая его).
2. Если **a** не указан, срез начинается с **начала строки или списка**. Если **b** не указан, срез идет **до конца строки или списка**.
3. Можно использовать **отрицательные индексы** для **обратного отсчета** с конца строки или списка. Например, s[-1] обращается к последнему символу строки или последнему элементу списка.
4. Срезы также могут иметь третий параметр - **шаг (step)**. Например, s[::2] вернет каждый второй символ строки или каждый второй элемент списка.
```python
s = "Привет, мир!"
print(s[0:6])  # "Привет"
print(s[7:])  # "мир!"
print(s[::-1])  # "!рим ,тевирП"
```
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # [2, 3, 4]
print(numbers[::-1])  # [5, 4, 3, 2, 1]
```
### Важно
Обратите внимание, что срезы возвращают **новую последовательность**, а **не изменяют исходную строку или список**.

## Основные методы строк в Python:
1. **replace(old, new)** - заменяет все вхождения подстроки old на подстроку new в строке. Возвращает новую строку с замененными значениями. Пример использования:
```python
s = "Привет, мир!"
new_s = s.replace("мир", "вселенная")
print(new_s)  # "Привет, вселенная!"
```
2. **split(sep)** - разделяет строку на подстроки, используя разделитель sep. Возвращает список подстрок. Пример использования:
```python
s = "Я люблю Python"
words = s.split()
print(words)  # ["Я", "люблю", "Python"]
```
3. **strip()** - удаляет пробельные символы в начале и конце строки. Возвращает новую строку без пробельных символов. Пример использования:
```python
s = "   Привет   "
new_s = s.strip()
print(new_s)  # "Привет"
```
4. **lower()** - преобразует все символы строки в нижний регистр. Возвращает новую строку в нижнем регистре. Пример использования:
```python
s = "Hello, World!"
new_s = s.lower()
print(new_s)  # "hello, world!"
```
5. **upper()** - преобразует все символы строки в верхний регистр. Возвращает новую строку в верхнем регистре. Пример использования:
```python
s = "Hello, World!"
new_s = s.upper()
print(new_s)  # "HELLO, WORLD!"
```
6. **startswith(prefix)** - проверяет, начинается ли строка с указанного префикса prefix. Возвращает True или False. Пример использования:
```python
s = "Hello, World!"
starts_with_hello = s.startswith("Hello")
starts_with_ello = s.startswith("Ello")
print(starts_with_hello)  # True
print(starts_with_ello) # False
```
7. **endswith(suffix)** - проверяет, заканчивается ли строка указанным суффиксом suffix. Возвращает True или False. Пример использования:
```python
s = "Hello, World!"
ends_with = s.endswith("!")
print(ends_with)  # True
```
8. **len()** - возвращает длину строки (количество символов). Пример использования:
```python
s = "Hello, World"
length = len(s)
print(length)  # 12
```
9. **" ".join()** - используется для объединения элементов последовательности в одну строку, разделенных определенным разделителем. Пример использования:
```python
vowels = ["a", "e", "i", "o", "u"]
vowels_str = ",".join(vowels)
print("Гласные буквы:", vowels_str)

names = ['JavaScript', 'Python', 'Go']
delimiter = ', '
single_str = delimiter.join(names)
print(f'Языки программирования: {single_str}')

```

## Задание:
1. Напишите программу, которая принимает строку от пользователя и выводит первый и последний символы этой строки, используя индексы и f-строки.
```python
print(f"Первый символ: {first_char}, последний символ: {last_char}")
```
2. Напишите программу, которая принимает строку от пользователя и выводит каждый третий символ этой строки, начиная с первого символа, используя срезы и f-строки.
```python
print(f"Каждый третий символ: {every_third_char}")
```
3. Напишите программу, которая принимает строку чисел через пробел от пользователя и выводит только числа под четными индексами из этого списка, используя срезы и f-строки.
```python
print(f"Четные числа: {', '.join(even_numbers)}")
```

## 3. Условный оператор if. Конструкция if-elif-else.
#### Условный оператор if в Python позволяет выполнять определенные действия в зависимости от условия. Конструкция if-elif-else используется для проверки нескольких условий и выполнения соответствующего блока кода в зависимости от результата проверки.
1. Проверка числа на положительность, отрицательность.
```python
number = int(input("Введите целое число"))
if number > 0:
    print("Вы ввели положительное число")
else:
    print("Вы ввели отрицательное число")
```
2. Проверка числа на положительность, отрицательность или ноль.
```python
num = int(input("Введите число: "))

if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
```
3. Проверка возраста и вывод соответствующего сообщения.
```python
age = int(input("Введите ваш возраст: "))

if age < 18:
    print("Вы несовершеннолетний")
elif age >= 18 and age < 65:
    print("Вы взрослый")
else:
    print("Вы пенсионер")
```
### Объединение нескольких условий с помощью and, or. Оператор not. Оператор in
#### 1. Оператор **and**. Найти диапазон числа:
```python
number = int(input("Введите число: "))
if number > 0 and number < 11:
    print("Число в диапазоне от 0 до 10")
elif number > 9 and number < 101:
    print("Число в диапазоне от 10 до 100")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")
```
#### 2. Оператор **or**. Проверка вводимого имени:
```python
name = input("Введите ваше имя: ")
if name == "Alice" or name == "Bob":
    print("Привет, " + name + "!")
else:
    print("Привет, незнакомец!")
```
#### 3. Оператор **not**. Определить, есть ли значение в переменной:
```python
name = input("Введите ваше имя: ")
if not name:
    print("Вы не ввели имя")
elif name == "Алиса":
    print("Привет, Алиса!")
elif name == "Боб":
    print("Привет, Боб!")
else:
    print("Привет, незнакомец!")
```
В этом коде, если переменная name пустая или равна False, то условие not name будет истинным. В этом случае будет выполнен блок кода под условием if not name, и на экран будет выведено сообщение "Вы не ввели имя".
#### 4. Оператор **in**. Определить, есть ли введенное имя в списке:
```python
names = ["Алиса", "Боб", "Чарли"]
name = input("Введите ваше имя: ")

if not name:
    print("Вы не ввели имя")
elif name in names:
    print(f"Привет {name}!")
else:
    print("Привет, незнакомец!")
```
Оператор in используется для проверки, содержится ли значение name в списке names (name in names). Если значение name присутствует в списке names, то выполняется блок кода под условием elif name in names, и выводится приветствие с именем.


## 4. Циклы While и for.
### Цикл while
Цикл **while** в Python используется для **повторения блока кода до тех пор, пока условие остается истинным**. Он применяется, когда вы хотите выполнить определенные действия до тех пор, пока выполняется определенное условие.
#### Использование цикла while:
1. Установите начальное значение переменной, которая будет использоваться в условии цикла.
2. Укажите условие, которое должно быть истинным для продолжения выполнения цикла.
3. Определите блок кода, который будет выполняться, пока условие остается истинным.
4. Внутри блока кода обычно включается изменение значения переменной, чтобы в конечном итоге условие стало ложным и цикл завершился.
#### Пример 1: Повторение блока кода до достижения определенного значения
```python
count = 0
while count < 5:
    print("Текущее значение count:", count)
    count = count + 1
```
#### Пример 2: Чтение ввода пользователя до ввода определенного значения
```python
password = ""
while password != "секрет":
    password = input("Введите пароль: ")
    if password == "секрет":
        print("Доступ разрешен!")
    else:
        print("Неверный пароль. Попробуйте еще раз.")
```
### Цикл for
Цикл **for** в Python используется для **итерации по элементам последовательности**, такой как список, строка или диапазон чисел. Он применяется, когда вы хотите выполнить определенные действия для каждого элемента в последовательности.
#### Использование цикла for:
1. Укажите переменную, которая будет использоваться для хранения текущего элемента последовательности.
2. Укажите последовательность, по которой будет происходить итерация.
3. Определите блок кода, который будет выполняться для каждого элемента последовательности.
#### Пример 1: Итерация по списку
```python
names = ["Алиса", "Боб", "Чарли"]
for name in names:
    print("Привет,", name)
```
#### Пример 2: Итерация по строке
```python
message = "Привет, мир!"
for char in message:
    print(char)
```
#### Пример 3: Итерация по диапазону чисел
```python
for number in range(1, 6):
    print(number)
```

## 5. Операторы break, continue.
Операторы **break** и **continue** в Python используются для управления выполнением циклов.
### Оператор break:
1. Оператор **break** используется для немедленного прерывания выполнения цикла.
2. Когда оператор **break** выполняется внутри цикла, выполнение цикла **немедленно прекращается**, и управление передается к следующему оператору после цикла.
3. Оператор **break** обычно используется **вместе с условием**, чтобы прервать цикл, когда выполняется определенное условие.
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)
```
В этом примере цикл for выполняется для каждого элемента в списке numbers. Когда значение number становится равным 3, оператор break прерывает выполнение цикла, и остальные элементы списка не выводятся.
### Оператор continue:
1. Оператор continue используется для пропуска текущей итерации цикла и перехода к следующей итерации.
2. Когда оператор continue выполняется внутри цикла, оставшаяся часть текущей итерации пропускается, и управление передается к следующей итерации цикла.
3. Оператор continue обычно используется вместе с условием, чтобы пропустить выполнение определенных действий для некоторых элементов в цикле.
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)
```
В этом примере цикл for выполняется для каждого элемента в списке numbers. Когда значение number становится равным 3, оператор continue пропускает оставшуюся часть текущей итерации, и выводится только остальные элементы списка.

## 6. Цикл for и функция range.
Цикл for с функцией range в Python используется для итерации по последовательности чисел. Он часто используется для выполнения действий определенное количество раз или для обработки элементов в последовательности.
### Использование цикла for с функцией range:
1. Используйте ключевое слово for для начала цикла.
2. Укажите переменную, которая будет использоваться для хранения текущего значения из последовательности.
3. **Используйте функцию range для создания последовательности чисел**.
4. Определите блок кода, который будет выполняться для каждого значения из последовательности.
#### Пример 1: Итерация по последовательности чисел
```python
for i in range(5):
    print(i)
```
В первом примере цикл for итерируется по последовательности чисел, созданной с помощью функции range(5). Для каждого значения из последовательности выполняется блок кода, и значение выводится на экран.
#### Пример 2: Итерация с использованием диапазона значений
```python
for i in range(1, 6):
    print(i)
```
Во втором примере цикл for итерируется по последовательности чисел от 1 до 5 (не включая 6), созданной с помощью функции range(1, 6). Для каждого значения из последовательности выполняется блок кода, и значение выводится на экран.
#### Пример 3: Итерация с использованием шага
```python
for i in range(0, 10, 2):
    print(i)
```
В третьем примере цикл for итерируется по последовательности чисел от 0 до 10 с шагом 2, созданной с помощью функции range(0, 10, 2). Для каждого значения из последовательности выполняется блок кода, и значение выводится на экран.
#### Пример 4: Использование цикла для выполнения действий определенное количество раз
```python
total = 0
for i in range(1, 6):
    total += i
print("Сумма чисел от 1 до 5:", total)
```
В четвертом примере цикл for используется для выполнения действий определенное количество раз. Цикл итерируется по последовательности чисел от 1 до 5 (включительно), созданной с помощью функции range(1, 6). В каждой итерации значение добавляется к переменной total, и в конце выводится сумма чисел от 1 до 5.

## Задание
### Задача 1: Проверка на четность
Попросите пользователя ввести число.
Используя операторы if и else, проверьте, является ли число четным или нечетным.
Выведите соответствующее сообщение.

### Задача 2: Сумма чисел
Попросите пользователя ввести число N.
Используя цикл for и функцию range, найдите сумму всех чисел от 1 до N.
Выведите полученную сумму.

### Задача 3*: Поиск простых чисел
Используя цикл for и операторы break и continue, найдите и выведите все простые числа в диапазоне от 1 до 100.

### Задача 4: Таблица умножения
Используя цикл for и функцию range, создайте таблицу умножения для определенного числа, например, для числа 5.
Выведите таблицу умножения на экран.

### Задача 5: Поиск среднего значения
Попросите пользователя ввести последовательность чисел, разделенных пробелами.
Используя цикл for и функцию range, найдите среднее значение введенной последовательности.
Выведите полученное среднее значение.