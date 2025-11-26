import math

valor = int(input('Informe um valor: '))
raiz_quadrada = math.sqrt(valor)
raiz_cubica = math.cbrt(valor)

print(f'O dobro do valor informado é: {valor * 2:.2f}')
print(f'O triplo do valor informado é: {valor * 3:.2f}')
print(f'O valor informado ao quadrado é: {valor ** 2:.2f}')
print(f'A raiz quadrada do valor informado é: {raiz_quadrada:.2f}')
print(f'A raiz cúbica do valor informado é: {raiz_cubica:.2f}')