nome = input("Informe seu nome: ")
idade = int(input('Informe sua idade: '))
altura = float(input('Informe sua altura em metros: '))

nota1 = float(input('Informe sua 1ª nota: '))
nota2 = float(input('Informe sua 2ª nota: '))
soma_notas = float(nota1 + nota2)

info = print(f'Olá {nome}, você tem {idade} anos e tem {altura} metros de altura. A soma de suas notas é {soma_notas}')
print(info)
