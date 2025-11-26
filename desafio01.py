nome = input("Digite seu nome: ")
print(f'Olá {nome}. Em janeiro você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10')
cupom = input('Informe o cupom de desconto: ')
valor_compra = 500
desconto = 500 * 0.1
print(f"Sua compra de R${valor_compra}, e você teve um desconto de R${desconto} com o cupom. Valor final R${valor_compra - desconto}")