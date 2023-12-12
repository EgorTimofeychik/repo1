#задание 1
from datetime import datetime

def working_hours_only(func):
    def wrapper():
        current_hour = datetime.now().hour
        if current_hour >= 9 and current_hour < 18:
            func()
        else:
            print("Работать нельзя!")
    return wrapper

@working_hours_only
def work():
    print("Работаем")

work()

#задание 2
def type_chek(correct_type):
    def func2(func):
        def wrapper(arg):
            if type(arg) == correct_type:
                return func(arg)
            else:
                return 'Bad type'
        return wrapper
    return func2

@type_chek(int)
def times2(num):
    return num * 2

print(times2(2))
print(times2(True))

@type_chek(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(1.5))

print(first_letter(1.5))