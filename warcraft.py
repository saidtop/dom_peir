import random
def statistics():
    person = { "Damage" :15,
    "hp":100,
    "protection" :0,
    "kritical" :0,
    "heal" :0
    }
    person['gender'] = int(input("""Ваш пол:
        1.Мужской
        2.Женский
        :"""))   
    if person["gender"] ==1:
        person["hp"] +=5
        person['Damage'] +=5
    elif person["gender"] ==2:
        person["hp"] +=10
        person['Damage'] +=0
    else:
        print('походу вы гермафродит')
        exit()
    person['fraction'] = int(input("""Выберите фракцию:
        1.Aliens
        2.Horde
        :"""))
    if person['fraction'] ==1:
        person['race'] = int(input("""Выберите расу:
            1.Люди
            2.Дворфы
            3.Ночные эльфы
            4.Гномы
            5.Дреней
            6.Воргены
            7.Пандарены
            :"""))
        if person['race'] ==1:
            person['Damage'] +=5
            person["hp"] +=5
            person["protection"] +=5
            person["kritical"] +=5        
        elif person["race"]==2:
            person['Damage'] +=0
            person["hp"] +=10
            person["protection"] +=10
            person["kritical"] +=0        
        elif person["race"] ==3:
            person['Damage'] +=3
            person["hp"] +=8
            person["protection"] +=8
            person["kritical"] +=1        
        elif person["race"] ==4:
            person['Damage'] +=5
            person["hp"] +=15
            person["protection"] +=0
            person["kritical"] +=0        
        elif person["race"] ==5:
            person['Damage'] +=6
            person["hp"] +=6
            person["protection"] +=3
            person["kritical"] +=5       
        elif person["race"] ==6:
            person['Damage'] +=5
            person["hp"] +=0
            person["protection"] +=0
            person["kritical"] +=15
        elif person["race"]==7:
            person['Damage'] +=5
            person["hp"] +=10
            person["protection"] +=5
            person["kritical"] +=0
        else:
            print("вы не туда нажали,попробуйте заного")
            exit()
    elif person['fraction'] ==2:
        person['race'] = int(input("""Выберите расу:
            1.Орки
            2.Нежить
            3.Таурены
            4.Тролли
            5.Эльфы крови
            6.Гоблины
            7.Пандарены
            :"""))
        if person['race'] ==1:
            person['Damage'] +=5
            person["hp"] +=5
            person["protection"] +=5
            person["kritical"] +=5        
        elif person["race"] ==2:
            person['Damage'] +=0
            person["hp"] +=10
            person["protection"] +=10
            person["kritical"] +=0        
        elif person["race"] ==3:
            person['Damage'] +=3
            person["hp"] +=8
            person["protection"] +=8
            person["kritical"] +=1        
        elif person["race"] ==4:
            person['Damage'] +=5
            person["hp"] +=15
            person["protection"] +=0
            person["kritical"] +=0  
        elif person["race"] ==5:
            person['Damage'] +=6
            person["hp"] +=6
            person["protection"] +=3
            person["kritical"] +=5
        elif person["race"] ==6:
            person['Damage'] +=5
            person["hp"] +=0
            person["protection"] +=0
            person["kritical"] +=15
        elif person["race"] ==7:
            person['Damage'] +=5
            person["hp"] +=10
            person["protection"] +=5
            person["kritical"] +=0
    else:
        print("вы не туда нажали,попробуйте заного")
        exit()
    person['klass'] = int(input("""Выберите класс:
        1.Воин
        2.Паладин
        3.Охотник
        4.Разбойник
        5.Жрец
        6.Рыцарь смерти
        7.Шаман
        8.Маг
        9.Чернокнижник
        10.Монах
        11.Друид
        12.Охотник на демонов
        :"""))
    if person['klass'] ==1:
        person["Damage"] +=5
        person["hp"] +=5
        person["protection"] +=20
        person['kritical'] +=0
        person["heal"] +=0
    elif person['klass'] ==2:
        person["Damage"] +=5
        person["hp"] +=5
        person["protection"] +=5
        person['kritical'] +=0
        person["heal"] +=15
    elif person['klass'] ==3:
        person["Damage"] +=10
        person["hp"] +=10
        person["protection"] +=0
        person['kritical'] +=10
        person["heal"] +=0
    elif person['klass'] ==4:
        person["Damage"] +=15
        person["hp"] +=0
        person["protection"] +=0
        person['kritical'] +=15
        person["heal"] +=0   
    elif person['klass'] ==5:
        person["Damage"] +=0
        person["hp"] +=5
        person["protection"] +=0
        person['kritical'] +=0
        person["heal"] +=25
    elif person['klass'] ==6:
        person["Damage"] +=10
        person["hp"] +=2
        person["protection"] += 10
        person['kritical'] +=8
        person["heal"] +=0    
    elif person['klass'] ==7:
        person["Damage"] +=8
        person["hp"] +=6
        person["protection"] +=0
        person['kritical'] +=8
        person["heal"] +=8   
    elif person['klass'] ==8:
        person["Damage"] +=20
        person["hp"] +=0
        person["protection"] +=0
        person['kritical'] +=10
        person["heal"] +=0   
    elif person['klass'] ==9:
        person["Damage"] +=40
        person["hp"] +=-5
        person["protection"] +=0
        person['kritical'] +=0
        person["heal"] +=-5   
    elif person['klass'] ==10:
        person["Damage"] +=5
        person["hp"] +=5
        person["protection"] +=5
        person['kritical'] +=5
        person["heal"] +=10
    elif person['klass'] ==11:
        person["Damage"] +=7
        person["hp"] +=7
        person["protection"] +=7
        person['kritical'] +=3
        person["heal"] +=7
    elif person['klass'] ==12:
        person["Damage"] +=10
        person["hp"] +=7
        person["protection"] +=13
        person['kritical'] +=0
        person["heal"] +=0
    else:
        print("нету такого класса")
        exit()
    person['name'] = input('Введите имя персонажа: ')
    return person
def fight(Damager, defender ):
    krit = {"kritical" : 0}
    health = {"heal":0}
    real_damage = (Damager['Damage'] + krit["kritical"] + random.randint(-10,20))- (defender["protection"] + health["heal"])
    defender["hp"] -= real_damage
def health_info(person):
    print('У', person['name'], 'осталось', person['hp'], 'здоровья')
print("""Приветствую тебя в игре 
  "Варкрафт в пери" """)
player_1 = statistics()
player_2 = statistics()

while True:
    fight(player_1, player_2)
    fight(player_2, player_1)

    health_info(player_1)
    health_info(player_2)
    
    if player_1['hp'] <= 0:
        print(player_1['name'], 'сдох')
        break
    if player_2['hp'] <= 0:
        print(player_2['name'], 'сдох')
        break
    
    b = input()
    if b=="89280520039":
        print("""Султанмурад и Саид захватили игру 
            ваши попытки убить его были тщетны.
            Мир пал под их натиском.""")
        break


