import requests

all = requests.get('https://api.cartolafc.globo.com/atletas/mercado', verify=False).json()

print (type(all))

for k in all:
    print (type(k), k, type(all[k]))


atletas = all['atletas']

#print (all['clubes'])

for atleta in atletas:
    print(atleta['apelido'], '-', all['clubes'][str(atleta['clube_id'])]['nome'])










'''

atletas = all['atletas']   # Lista com todos os atletas
posicoes = all['posicoes']

#clubes = all['clubes']

#print (posicoes)


for atleta in atletas:
    pos_id = str(atleta['posicao_id'])
    print (atleta['apelido'], '->',  posicoes[pos_id]['nome'])


#    print (f"{atleta['apelido']}")
#    print (f"{clubes[str(atleta['clube_id'])]['nome']})")
#    print (f" -> {posicoes[str(atleta['posicao_id'])]['nome']}")
'''