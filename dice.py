import  random 

player_1 = {'счет': 1000}
player_2 = {'счет': 1000}

player_1['имя'] = input('Имя первого игрока: ')
player_2['имя'] = input('Имя второго игрока: ')

while True:
	player_1['ставка'] = int(input(player_1['имя'] + " ваша ставка: "))
	player_2['ставка'] = int(input(player_2['имя'] + " ваша ставка: "))

	player_1 ['бросок'] = random.randint(2,12)
	player_2 ['бросок'] = random.randint(2,12)

	print(player_1['имя'], "выбил", player_1['бросок'], 'очков')
	print(player_2['имя'], "выбил", player_2['бросок'], 'очков')


	if player_1['бросок'] > player_2['бросок']:
		player_1['счет'] += player_2 ["ставка"]
		player_2['счет'] -= player_1 ["ставка"]
		print(player_1['имя'], "выиграл ставку")

	elif player_1['бросок'] < player_2['бросок']:
		player_2['счет'] += player_1 ["ставка"]
		player_1['счет'] -= player_2 ["ставка"]
		print(player_2['имя'], "выиграл ставку")
	else:
		print("ничья")
	print("Счёт", player_1['имя'] , player_1["счет"])
	print("Счёт", player_2['имя'] , player_2["счет"])



	
