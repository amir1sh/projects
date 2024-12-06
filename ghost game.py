from random import randint
print('Игра ПривидениЯ')
feeling_brave=True
score=0
while feeling_brave:
    ghost_door=randint(1,3)
    print('Перед вами 3 двери')
    print('Привидение за какой-то из них')
    print('Какую дверь вы откроете?')
    door=input('1,2 или 3: ')
    door_num=int(door)
    if door_num==ghost_door:
        print('ПРИВИДЕНИЕ!!!')
        print('Беги от сюда!')
        print('ИГРА ОКОНЧНА!') 
        feeling_brave=False
    else:
        print('Нет привидения, вы переходите в следующую комнату ')
        print('')
        score=score+1
    if score==5:
        print('ПОЗДРАВЛЯЮ!!! ВЫ ВЫШЛИ ИЗ ЗАМКА')
        feeling_brave=False
print('Ваш счет',score)

