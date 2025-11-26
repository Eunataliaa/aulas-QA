idade = int(input("Informe sua idade: "))

if idade >= 18:
    print(f'Você tem {idade} anos e já é maior de idade. Você já possuí a idade miníma para dirigir!')

elif idade >= 17:
    print(f'Você tem entre 17 e 18 anos e ainda NÃO está apto para dirigir')

else:
    print(f'Você tem {idade} anos e é menor de idade. Você não possuí a idade miníma para dirigir!')