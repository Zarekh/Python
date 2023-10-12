def getCount(inputStr):
    num_vowels = 0
    for vow in ["a", "e", "i", "o", "u"]:
        num_vowels += inputStr.count(vow)
    return num_vowels
getCount("askdmasdmaowdadlasmdlnk")

'''
# Карты 3.0
# Демонстрирует наследование в части переопределения методов
class Card(object):
    """Одна игральная карта"""
    RANKS = ["Т", "б", "7", "8", "9", "10", "В", "Д", "К"]
    SUITS = ["к", "ч", "п", "б"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Unprintable_Card(Card) :
    """ Карта, номинал и масть которой не могут быть выведены на экран"""
    def __str__(self):
        return "<нельзя напечатать>"


class Positionable_Card(Card):
    """Карта. которую можно положить лицом или рубашкой вверх"""
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "ХХ"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

# основная часть
card1 = Card("Т", "к")
card2 = Unprintable_Card("Т", "ч")
card3 = Positionable_Card("Т", "п")
print("Печатаю объект Card:", card1)
print("\nПечатаю объект Unprintable_Card:", card2)
print("\nПечатаю объект Positionable_Card:", card3)
print("Переворачиваю объект Positionable Card.")
card3.flip()
print("\nПечатаю объект Positionable_Card:", card3)
input("\n\nНажмите Enter. чтобы выйти.")


# Карты 2.0
# Демонстрирует расширение класса через наследование
class Card(object):
    """Одна игральная карта"""
    RANKS = ["Т", "б", "7", "8", "9", "10", "В", "Д", "К"]
    SUITS = ["к", "ч", "п", "б"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """Рука: набор карт на руках у одного игрока"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """Колода игральных карт"""
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("He могу больше сдавать: карты закончились!")

# основная часть
deck1 = Deck()
print("Создана новая колода:")
print(deck1)
deck1.populate()
print("\nКолода которой появились новые карты.")
print(deck1)
deck1.shuffle()
print("\nПеремешанная колода:")
print(deck1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand=5)
print("\nMнe и вам на руки роздано по 5 карт.\nУ меня на руках:")
print(my_hand)
print("у вас на руках:")
print(your_hand)
print("Осталось в колоде:")
print(deck1)
deck1.clear()
print("Очищенная колода она выглядит теперь:", deck1)
input("\n\nНажмите Enter. чтобы выйти.")


# Карты
# Демонстрирует сочетание объектов
class Card(object):
    """Одна игральная карта"""
    RANKS = ["Т", "6", "7", "8", "9", "10", "В", "Д", "К"]
    SUITS = ["к", "б", "п", "ч"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
class Hand(object):
    """Рука: набор карт на руках у одного игрока"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<Пусто>"
        return rep

    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# основная часть
card1 = Card(rank="Т",suit="к")
print("Вывожу на экран объект-карту:")
print(card1)
card2 = Card(rank="6", suit="к")
card3 = Card(rank="7", suit="к")
card4 = Card(rank="8", suit="к")
card5 = Card(rank="9", suit="к")
print("\nВывожу еще четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nПечатаю карты. которые у меня на руках до раздачи:")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПечатаю пять карт. которые появились у меня на руках:")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nПервые две из моих карт я передал вам.")
print("Теперь у вас на руках:")
print(your_hand)
print("A у меня на руках:")
print(my_hand)

my_hand.clear()
print("\nY меня на руках после того. как я сбросил все карты:")
print(my_hand)
input("\n\nНажмите Enter. чтобы выйти.")


# Гибель пришельца
# Демонстрирует взаимодействие объектов
class Player(object):
    """Игрок в экшен-игре. """
    def blast(self, enemy):
        print("Стрельба во врага.\n")
        enemy.die()
class Alien(object):
    """ Враждебный пришелец-инопланетянин в зкшен-игре. """
    def die (self):
        print("Смерть пришельца")
# Основная часть программы
print("Гибeль пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
input("\n\nHaжмитe Enter. чтобы выйти.")


# Моя зверюшка
# Виртуальный питомец. о котором пользователь может заботиться
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Kaк вы назовете свою зверюшку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        choice = input("Baш выбор:")
        print()

        # ВЫХОД
        if choice == "0":
            print("Дo свидания.")
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        # кормление зверюшки
        elif choice == "2":
            crit.eat()
        # игра со зверюшкой
        elif choice == "3":
            crit.play()
        # непонятный пользовательский ввод
        else:
            print("Извините. в меню нет пункта", choice)
main()
input("\n\nHaжмитe Enter. чтобы выйти.")


# Зверюшка со свойствами
# Демонстрирует свойства
class Critter(object):
    # Виртуальный питомец
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name in "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("\nПривет, меня зовут", self.name)

# основная часть
crit = Critter("Бoбик")
crit.talk()
print("\nМою зверюшку зовут", end=" ")
print(crit.name)
print("\nПробую изменить имя зверюшки на Мурзик")
crit.name = "Мурзик"
print("Moю зверюшку зовут", end=" ")
print(crit.name)
print("\nПробую изменить имя зверюшки на пустую строку")
crit.name = ""
print("Мою зверюшку зовут", end=" ")
print(crit.name)
input("\n\nНажмите Enter. чтобы выйти.")


# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name # открытый атрибут
        self.__mood = mood # закрытый атрибут

    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Этo закрытый метод.")

    def public_method(self):
        print("Этo открытый метод.")
        self.__private_method()
# основная часть
crit = Critter (name ="Бобик", mood ="прекрасно")
crit.talk()
crit.public_method()
input("\n\nHaжмитe Enter. чтобы выйти.")


# Классово верная зверюшка
# Демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверюшек", Critter.total)
    def __init__ (self, name):
        print("Появилась новая зверюшка!")
        self.name = name
        Critter.total += 1
# основная часть
print("Находим значение атрибута класса Critter.total:", end=" ")
print(Critter.total)
print("\nСоздаем зверюшек.")
crit1 = Critter("зверюшка 1")
crit2 = Critter("зверюшка 2")
critЗ = Critter("зверюшка 3")
Critter.status()
print("\nОбращаемся к атрибуту класса через объект:", end=" ")
print(crit1.total)
input("\n\nНажмите Enter. чтобы выйти.")


# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним
class Critter(object) :
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep +="имя: "+ self.name + "\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")
# основная часть
crit1 = Critter("Бoбик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Bывoд объекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name:")
print(crit1.name)
input("\n\nHaжмитe Enter. чтобы выйти.")

# Зверюшка с конструктором
# Демонстрирует метод-конструктор
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет новая зверюшка!")
    def talk(self):
        print("\nПpивeт. Я зверюшка - экземпляр класса Critter.")
# основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input("\n\nHaжмитe Enter. чтобы выйти.")

# Просто зверюшка
# Демонстрирует простейшие класс и объект
class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")
# основная часть
crit = Critter()
crit.talk()
input("\n\nHaжмитe Enter. чтобы выйти.")

# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы которой читаются из текстового файла
import sys
def open_file(file_name, mode):
    # Открывает файл
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", file_name, "Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter. чтобы выйти.")
        sys.exit()
    else:
        return the_file
# Возвращает в отформатированном виде очередную строку игрового файла
def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
# Возвращает очередной блок данных из игрового файла
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        correct = next_line(the_file)
        if correct:
            correct = correct[0]
            explanation = next_line(the_file)
    return category, question, answers, correct, explanation
#Приветствует игрока и сообщает тему игры
def welcome(title):
    print("\t\tДобро пожаловать в игру 'Викторина' !\n")
    print("\t\t", title, "\n")
# Настройка игры
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # получение ответа
        answer = input("Baш ответ: ")
        # проверка ответа
        if answer == correct:
            print("\nДa!", end=" ")
            score += 1
        else:
            print("\nHeт.", end=" ")
            print(explanation)
            print("Счёт:", score, "\n\n")
            # переход к следующему вопросу
            category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()
    print("Этo был последний вопрос!")
    print("Ha вашем счету", score)

main()
input("\n\nHaжмитe Enter. чтобы выйти.")

# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
try:
    num = float(input("Введите число: "))
except:
    print("Похоже, это не число!")

# обработка исключения определенного типа
try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Этo не число!")

# обработка исключений нескольких разных типов
print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число:", value, "->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")

for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умею преобразовывать только строки. составленные из цифр!")

# получение аргумента
try:
    num = float(input("\nВведите число:"))
except ValueError as e:
    print("Этo не число! Интерпретатор как бы говорит нам:")
    print(e)

# try/except/else
try:
    num = float(input("\nВведите число:"))
except ValueError:
    print("Этo не число!")
else:
    print("Bы ввели число", num)
input("\n\nHaжмитe Enter. чтобы выйти.")


# Законсервируем
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки
import pickle, shelve

print("Консервация списков")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондюзль"]
# Открытие на запись нового файла
f = open("pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nРасконсервация списков.")
f = open ( "pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
# вывод списков на экран
print(variety)
print(shape)
print(brand)
f.close()

print("\nПомещение списков на полку")
s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]
# убедимся что данные записаны
s.sync()

print("\nИзвлечение списков из файла полки:")
print("торговые марки:", s["brand"])
print("формы:", s["shape"])
print("виды овощей:", s["variety"])

s.close()


# Запишем
# Демонстрирует запись в текстовый файл
print("Создаю текстовый файл методом write()")
text_file = open("write_it.txt", "w", encoding='utf-8')
text_file.write("Строка 1\n")
text_file.write("Этo строка 2\n")
text_file.write("Этой строке достался номер 3\n")
text_file.close()

print("\nЧитаем вновь созданный файл")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print ( "\nСоздаю текстовый файл методом writelines()")
text_file = open("write_it.txt", "w", encoding='utf-8')
lines = ["Строка 1\n",
        "Строка 2\n",
        "Этой строке достался номер 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nЧитаю вновь созданный файл")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()
input("\n\nНажмите Enter. чтобы выйти.")


# Прочитаем
# Демонстрирует чтение из текстового файла
print("Открываю и закрываю файл:")
text_file = open("read_it.txt", "r", encoding='utf-8')
text_file.close()
print("\n Читаем файл посимвольно:")
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()
print("\n Читаем файл целиком:")
text_file = open("read_it.txt", "r", encoding='utf-8')
whole_thing = text_file.read()
print(whole_thing)
text_file.close()
print("\n Читаем одну строку посимвольно:")
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()
print("\nЧитаем одну строку целиком:")
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()
print("\nЧитаем весь файл в список:")
text_file = open("read_it.txt", "r", encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()
print("\n Перебираем файл построчно:")
text_file = open("read_it.txt", "r", encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()
input("\n\n Нажмите Enter. чтобы выйти.")


# Доработайте новую версию игры «Опадай число» (которую вы создали, решая предыдущую задачу) так, чтобы
# основная часть программы стала функцией main(). Для того чтобы игра началась, не забудьте вызвать эту
# функцию глобально.
import random
def hod_number(LOW=0,HIGH=5):
    attempt = int(input("Это число: "))
    return attempt
def main():
    LOW = 0
    HIGH = 5
    attempt = 0
    attempt_count = 0
    print('Я загадала целое число от 0 до 100. Угадай с 5 попыток!')
    number = random.randrange(101)
    while attempt_count in range(LOW, HIGH):
        hod_number()
        attempt_count += 1
        if attempt < number:
            print('Больше!')
        elif attempt > number:
            print('Меньше!')
        elif attempt == number:
            print('Ничего себе! Ты отгадал! Это правда', number)
            print('Количество попыток:', attempt_count)
            break
    if attempt != number:
        print("О, ужас! Ты совершенно не умеешь читать мои мысли!Это было число:\n", number,
            "Так и не смог угадать число за 5 попыток :(" )
main ()


# Доработайте игру «Опадай число» из главы З так, чтобы в ней нашла применение функция ask_number()
import random
print('Я загадала целое число от 0 до 100. Угадай с 5 попыток!')
number = random.randrange(101)
attempt = None
def ask_number(low=0, high=5):
    attempt_count = 0
    while attempt_count in range(low, high):
        attempt = int(input("Это число: "))
        attempt_count += 1
        if attempt < number:
            print('Больше!')
        elif attempt > number:
            print('Меньше!')
        elif attempt == number:
            print('Ничего себе! Ты отгадал! Это правда', number)
            print('Количество попыток:', attempt_count)
            break
    return attempt
ask_number()
if attempt!=number:
    print("О, ужас! Ты совершенно не умеешь читать мои мысли! Это было число", number, "\n"
        "Так и не смог угадать число за 5 попыток :(")


# Крестики-нолики
# Компьютер играет в крестики-нолики против пользователя
# глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9
# Инструкция
def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print("""
    Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех вре-
    Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-ноли-
    Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
    доски - так. как показано ниже:
    0|1|2
    -----
    3|4|5
    -----
    6|7|8
    Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сражение.""")

def ask_yes_no(question):
    """Задает вопрос с ответом 'Да' или 'Нет'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
"""
# Доработанная функция
def ask_number(low, high, question=1):
    response = None
    while response not in range(low, high, question):
        response = int(input("Делай свой ход - напиши номер поля (0-8): "))
    return response
"""
def pieces():
    """Определяет принадлежность первого хода."""
    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")
    if go_first =="y":
        print("\nHy что ж. Даю тебе фору: играй крестиками.")
        human = X
        computer = O
    else:
        print("\n Твоя удаль тебя погубит... Буду начинать я.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Создает новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображает иге>овую доску на экране."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "| ", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves (board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя в игре."""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Получает ход человека. """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (О-8):", 0, NUM_SQUARES)
    if move not in legal:
        print("\nCмeшнoй человек! Это поле уже занято. Выбери другое.\n")
    print("Ладно...")
    return move

def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    # создадим рабочую копию доски. потому что функция будет менять некоторые значения в списке
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
    # если следующим ходом может победить компьютер. выберем этот ход
        if winner (board) == computer:
            print(move)
            return move
        # выполнив проверку. отменим внесенные изменения
        board[move] = EMPTY
    # поскольку следующим ходом ни одна сторона не может победить.
    # выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Поздравляе; победителя игры."""
    if the_winner != TIE:
        print("Tpи", the_winner, "в ряд!\n")
    else:
        print("Hичья!\n")
    if the_winner == computer:
        print("Kaк я и предсказывал. победа в очередной раз осталась за мной.\n",
              "Вот еще один довод в пользу того. что компьютеры превосходят людей решительно во всем.")
    elif the_winner == human:
        print("O нет. Этого не может быть! Неужели ты как-то сумел перехитрить меня,белковый? \n",
        "Клянусь: я. компьютер. не допущу этого больше никогда!")
    elif the_winner == TIE:
        print("Teбe несказанно повезло. дружок: ты сумел свести игру вничью. \n",
    "Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить.")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
# запуск программы
main()
input("\n\nНажмите Enter. чтобы выйти.")


# Доступ отовсюду
# Демонстрирует работу с глобальными переменными
def read_global():
    print("В области видимости функции read_global () значение value равно", value)
def shadow_global():
    value=-10
    print("B области видимости функции shadow_global() значение value равно", value)
def change_global():
    global value
    value = -10
    print("B области видимости функции change_global() значение value равно", value)
# основная часть
# value - глобальная переменная. потому что сейчас мы находимся в глобальной области видимости
value = 10
print("B глобальной области видимости значение переменной value сейчас стало равным", value)
read_global ()
print("Вернемся в глобальную область видимости. Здесь value по-прежнему равно", value)
shadow_global()
print("Bepнeмcя в глобальную область видимости. Здесь value по-прежнему равно", value)
change_global()
print("Вернемся в глобальную область видимости. Значение value изменилось на", value)


# День рождения
# Демонстрирует именованные аргументы и значения параметров по умолчанию

# позиционные параметры
def birthday1(name, age):
    print("С днем рождения,", name, "!", "Вам сегодня исполняется", age, "не такли?")

# параметры со значениями по умолчанию
def birthday2(name = "Иванов", age = 1):
    print("С днем рождения,", name, "!", "Вам сегодня исполняется", age, "не так ли?")

birthday1("Иванов", 1)
birthday1(1, "Иванов")
birthday1(name="Иванов", age=1)
birthday1(age=1, name="Иванов")
birthday2()
birthday2(name="Катя")
birthday2(age=12)
birthday2(name="Катя", age=12)
birthday2("Катя", 12)


# Принимай - возвращай
# Демонстрирует параметры и возвращаемые значения
def display(message):
    print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question) :
    """Задает вопрос с ответом 'да' или 'нет ' ."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
# основная часть
display("Baм сообщение.\n")
number = give_me_five()
print("Boт что возвратила функция give_me_five():", number)
answer = ask_yes_no("\nПожалуйста. введите 'у' или 'n':")
print( "Спасибо. что ввели", answer)
input("\n\nHaжмитe Enter. чтобы выйти.")


# Программа «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
# 5 пунктов, которые можно распределить между тремя характеристиками: Сипа, Мудрость
# и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пупа», но и возвращать
# их туда из характеристик, которым он решит присвоить другие значения.
parametr = 5
power = 0
wisdom = 0
dexterity = 0
choice = None

while choice != 0:
    print("""
    О - Выйти               7 - итоговые характеристики
    1 - Добавить силы       4 - Убавить силы        
    2 - Добавить мудрость   5 - Убавить мудрость
    3 - Добавить ловкость   6 - Убавить ловкость
    """)
    choice = input("Baш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания")
        # Расперделение характеристик
    elif choice == "1":
        if parametr != 0:
            parametr -= 1
            power += 1
        else:
            print("Не хватает характеристик")
        print("Теперь Ваша сила", power)
    elif choice == "2":
        if parametr != 0:
            parametr -= 1
            wisdom += 1
        else:
            print("Не хватает характеристик")
        print("Теперь Ваша мудрость", wisdom)
    elif choice == "3":
        if parametr != 0:
            parametr -= 1
            dexterity += 1
        else:
            print("Не хватает характеристик")
        print("Теперь Ваша ловкость", dexterity)
    elif choice == "4":
        if parametr != 0:
            parametr += 1
            power -= 1
        else:
            print("Не хватает характеристик")
        print("Теперь Ваша сила", power)
    elif choice == "5":

        if parametr != 0:
            parametr += 1
            wisdom -= 1
        else:
            print("Не хватает характеристик")
        print("Теперь Ваша мудрость", wisdom)
    elif choice == "6":
        if parametr != 0:
            parametr += 1
            dexterity -= 1
        else:
            print("Не хватает характеристик")
        print("Теперь Ваша ловкость", dexterity)
    elif choice == "7":
        print("Ваши характеристики", "Сила:", power, "Мудрость:", wisdom, "Ловкость:", dexterity)

# Программа, которая будет выводить список слов в случайном порядке. На экране должны печататься
# без повторений все слова из представленного списка.
import random
list = ["меч", "кольчуга", "щит"]
random.shuffle(list)
print(list)

# Виселица
# Классическая игра "Виселица". Компьютер случайным образом выбирает слово.
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток. на экране появится фигурка повешенного.
# Импорт модуля
import random
HANGMAN = ("Осталось семь попыток", "Осталось шесть попыток", "Осталось пять попыток", "Осталось четыре попытки",
           "Осталось три попытки", "Осталось две попытки", "Последняя попытка", "Вы проиграли")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# инициализация переменных
word = random.choice(WORDS) # слово для отгадывания
so_far = "-" * len(word) # по одному дефису на каждую букву. которую надо отгадать
wrong = 0 # количество ошибок. которые сделал игрок
used = [] # буквы, которые игрок уже предлагал
# Соэдание основного цикла
print("Добро пожаловать в игру 'Виселица'. У Вас есть восемь попыток, удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nBы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    # Получение ответа игрока
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Bы уже предлагали букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    # Проверка напичия буквы в слове
    if guess in word:
        print("\nДa! Буква", guess, "есть в слове!")
        # новая строка so_far с отгаданной буквой или буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nK сожалению. буквы", guess, "нет в слове.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nBac повесили!")
else:
    print("\nBы отгадали!")
print("\nБыло загадано слово", word)
input("\n\nHaжмитe Enter. чтобы выйти.")


# Переводчик с гикского на русский
# Демонстрирует использование словарей
geek = {
    "404": "Не знать. не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
    "Googling": "'Гугление', поиск в Сети сведений о ком-либо.",
    "Keyboard Plaque": "Мусор, который скапливается в клавиатуре компьютера.",
    "Link Rot": "Процесс устаревания гиперссылок на веб-страницах. ",
    "Percussive Maintenance":"Когда кто-либо бьет по корпусу неисправного прибора в надежде восстановить его работу.",
    "Uninstalled": "Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов."
}
choice = None
while choice != "0":
    print("""
    Переводчик с гикского на русский
    О Выйти
    1 Найти толкование термина
    2 Добавить термин
    3 Изменить толкование
    4 Удалить термин
    """)
    choice = input("Ваш выбор:")
    print()
    # выход
    if choice == "0":
        print("Дo свидания.")
    # поиск толкования
    elif choice == "1":
        term = input("Какой термин вы хотите перевести с гикского на русский? ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "означает", definition)
        else:
            print("\nYвы. этот термин мне незнаком:", term)
    # добавление термина с толкованием
    elif choice == "2":
        term = input("Какой термин гикского языка вы хотите добавить?")
        if term not in geek:
            definition = input("\nВпишите ваше толкование:")
            geek[term] = definition
            print("\nТермин",term, "добавлен в словарь.")
        else:
            print("\nТакой термин уже есть! Попробуйте изменить его толкование.")
    # новое толкование известного термина
    elif choice == "3":
        term = input("Какой термин вы хотите переопределить? ")
        if term in geek:
            definition = input("Впишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "переопределен.")
        else:
            print("\nТакого термина пока нет! Попробуйте добавить его в словарь.")
    # удаление термина вместе с его толкованием
    elif choice == "4":
        term = input("Какой термин вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин", term, "удален.")
        else:
            print("\nНичем не могу помочь. Термина",term, "нет в словаре.")
    # непонятный пользовательский ввод
    else:
        print("Извините. в меню нет пункта", choice)

# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != "0":
    print("""
    Рекорды 2.О
    О - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    """)
    choice = input("Baш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания.")
    # вывод таблицы рекордов
    elif choice == "1":
        print("Рекорды:\n")
        print("ИМЯ \t РЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # add а score
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # в списке остается только 5 рекордов


# Рекорды
# Демонстрирует списочные методы
scores = []
choice = None
while choice != "0":
    print(
        """
    Рекорды
    О - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    3 - Удалить рекорд
    4 - Сортировать список
    """
    )
    choice = input("Baш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания")
        # вывод лучших результатов на экран
    elif choice == "1":
        print("Peкopды")
        for score in scores:
            print(score)
    # добавление рекорда
    elif choice == "2":
        score = int(input("Bnишитe свой рекорд: "))
        scores.append(score)
    # удаление рекорда
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержится в списке рекордов.")
    # сортировка рекордов
    elif choice == "4":
        scores.sort(reverse=True)


#Арсенал героя 3.0
# Демонстрирует работу со списками
# создадим список с несколькими элементами и выведем его с помощью цикла for
inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("Итaк, в вашем арсенале:")
for item in inventory:
    print(item)
# найдем длину списка
print("Сейчас в вашем распоряжении", len(inventory), "предмета/-ов. ")
# проверка на принадлежность списку с помощью in
if "целебное" in inventory:
    print("Bы еще поживете и повоюете.")
# вывод одного элемента с определенным индексом
index = int(input("\nBвeдитe индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])
# отобразим срез
start = int(input("\nBвeдитe начальный индекс среза: "))
finish = int(input("Bвeдитe конечный индекс среза: "))
print("Cpeз inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
# соединим два списка
chest = ["золото", "драгоценные камни"]
print("Bы нашли ларец. Вот что в нем есть:")
print(chest)
print("Bы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)
# присваиваем значение элементу по индексу
print("Bы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Teпepь ваш арсенал содержит следующие предметы:")
print(inventory)
# удаляем элемент
print("B тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Boт что осталось в арсенале:")
print(inventory)
# удаляем срез
print("Bopы лишили вас арбалета и кольчуги.")
del inventory[: 2]
print("B арсенале теперь только:")
print(inventory)
input ("\nНажмите Enter. чтобы продолжить.")

#130
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#  Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть
# ли какая-либо буква в слове, причем программа может отвечать только «Да» и «Her».
# Вслед за тем игрок должен попробовать отгадать слово.

import random

WORDS=('пирог', 'кошка', 'сложно', 'мышь', 'компьютер')
word= random.choice(WORDS)
correct=word
print('Добро пожаловать в игру! У Вас всего 5 попыток')
print('\nСлово состоит из {} букв'.format(len(word)))
guess=''
guessed=''
hint=5

while hint:
    guess=input('\nВаш ответ: ')
    if guess.lower() in word:
        print('Да, Вы угадали ')
        guessed+=guess
        print('\nВы угадали эти буквы: ', guessed)
        hint-=1
    else:
        print('\nsИзвините, это не так')
        hint-=1
        print('\nВы угадали эти буквы: ', guessed)
guess=input('\nТеперь попробуем отгадать всё слово: ')
if guess.lower()==correct:
    print('\nВы выиграли! это слово: ', correct)
   
else:
    print('\nВы проиграли( Это слово: ', correct)
input('\nНажмите Enter')


# Анаrраммы (Доработанная с количеством попыток)
# Компьютер выбирает какое-либо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово
import random
#Последовательность слов из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
#Выбор случайным образом одно слово из последовательности 
word = random.choice(WORDS)
#Переменная с которой будет затем составлена версия игрока
correct = word
#Пустая строка для анаграммы
jumble = " "
mistakes = 1
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
#Начало игры
print ("Добро пожаловать в игру 'Анаграммы'! Здесь Вам необходимо переставить буквы так, чтобы получилось слово.")
print("Вот анаграмма: ", jumble)
#Получение пользовательского кода 
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != " ":
    mistakes += 1
    print("К сожалению, этого слова нет")
    guess = input("попробуйте отгадать ещё раз: ")
    
if guess == correct:
    print("Да, именно так! Вы отгадали! Ваше количество попыток: ", mistakes)
print("Спасибо за игру!")

#Программа которая меняет текст наоборот
word = str(input("Введите текст:"))
finish = ""
for i in word[::-1]:
    finish = finish + word
print(finish)

#Считательная прог-ма 
start = int(input("Введите начало отсчета: "))
finish = int(input("Введите конец отсчета: "))
for i in range (start,finish):
    print(i, end=" ")

# Анаrраммы 
# Компьютер выбирает какое-либо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово
import random
#Последовательность слов из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
#Выбор случайным образом одно слово из последовательности 
word = random.choice(WORDS)
#Переменная с которой будет затем составлена версия игрока
correct = word
#Пустая строка для анаграммы
jumble = " "
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
#Начало игры
print ("Добро пожаловать в игру 'Анаграммы'! Здесь Вам необходимо переставить буквы так, чтобы получилось слово.")
print("Вот анаграмма: ", jumble)
#Получение пользовательского кода 
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != " ":
    print("К сожалению, этого слова нет")
    guess = input("попробуйте отгадать ещё раз: ")
if guess == correct:
    print("Да, именно так! Вы отгадали!")
print("Спасибо за игру!")

#Арсенал героя 2.0
# Демонстрирует работу с кортежами
# создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = ("меч" ,   
            "кольчуга",
            "щит",
            "целебное снадобье")
print("\nИтак . в вашем арсенале ")
for item in inventory:
    print (item) 
input("\nНажмите Enter. чтобы продолжить.")
print("Сейчас в вашем распоряжении" , len(inventory) , "предмета/-ов.")

start = int(input("Введите начальный индекс:"))
finish = int(input("Введите конечный индекс:"))
print("Срез inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])

#Арсенал героя
inventory = ()
# рассмотрим его как условие
if not inventory:
    print ( "Вы безоружны. " ) 
input("\nНажмите Enter, чтобы продолжить.")
# теперь создадим кортеж с несколькими элементами
inventory = ("меч",
            "кольчуга",
            "щит",
            "целебное снадобье")
# выведем этот кортеж на экран
print ( "\nСодержимое кортежа: ")
print (inventory)
# выведем все элементы последовательно
print("\nИтак. в вашем арсенале:")
for item in inventory:
    print (item)
#input( "\n\nНажмите Enter, чтобы выйти")

# Резчик пиццы
# Демонстрирует срезы строк
word = "пицца"
print(
#Памятка
#0   1   2   3   4   5 
#+---+---+---+---+---+
#| п | и | ц | ц | а |
#+---+---+---+---+---+
#-5  -4  -3 -2  -1
)
print ("Введите начальный и конечный индексы для того среза 'пиццы', который хотите получить.")
print ("Для выхода нажмите Enter. не вводя начальную позицию ")
start = None
while start != "":
    start = (input("\nНачальная позиция: "))
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("Срез word[", start, ":", finish, "]выглядит как", end=" ")
        print(word[start:finish]) 
input("\n\nНажмите Enter. чтобы выйти.")

# Только согласные
#Демонстрирует. как создавать новые строки из исходных с помощью цикла for
message = input("Введите текст: ")
new_message = ""
VOWELS = "аеiоuаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Создана новая строка ", new_message) 
print("\nBoт ваш текст с изъятыми гласными буквами:", new_message) 

#Случайный индекс
import random
word = "слово"
print ("В переменной word хранится слово: ", word , "\n")
high = len(word)
low = - len(word)
for i in range(10):
    position = random.randrange(low, high)
    print ( "word[", position, "]\t", word[position]) 

#Анализатор текста 
message = input("Введите текст: ")
print ( "\nДлина введенного вами текста составляет:", len(message))
print( "\nСамая частая согласная , 'w' , ")
if "w" in message: 
    print("встречается в вашем тексте.")
else:
    print("нe встречается в вашем тексте.")
input("\n\nHaжмитe Enter. чтобы выйти.") 

# Считалка
print("Посчитаем")
for i in range(10):
    print(i, end=" ")
print("Перечислим числа кратные пяти:")
for i in range(0, 50, 5):
    print(i, end=" ")
print("Посчитаем числа в обратном порядке")
for i in range(10, 0, -1):
    print(i, end=" ")

#Слово по буквам 
word = input("Введите слово: ")
print("\noВот все буквы вашего слова")
for letter in word:
    print(letter)

# Программа "Отгадай число"
# Игрок пытается отгадать случайное число где прог-ма говорит больше или меньше , а также  количество попыток
# Кол-во попыток ограничено
import random

print('Игра "Отгадай число"')

the_number = random.randint(1,100)
guess=int(input("Ваше число: "))
tries=1

while guess !=the_number:
    if tries >=3:
        print("Вы не справились(")
        break
        
    elif guess > the_number:
        print("Ваше число меньше")
    else:
        print("Ваше число больше")
    guess=int(input("Ваше число: "))
    tries += 1
    
print("Ваше кол-во попыток: ", tries)

#Условная монета
import random

podbros = random.randint(1,2)
eagle = 0
tails = 0
kol_podbros = 0
while kol_podbros !=100:
    kol_podbros +=1
    podbros = random.randint(1,2)
    if  podbros == 1:
        eagle += 1
    else:
        tails +=1
print("Орёл: ", eagle, "Решка: ", tails )

# Симулятор пирожка с сюрпризом
import random

print("Хотите узнать какой пирожок вас ждет?")
number = random.randint(1,5)

if  number == 1:
    print("Пирожок с капустой")
elif number == 2:
    print("Пирожок с картошкой")
elif number == 3:
    print("Пирожок с мясом")
elif number == 3:
    print("Пирожок с ягодой")
else:
    print("Без пирожка")


# Программа "Отгадай число"
# Игрок пытается отгадать случайное число где прог-ма говорит больше или меньше , а также  количество попыток
import random

print('Игра "Отгадай число"')

the_number = random.randint(1,100)
guess=int(input("Ваше число: "))
tries=1

while guess !=the_number:
    if guess > the_number:
        print("Ваше число меньше")
    else:
        print("Ваше число больше")
    guess=int(input("Ваше число: "))
    tries += 1
print("Ваше кол-во попыток: ", tries)


print("\tЭксклюзивная компьютерная сеть")
security = 0
username = ""
while not username :
    username = input("Логин: ")
password = ""
while not password :
    password = input("Пapoль: ")
if username == "M.Dawson" and password == "secret" : 
    print("Привет Майк ")
    security = 5
elif username == "S.Meier" and password == "civilization": 
    print("Здравствуй Сид")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros" : 
    print("Дoбporo времени суток Сигеру")
    security = 3
elif username == "W.Wright" and password == "thesims": 
    print("Kaк дела Уилл?")
    security = 3 
elif username == "guest" or password == "guest": 
    print("Дoбpo пожаловать к нам в гости.")
    security = 1
else:
    print( "Войти в систему не удалось. Должно быть. вы не очень-то эксклюзивный гражданин.") 

'''



# total = 386
# no_total = 277
# old = int(input("Ваша начальная страница:"))
# new = int(input("Ваша последняя страница: "))
# passed = new - old
# answer = total - new
# no_all = no_total - new
# print("Вы прошли ", passed, "страниц")
# print("Вам осталось ", answer, " страниц")
# print("Если не считать графику, то Вам осталось:", no_all)