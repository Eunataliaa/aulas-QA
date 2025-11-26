import pandas as pd

alunos = {
     1: {"nome": "Ana Silva", "idade": 20},
     2: {"nome": "Bruno Santos", "idade": 22},
     3: {"nome": "Carlos Oliveira", "idade": 19},
     4: {"nome": "Daniela Costa", "idade": 21},
     5: {"nome": "Eduardo Souza", "idade": 23},
     6: {"nome": "Fernanda Lima", "idade": 20},
     7: {"nome": "Gabriel Alves", "idade": 18},
     8: {"nome": "Helena Pereira", "idade": 22},
     9: {"nome": "Igor Rodrigues", "idade": 21},
    10: {"nome": "Juliana Ferreira", "idade": 19},
    11: {"nome": "Kevin Martins", "idade": 24},
    12: {"nome": "Larissa Gomes", "idade": 20},
    13: {"nome": "Marcelo Ribeiro", "idade": 23},
    14: {"nome": "Natália Cardoso", "idade": 21},
    15: {"nome": "Otávio Barbosa", "idade": 22},
    16: {"nome": "Paula Araújo", "idade": 19},
    17: {"nome": "Rafael Dias", "idade": 20},
    18: {"nome": "Sabrina Castro", "idade": 18},
    19: {"nome": "Thiago Moreira", "idade": 23},
    20: {"nome": "Vanessa Rocha", "idade": 21},
    21: {"nome": "Wagner Cunha", "idade": 22},
    22: {"nome": "Yasmin Mendes", "idade": 20},
    23: {"nome": "André Vieira", "idade": 24},
    24: {"nome": "Beatriz Soares", "idade": 19},
    25: {"nome": "Caio Monteiro", "idade": 21},
    26: {"nome": "Débora Freitas", "idade": 23},
    27: {"nome": "Enzo Carvalho", "idade": 18},
    28: {"nome": "Flávia Batista", "idade": 22},
    29: {"nome": "Gustavo Nunes", "idade": 20},
    30: {"nome": "Isabela Campos", "idade": 21},
    31: {"nome": "João Ramos", "idade": 19},
    32: {"nome": "Kamila Correia", "idade": 23},
    33: {"nome": "Leonardo Pinto", "idade": 22},
    34: {"nome": "Mariana Teixeira", "idade": 20},
    35: {"nome": "Nicolas Azevedo", "idade": 24},
    36: {"nome": "Olivia Borges", "idade": 18},
    37: {"nome": "Pedro Melo", "idade": 21},
    38: {"nome": "Rafaela Lopes", "idade": 19},
    39: {"nome": "Samuel Rezende", "idade": 23},
    40: {"nome": "Tatiana Macedo", "idade": 22},
    41: {"nome": "Ulisses Farias", "idade": 20},
    42: {"nome": "Vitória Moura", "idade": 21},
    43: {"nome": "William Gonçalves", "idade": 19},
    44: {"nome": "Xuxa Tavares", "idade": 24},
    45: {"nome": "Yuri Nascimento", "idade": 23},
    46: {"nome": "Zélia Duarte", "idade": 20},
    47: {"nome": "Arthur Fonseca", "idade": 18},
    48: {"nome": "Bianca Aragão", "idade": 22},
    49: {"nome": "Cauã Miranda", "idade": 21},
    50: {"nome": "Diana Siqueira", "idade": 19}
}

grupo_azul = {}
grupo_amarelo = {}

#Função para dividir o time
def dividir_time(lista_alunos):
    for matricula, dados in alunos.items():
        if matricula % 2 == 0:
            grupo_azul[matricula] = dados
        
        else:
            grupo_amarelo[matricula] = dados



#Função para saber e exibir o time do aluno
def time(matricula):

    if matricula in grupo_amarelo:
        #Usando a função .T para inverter a ordem das linhas e colunas. Método transpose
        df = pd.DataFrame(grupo_amarelo).T
        nome_time = "amarelo"
    
    else:
        df = pd.DataFrame(grupo_azul).T
        nome_time = "azul"
    
    mensagem1 = print(f'\nOlá {alunos[matricula]["nome"]} você está no time {nome_time}!')
    mensagem2 = print(f'Veja todos integrantes do time:\n{df}')
    #Não é necessário o return!
    return mensagem1, mensagem2


matricula = int(input("Olá aluno. Para saber o seu time, digite o número da sua matrícula: "))

dividir_time(alunos)
time(matricula)
