import requests

dados = [
    {
        "nome": "Layza",
        "CEP": 11635160
    },
    {
        "nome": "Ana julia",
        "CEP": 39404522
    },
    {
        "nome": "tatiane",
        "CEP": 11640224
    }
]

for dado in dados:
    cep = dado["CEP"]
    nome = dado["nome"]
    url_viacep = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url_viacep)
        
    if resposta.status_code == 200:
         
         #Transformar a resposta em JSON
         dados_cep = resposta.json()
         
         # Checa se o ViaCEP retornou um erro (ex: CEP não encontrado)
         if dados_cep.get("erro"):
             print(f"Olá {nome}, não foi possível encontrar o CEP {cep}.")
         else:
             # Pega a cidade (a chave no ViaCEP é "localidade")
             cidade = dados_cep["localidade"]
             uf = dados_cep["uf"]
             print(f'Olá {nome}, sua cidade é {cidade} - {uf}')
        
    else:
        print(f"Erro ao consultar o CEP {cep} para {nome}. Status: {resposta.status_code}")