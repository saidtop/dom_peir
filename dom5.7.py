import random 
man = {'деньги' :500}
bitcoin = {"курс" :0}
efir = {'курс' :0}
while True:
    bitcoin['курс'] = random.randint(0,100)
    efir['курс'] = random.randint(0,100)
    print("курс биткоина равен:" ,bitcoin)
    print("курс ефира равен:" ,efir)
    kriptovaluta=int(input("""что вы хотите купить?
    1.Биткоин
    2.Эфир
    3.Биткоин и эфир
    :"""))
    if kriptovaluta ==1 :
        man['деньги'] -= bitcoin['курс']
        print("Ваш баланс после покупки биткоина:" , man['деньги'])
        bitcoin['курс_1'] = random.randint(0,100)
        man['деньги'] += bitcoin['курс_1'] 
        man['деньги'] -= bitcoin['курс'] 
        print("Ваш баланс после изменения курса на биткоин:" , man['деньги'])
    elif kriptovaluta ==2 :
        man['деньги'] -= efir['курс']
        print("Ваш баланс после покупки эфира:" , man['деньги'])
        efir['курс_1'] = random.randint(0,100)
        man['деньги'] += efir['курс_1'] 
        man['деньги'] -= efir['курс'] 
        print("Ваш баланс после изменения курса на эфир:" , man['деньги'])
    elif kriptovaluta ==3:
        man['деньги'] -= bitcoin['курс'] 
        man['деньги'] -=  efir['курс']
        print("Ваш баланс после покупки биткоина и эфира:" , man['деньги'])
        bitcoin['курс_1'] = random.randint(0,100)
        efir['курс_1'] = random.randint(0,100)
        bitcoin['курс_1'] -= bitcoin['курс']
        efir['курс_1'] -= efir['курс']
        man['деньги'] += bitcoin['курс_1']
        man['деньги'] += efir['курс_1']
        print("Ваш баланс после изменения курса на эфир и биткоин:" , man['деньги'])
    else:
        print("щас бы по кнопкам не попадать")
        break
    if man['деньги'] >= 1000:
        print("Вау да ты лакерок , но предел все таки надо знать ")        
        break
    elif man['деньги'] <= 0:
        print("Вы банкрот :((((  HELLO DARKNESS SMILE FRIEND I CAN TO TAKE THIS YOU AGAIN")
        break
    

