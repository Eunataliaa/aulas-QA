

lista_matricula = []

while len(lista_matricula) < 5:
    try:
        matricula = int(input("Infome o número da matrícula: "))
        if matricula not in lista_matricula:
            lista_matricula.append(matricula)
            print(f'Matrícula {matricula} cadastrada com sucesso!\n')
        else:
             print("Matrícula já cadastrada!")
    
    except ValueError:
         print("Erro! Informe somente números inteiros!")

print('Sua lista de matrícula já está cheia!\n')

def validar_matricula(lista_matricula):
    for matricula in lista_matricula:
            if matricula % 2 == 0:
                print(f'A matrícula {matricula} é par!')
            else:
                print(f'A matrícula {matricula} é ímpar!')

validar_matricula(lista_matricula)