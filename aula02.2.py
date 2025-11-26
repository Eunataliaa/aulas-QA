import math

valor = int(input('Informe um valor: '))
raiz_quadrada = math.sqrt(valor)
raiz_cubica = math.cbrt(valor)

print(f'O dobro do valor informado é: {valor * 2}')
print(f'O triplo do valor informado é: {valor * 3}')
print(f'O valor informado ao quadrado é: {valor ** 2}')
print(f'A raiz quadrada do valor informado é: {raiz_quadrada}')
print(f'A raiz cúbica do valor informado é: {raiz_cubica:.2f}')