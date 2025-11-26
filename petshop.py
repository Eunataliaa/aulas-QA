nome = input('Informe o nome do seu dog: ')
idade = int(input("Informe a idade humana em anos do seu dog: "))
idade_real = idade * 7

print(f'A idade do seu dog, em anos de cachorro é {idade_real} ')


qtde_banhos = int(input('Informe a quantidade de banhos por ano do seu dog: '))
porte_dog = input('Informe o porte do seu dog em: Grande, Medio ou Pequeno: ' ).lower()


if porte_dog == 'grande': 
    banho = 75
    custo = 20
    lucro = (banho - custo) * qtde_banhos
    print(f'Olá, {nome} tem {idade_real} e nos últimos 12 meses o lucro desse animal foi de R${lucro:.2f}')
    
elif porte_dog == 'medio':
    banho = 60
    custo = 15
    lucro = (banho - custo) * qtde_banhos
    print(f'Olá, {nome} tem {idade_real} e nos últimos 12 meses o lucro desse animal foi de R${lucro:.2f}')
    
elif porte_dog == 'pequeno':
    banho = 50
    custo = 5
    lucro = (banho - custo) * qtde_banhos
    print(f'Olá, {nome} tem {idade_real} e nos últimos 12 meses o lucro desse animal foi de R${lucro:.2f}')

