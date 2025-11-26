

def simulador_catraca():
   
    frequencia = 0
    dia_do_mês = 1

    while frequencia < 21:
        select = int(input("Seja Bem-Vindo à academia JUNTOFIT\n" \
        "Escolhe uma opção no menu: \n" 
        "1- Confirmar Entrada!\n" \
        "2- Atualizar Cadastro!\n" \
        "3- Alterar forma de pagamento!\n"))


        if select == 1:
            print(f'\nSua entrada em {dia_do_mês} de outubro foi confirmada. Você está participando da nossa promo Treina Junto')
            frequencia += 1
            dia_do_mês +=1
            print(f'Quantidade de dias seguidos: {frequencia}')
            print('\n')

        elif select == 2:
            print('Suas informações foram atualizadas!')

        elif select == 3:
            print('Forma de pagamento alterada com sucesso!')

    if frequencia >= 21:
        print(f'Parabéns. Você teve uma frequencia de {frequencia} dias seguidos.'\
            'Agora você pode presentear um amigo ou amiga para treinar com você\n')

simulador_catraca()