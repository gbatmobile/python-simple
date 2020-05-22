import requests

all = requests.get('https://api.cartolafc.globo.com/atletas/mercado', verify=False).json()

atletas = all['atletas']
clubes = all['clubes']
posicoes = all['posicoes']

# Listar todos os jogadores, posicoes e clubes!
for atleta in atletas:
    apelido = atleta['apelido']
    posicao = posicoes[str(atleta['posicao_id'])]['nome']
    clube  = clubes[str(atleta['clube_id'])]['nome']
    print (apelido, ' -> ', posicao, ' -> ', clube)

# Qual o jogador fez mais pontos - quantos ?
atletaMaisPontos = -1
nomeAtletaMaisPontos = ''
for atleta in atletas:
    pontos = atleta['media_num'] * atleta['jogos_num']
    if pontos > atletaMaisPontos:
        atletaMaisPontos = pontos
        nomeAtletaMaisPontos = atleta['apelido']

print('Maior pontuador', nomeAtletaMaisPontos, atletaMaisPontos, sep=' -> ', end=' pontos\n')

# Qual o clube fez mais pontos - quantos ?
clubesPontos = {}
for atleta in atletas:
    pontos = atleta['media_num'] * atleta['jogos_num']
    clubeAtleta = atleta['clube_id']
    clubesPontos[clubeAtleta] = clubesPontos.get(clubeAtleta, 0) + pontos

clubeMaisPontos = -1
idClubeMaisPontos = 0
for idClube in clubesPontos:
    if clubesPontos[idClube] > clubeMaisPontos:
        clubeMaisPontos = clubesPontos[idClube]
        idClubeMaisPontos = idClube

print (f'Clube com mais pontos -> {clubes[str(idClubeMaisPontos)]["nome"]} -> {clubeMaisPontos} pontos ')




