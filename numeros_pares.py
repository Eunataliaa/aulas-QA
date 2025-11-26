"""
qtd_total = 0

for number in range(1,1001):
    if number % 2 == 0:
        print(number)
        qtd_total += 1 
        
print(f'A quantidade de números pares entre 0 e 1000 é {qtd_total}')
"""

def teste():
    qtd_total = 0
    qtde_impar = 0
    for number in range(0,1001):
        if number % 2 == 0:
            print(f'Par: {number}')
            qtd_total += 1 
        else:
            print(f'Ímpar: {number}')
            
    print(f'A quantidade de números pares entre 0 e 1000 é {qtd_total}')

print(teste())
