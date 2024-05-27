import time
VladimerPutin = "владимир путин"
Jakarta = "джакарта"
Arachnophobia = "арахнофобия"
BreakDown = "сломается"
Owl = "сова"
MaxPoints = 5
Counter = 0

print("добро пожаловать в игру 'викторина'")
print("правила игры:")
print("мы задоем вапросы, а вы стараетесь на них ответеть")
time.sleep(2.5)
print()
print("1. Кто призидент России?")

answerFirstQuestion = input()

if answerFirstQuestion == VladimerPutin:
    print("Правильно")
    Counter + 1
else:
    print("Не правильно")

time.sleep(1)
print("2. Напишите столицу индонезии")

answerSecondQuestion = input()

if answerSecondQuestion == Jakarta:
    print("Правильно")
    Counter + 1
else:
    print("Не правильно")

time.sleep(1)
print("3. Как називаеться фобия боязни пауков?")

answerThirdQuestion = input()

if answerThirdQuestion == Arachnophobia:
        print("Правильно")
        Counter + 1
else:
        print("Не правильно")

time.sleep(1)
print("4. вставте пропушеное слово: Нoвaя мeтлa пo-нoвoмy мeтёт, a кaк (...) — пoд лaвкoй вaляeтcя.")

answerFourthQuestion = input()

if answerFourthQuestion == BreakDown:
    print("Правильно")
    Counter + 1
else:
    print("Не правильно")

time.sleep(1)
print("5. Отгадай загатку: У неё глаза большие, хищный клюв – всегда крючком. По ночам она летает, спит на дереве лишь днём.")

answerFifthQuestion = input()

if answerFifthQuestion == Owl:
        print("Правильно")
        Counter + 1
else:
        print("Не правильно")

if Counter == MaxPoints:
    print("поздровляю вы ответили правильно на все вопросы")