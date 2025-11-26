import requests

cep = int(input("Informe seu CEP: "))

salvador = 41630240
Roraima = 69373000

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
regioes = ['Norte', 'Nordeste']

if resposta.status_code == 200:
    dados_cep = resposta.json()
    cidade = dados_cep["localidade"]
    regiao = dados_cep['regiao']

    if regiao in regioes:
        print(f'Parabéns. Você é da cidade de {cidade} da região {regiao} e ganhou frete grátis!')
    else:
        print(f'Que pena, você é da cidade de {cidade}  da região {regiao} e não tem direto a frete grátis!')
else:
    print(f"Erro ao consultar o CEP{cep}. Status: {resposta.status_code} ")