

from github import Github
import json
import requests

print('1. Bibliotecas Importadas')

# tokens
TOKEN_API_FUTEBOL = 'test_c961e301def7b699c92963a17ac1db'
TOKEN_GITHUB = ''

print('2. Tokens carregados')


def tabela_serie_a(campeonato_id, TOKEN_API_FUTEBOL):   
    
    url = f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/tabela'
    headers = {'Authorization': f'Bearer {TOKEN_API_FUTEBOL}'}
    requisicao = requests.get(url, headers=headers)

    requisicao = json.loads(requisicao.text)

    tabela_campeonato = []

    for time in requisicao:
        dados_time = {
            'time': time['time']['nome_popular'],
            'posicao': time['posicao'],
            'pontos': time['pontos'],
            'escudo': time['time']['escudo'],
        }

        tabela_campeonato.append(dados_time)

    return tabela_campeonato


tabela = tabela_serie_a(10, TOKEN_API_FUTEBOL)

print('3. Dados coletados e tratados')

# dados no formato de lista de dicionários
tabela_json = json.dumps(tabela) # converte em json
# tabela_json

print('4. Dados convertidos para json')


# ATUALIZANDO ARQUIVO JSON NO GITHUB

g = Github(TOKEN_GITHUB) 

# repositorio
repo = g.get_repo("lucasthaynan/construindoAPI")

# local do arquivo no repositorio
contents = repo.get_contents("/api_teste.json")

# atualizando arquivo 
repo.update_file(contents.path, 'Dados atualizados', tabela_json, contents.sha, branch="main")
print('5. Arquivo atualizado no GitHub')

print('--- FIM ---')