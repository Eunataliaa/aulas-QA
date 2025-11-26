import os


def manipulacao():
    #Criando um novo diretório
    os.mkdir("diretorio_os")

    #Criando uma lista com dados de jogadores
    dados_jogadores = [
        ["Neymar", 32, "Atacante"],
        ["Alisson", 32, "Goleiro"],
        ["Marquinhos", 30, "Zagueiro"],
        ["Casemiro", 32, "Volante"],
        ["Vinicius Jr", 24, "Atacante"]
    ]

    #Salvando os dados em um arquivo txt
    with open("dados_jogadores.txt", "w", encoding="utf-8") as arquivo:
        for jogador in dados_jogadores:
            linha = ", ".join(map(str, jogador))
            arquivo.write(linha + "\n")

    #Movendo o arquivo txt para a nova pasta
    os.rename("dados_jogadores.txt", "diretorio_os/dados_jogadores.txt")
    
    #Salvando o caminho do diretório atual
    diretorio_principal = os.getcwd()

    #Salvando o caminho do diretório criado
    novo_diretorio = "diretorio_os"
    caminho_novo_diretorio = os.path.join(diretorio_principal, novo_diretorio)

    #Listando o arquivo movido para o novo diretório
    arquivos = os.listdir(caminho_novo_diretorio)
    for arquivo in arquivos:
        print('\n')
        print(arquivo)
        print('\n')

#Chamando a função para gerar todo processo do exercício
manipulacao()