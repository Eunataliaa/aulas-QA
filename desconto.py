# formulario
nome_pet = input("Digite o nome do pet: ")
idade_humana_pet = int(input("Digite a idade humana do pet: "))
porte = input("Digite o porte (P/M/G): ").upper()
quantidade_banhos = int(input("Quantos banhos em 12 meses: "))


# consideracao cada ano de idade do cachorro
idade_cachorro = idade_humana_pet * 7


# script 
if porte == "G":
    lucro_total = quantidade_banhos * (75 - 20)
elif porte == "M":
    lucro_total = quantidade_banhos * (60 - 15)
elif porte == "P":
    lucro_total = quantidade_banhos * (50 - 5)
else:
    print("Porte inválido!")
    exit()

# retorno
print(f"Olá, {nome_pet} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}")