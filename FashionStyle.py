

nome = input('Informe seu nome: ')
valor_compra = float(input('Informe o valor da sua compra: '))

if valor_compra >= 500.0:
        print(f'Parabéns {nome}. Você ganhou um super desconto de 30%. O valor do seu desconto é de R${valor_compra * 0.3:.2f}') 


elif valor_compra >= 250.0:
    print(f'Parabéns {nome}. Você ganhou 10% de desconto, mas pode ganhar 30% se sua compra for acima de R$500')

else:
       print(f'Poxa {nome}, falta pouco para você ganhar 10% de desconto em sua compra.')