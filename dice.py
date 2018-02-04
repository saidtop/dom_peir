import random
player_one = {'счет': 1000}
player_two = {'счет': 1000}

player_one['лет'] = int(input("Сколько вам лет:"))
player_two['лет'] = int(input("Сколько вам лет:"))


if player_one['лет'] >= 18 and player_two['лет'] >= 18:
    print("Проходите")
else:
    print("ахаха:) малышня вам еще расти и расти")
    exit()

player_one['имя'] = input('Имя первого игрока: ')
player_two['имя'] = input('Имя второго игрока: ')
while True:
    
    player_one['ставка'] = int(input(player_one['имя']  +  " ставит: "))
    player_two['ставка'] = int(input(player_two['имя']  +  " ставит: "))
    

    if player_one['ставка'] > player_two['счет'] :
        player_one['ставка'] =  player_two['ставка']
    elif player_two['ставка'] > player_one['счет']:
        player_two['ставка'] = player_one['ставка']
    

    if player_one['счет'] < player_one['ставка']:
        print(" воу воу у вас "+ player_one['имя'] + " нет столько денег")        
        break
    elif  player_two['ставка'] > player_two['счет']:
        print(" воу воу у вас "+ player_two['имя'] + " нет столько денег")
        break



    player_one['бросок'] = random.randint(2, 12)
    player_two['бросок'] = random.randint(2, 12)

    print(player_one['имя']  + ' выпало ', player_one['бросок'], 'очков')
    print(player_two['имя']  + ' выпало ', player_two['бросок'], 'очков')

    if player_one['бросок'] > player_two['бросок']:
        print(player_one['имя']  + " выиграл ставку")
        player_one['счет'] += player_two['ставка']
        player_two['счет'] -= player_two['ставка']  
    elif player_one['бросок'] < player_two['бросок']:
        print(player_two['имя'] + " выиграл ставку")
        player_two['счет'] += player_one['ставка']
        player_one['счет'] -= player_one['ставка']
    else:
        print("Ничья")

    print(player_one['имя'] + " на счету ", player_one['счет'])
    print(player_two['имя']  + " на счету ", player_two['счет'])

    if player_one['счет'] <= 0:
        print(player_one['имя']  + " обанкротился " +  player_two['имя']  +  " выиграл ")
        break
    elif player_two['счет'] <= 0:
        print(player_two['имя'] + ' обанкротился ' +  player_one['имя'] + '  выиграл ')
        break