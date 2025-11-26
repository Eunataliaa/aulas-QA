#Criando uma tupla
tupla = ("verde", "vermelho", "azul", "preto", "branco")
print(f'Tupla: {tupla}')
print('\n')

#Alterando a tupla para lista
lista = []
for i in tupla:
    lista.append(i)

lista.append("roxo")
lista.append("marrom")

print(f'Lista com +2 dados adicionados: {lista}')
print('\n')

#Removendo o primeiro dado da lista
lista.remove(lista[0])
print(f'Lista com o primeiro dado removido: {lista}')
print('\n')

#Removendo o último dado da lista
lista.remove(lista[-1])
print(f'Lista com o último dado removido: {lista}')
print('\n')

#Primeiro dado da lista
print(f'Primeiro dado da lista: {lista[0]}')
print('\n')

#Quantidade de dados na lista
print(f'Quantidade de dados na lista: {len(lista)}')
print('\n')

#Criando um dicionário
dic = {
    "nome": "Caique",
    "Idade": 25,
    "Profissão": "Estagiário"
}

print(f'Nome no dicionário: {dic["nome"]}')