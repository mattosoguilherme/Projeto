from random import randint #função da biblioteca radom que escolhe um número aleatório dentro de um parametro informado pelo programador\usuário
from time import sleep #função da biblioteca time que faz uma pausa entre uma excecuçã de código e outro. O tempo de pausa é determinado pelo programador
from operator import itemgetter

print('''                           []=DICE GAME=[]
   
    COMO FUNCIONA? 
        Bom, DICE GAME ou JOGO DE DADOS é um jogo bem simples foi feito para jogar 
em gupo de 4 jogadores. Ganha quem tirar o maior número na rodada, o próprio usuário 
determina a quantidade de rodadas, no fim programa irá mostrar quem venceu mais partidas!        
''')
jogadores=dict()
quantidade_rodadas = int(input('Quantas rodadas você quer jogar?\n'))
jogadores['player1'] = input('Qual o nome do 1º jogador?\n').capitalize()
jogadores['player2'] = input('Qual o nome do 2º jogador?\n').capitalize()
jogadores['player3'] = input('Qual o nome do 3º jogador?\n').capitalize()
jogadores['player4'] = input('Qual o nome do 4º jogador?\n').capitalize()

vitoria_jgd1=vitoria_jgd2=vitoria_jgd3=vitoria_jgd4=0
empates=0
# listaRestultados = list()
#  listaRestultados.append(v)

for r in range(quantidade_rodadas):
    dados = dict()
    dados = {'dado1':randint(1,6),'dado2':randint(1,6),'dado3':randint(1,6),'dado4':randint(1,6)}
    v = sorted(dados.items(), key=itemgetter(1), reverse=True)
    

    if dados["dado1"] == dados["dado2"]:
        print(f"\nEmpate entre {jogadores['player1']} e {jogadores['player2']}.\n")
        empates=+1
    if dados["dado1"] == dados["dado3"]:
        print(f"\nEmpate entre {jogadores['player1']} e {jogadores['player3']}.\n")
        empates=+1
    if dados["dado1"] == dados["dado4"]:
        print(f"\nEmpate entre {jogadores['player1']} e {jogadores['player4']}.\n")
        empates=+1
    if dados["dado2"] == dados["dado3"]:
        print(f"\nEmpate entre {jogadores['player2']} e {jogadores['player3']}.\n")
        empates=+1
    if dados["dado3"] == dados["dado4"]:
        print(f"\nEmpate entre {jogadores['player3']} e {jogadores['player4']}.\n")
        empates=+1
    if dados["dado4"] == dados["dado2"]:
        print(f"\nEmpate entre {jogadores['player4']} e {jogadores['player2']}.\n")
        empates=+1

    if dados["dado1"] > dados["dado2"] and dado1 > dados["dado3"] and dado1 > dados["dado4"]:
        print(f"\n{jogadores['player1']} venceu está rodada\n")
        vitoria_jgd1+=1

    if dados["dado2"] > dados["dado1"] and dados["dado2"] > dados["dado3"] and dados["dado2"] > dados["dado4"]:
        print(f"\n{jogadores['player2']} venceu está rodada\n") 
        vitoria_jgd2+=1

    if dados["dado3"] > dados["dado1"] and dados["dado3"] > dados["dado2"] and dados["dado3"] > dados["dado4"]:
        print(f"\n{jogadores['player3']} venceu está rodada\n")
        vitoria_jgd3+=1

    if dados["dado4"] > dados["dado1"] and dados["dado4"] > dados["dado2"] and dados["dado4"] > dados["dado3"]:
        print(f"\n{jogadores['player4']} venceu está rodada\n")
        vitoria_jgd4+=1


print(f''' =resultado=
{jogadores['player1']} venceu {vitoria_jgd1}
{jogadores["player2"]} venceu {vitoria_jgd2}
{jogadores["player3"]} venceu {vitoria_jgd3}
{jogadores["player4"]} venceu {vitoria_jgd4}
O jogo teve {empates} empates
''')