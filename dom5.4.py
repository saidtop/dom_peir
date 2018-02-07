name_4 = []
name_2 = {"участников набрано" : 0}
while name_2['участников набрано'] != 3:
    name = input("введите ваше имя:")
    matan = int(input("Какая у вас оценка по математике:"))
    chemistry =  int(input("Какая у вас оценка по химий:"))
    geography =  int(input("Какая у вас оценка по географий:"))
    physics = int(input("Какая у вас оценка по физике:"))
    biology = int(input("Какая у вас оценка по биологий:"))
    name_1 = (matan+ chemistry + geography + physics + biology)/5
    if name_1 >= 4.8 and name_1 < 5.1:
        print(name + " вы нам подходите")
        name_2["участников набрано"] += 1
        name_4.insert(0, name)
    elif name_1 >= 5.1:
        print("земля тебе пухом ,нас не обманешь")
    else:
        print("Извините,но нам нужны знатоки ")
print("Победители конкурса" , name_4)
    
   

        