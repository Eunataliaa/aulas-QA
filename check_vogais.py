

def check_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    qtde_vogais = 0
    
    for letra in palavra:
        if letra in vogais:
            qtde_vogais +=1
        else:
            pass

    print(f'A palavra {palavra} tem {qtde_vogais} vogal(is)!')

palavra = input("Informe um palavra: ")        
check_vogais(palavra)

