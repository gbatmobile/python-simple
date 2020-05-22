import requests

def apelidoEClube(atleta):
    clube_id = str(atleta['clube_id'])
    nomeDoClube = clubes[clube_id]['nome']
    return atleta['apelido'] + ' (' + nomeDoClube +') '


all = requests.get('https://api.cartolafc.globo.com/atletas/mercado', verify=False).json()

atletas = all['atletas']
clubes = all['clubes']
posicoes = all['posicoes']

maiorPontuacao = 0

for atleta in atletas:
    apelido = atleta['apelido']
    pontos = atleta['jogos_num'] * atleta['media_num']

    if pontos > maiorPontuacao:
        maiorPontuacao = pontos
        maiorPontuador = atleta

    posicao_id = str(atleta['posicao_id'])
    nomeDaPosicao = posicoes[posicao_id]['nome']

    clube_id = str(atleta['clube_id'])
    nomeDoClube = clubes[clube_id]['nome']

    print (apelidoEClube(atleta), pontos, nomeDaPosicao, sep=' - ')

print ("Maior pontuador: ", apelidoEClube(maiorPontuador), 'com: ', maiorPontuacao, "pontos!")