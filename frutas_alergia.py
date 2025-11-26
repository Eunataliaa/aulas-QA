frutas = ['maça', 'banana', 'uva', 'goiaba', 'manga']
alergia = ['banana']

for fruta in frutas:
    if fruta in alergia:
        print(f'A fruta {fruta} está na lista de frutas alérgicas!')
        print('\n')
    else:
        print(f'A fruta {fruta} não está na lista de frutas alérgicas!')
        print('\n')