nome = input("Digite seu nome: ")

nota1 = float(input('Informe sua 1º nota: '))
nota2 = float(input('Informe sua 2º nota: '))
nota3 = float(input('Informe sua 3º nota: '))
nota4 = float(input('Informe sua 4º nota: '))

nota_final = (nota1 + nota2 + nota3 + nota4) / 4

if nota_final >= 7:
    print(f'Parabéns {nome}, sua média foi {nota_final}, você foi aprovado!')
elif nota_final >= 5:
    print(f'Olá {nome}, sua média final foi {nota_final}, você está de recuperação!')
else:
    print(f'Olá {nome}, sua média final foi {nota_final}, você foi reprovado!')

