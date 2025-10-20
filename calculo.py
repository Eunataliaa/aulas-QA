# Entrada do usuário
valor = float(input("Digite um valor: "))

# Cálculos
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor ** 0.5
raiz_cubica = valor ** (1/3)

# Saídas
print(f"Resultados para o valor {valor}:")
print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"Ao quadrado: {quadrado}")
print(f"Raiz quadrada: {raiz_quadrada:.2f}")
print(f"Raiz cúbica: {raiz_cubica:.2f}")