
# 1. функция произведения
def multiply(a, b):
    print(f'произведениe чисел a = {a}, b = {b} равно {a*b}')

a = int(input('Введите положительное число а: '))
b = int(input('Введите положительное число b: '))
multiply(a, b)



# 2. Напишите класс Calculator со следующими методами
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def subtract(self):
        print(f'subtract равен {self.a-self.b}')

    def multiply2(self):
        print(f'multiply равен {self.a*self.b}')

    def divide(self):
        print(f'divide равен {self.a//self.b}')

a = int(input('Введите положительное число а: '))
b = int(input('Введите положительное число b: '))
data1 = Calculator(a, b)
data1.multiply2()
data1.subtract()
data1.divide()



#3.  "Привет, я Адам, моя почта adam@gmail.com и у меня есть мечта "
class User:
    def __init__(self, name, mail, dream):
        self.name = name
        self.mail = mail
        self.dream = dream

    def texts(self):
        print(f'Привет, я {self.name}, моя почта {self.mail} и у меня есть мечта {self.dream}')

name, mail, dream = input('Введите имя '), input('Введите почту '), input('Введите мечту ')
data = User(name, mail, dream)
data.texts()