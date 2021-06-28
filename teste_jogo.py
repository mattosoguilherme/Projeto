from random import randint #função da biblioteca radom que escolhe um número aleatório dentro de um parametro informado pelo programador\usuário
from time import sleep #função da biblioteca time que faz uma pausa entre uma excecuçã de código e outro. O tempo de pausa é determinado pelo programador
from operator import itemgetter #função da biblioteca operator que colocar items em ordem crescente
from PySimpleGUI import PySimpleGUI as sg #biblioteca com funções de interface gráfica

#introdução do jogo
print('''                           []=JOGO DE DADOS=[]

Galvão Boeno:
    - Meus amiiiigos da Blue, hoje vamos ver no campo a raça, determinação e a sagacidaaade desses 
jogaores, maaas antes as passo a passo:

1º Digite o quantidade de partidas.

2º Digite seu nome e dos adverários, 
lebrando que esse jogo foi feito para jogar em grupo, com 4 jogadores.

3º Se dirviiiiiita jogaaando! ''')
sleep(2)
print('''\nRonaldo:
    - Galvão é bom lebrar que o computador vai jogar o dado pelo jogadores, eles só vão ter esperar pelo resultado na tela.''')

sleep(2)
print()
#variaveis com input para coletar informações do usuário final.
quantidade_rodadas = int(input('Quantas rodadas você quer jogar?\n'))
player1 = input('Qual o nome do 1º jogador?\n').capitalize()
player2 = input('Qual o nome do 2º jogador?\n').capitalize()
player3 = input('Qual o nome do 3º jogador?\n').capitalize()
player4 =  input('Qual o nome do 4º jogador?\n').capitalize()
print()
vitoria_jgd1=vitoria_jgd2=vitoria_jgd3=vitoria_jgd4=0
#laço de repetição para simular "tela de carregamento".
for o in range(5):
    print("............"*2, end='')
    sleep(1)
print('100%')

print()
#laço de repetição condicionado com parâmetros inseridos pelo usuário.
for r in range(quantidade_rodadas):
    dados = {player1:randint(1,6),player2:randint(1,6),player3:randint(1,6),player4:randint(1,6)} #dicionário criado para alocar valores aleatórios gerados.
    v = sorted(dados.items(), key=itemgetter(1), reverse=True) # a variavel 'v' está recebendo o dicionário já formatado em ordem decrescente
    print("-="*25)
    print(f"{r+1}º RODADA:\n")
    for k, x in v: #neste laço existem duas variaveis, 'k' que representa as chaves do dicionário e 'x' os valores.
        print(f'{k} tirou {x} no dado') #como é um laço condicionado ele vai varrer a o dicionario, mostrar cada chave e valor e finalizar
        sleep(1)
    print()
#condições para verficar quem venceu cada roda de cada volta no laço.
    if dados[player1]>= dados[player2] and dados[player1]>= dados[player3] and dados[player1] >= dados[player4]:
        print(f'\n{player1} venceu está rodada!\n')
        vitoria_jgd1+=1 # a cada volta vai irá contabilizar quantas vitorias o jogador teve
        
    if dados[player2] >= dados[player1] and dados[player2] >= dados[player3] and dados[player2] >= dados[player4]:
        print(f'\n{player2} venceu está rodada!\n')
        vitoria_jgd2+=1

    if dados[player3] >= dados[player2] and dados[player3] >= dados[player1] and dados[player3] >= dados[player4]:
        print(f'\n {player3} venceu está rodada!\n')
        vitoria_jgd3+=1

    if dados[player4] >= dados[player2] and dados[player4] >= dados[player3] and dados[player4] >= dados[player1]:
        vitoria_jgd4+=1
        print(f'\n{player4} venceu está rodada!\n')
    sleep(2)

sleep(2)

print(f''' =========PLACAR==========
{player1} ganhou um total de {vitoria_jgd1} rodadas.
{player2} ganhou um total de {vitoria_jgd2} rodadas.
{player3} ganhou um total de {vitoria_jgd3} rodadas.
{player4} ganhou um total de {vitoria_jgd4} rodadas.''')
#condicinais criadas para verificar e mostrar uma tela dizendo quais jogadores venceram mais vezes.
if vitoria_jgd1 >= vitoria_jgd2 and vitoria_jgd1 >= vitoria_jgd3 and vitoria_jgd1 >= vitoria_jgd4:
    sg.theme('LightGreen5') 
    layout = [
        [sg.Text(f'Parabens! {player1} você é o grande vencedor(a)!')],
        [sg.Button('Finalizar')]]
    janela = sg.Window("Final do jogo", layout)
    for c in range(1):
        eventos = janela.read()
    
if vitoria_jgd2 >= vitoria_jgd1 and vitoria_jgd2 >= vitoria_jgd3 and vitoria_jgd2 >= vitoria_jgd4:
    sg.theme('LightGreen5')
    layout = [
        [sg.Text(f'Parabens! {player2} você é o grande vencedor(a)!')],
        [sg.Button('Finalizar')]]
    janela = sg.Window("Final do jogo", layout)
    for c in range(1):
        eventos = janela.read()

if vitoria_jgd3 >= vitoria_jgd2 and vitoria_jgd3 >= vitoria_jgd1 and vitoria_jgd3 >= vitoria_jgd4:
    sg.theme('LightGreen5')
    layout = [
        [sg.Text(f'Parabens! {player3} você é o grande vencedor(a)!')],
        [sg.Button('Finalizar')]]
    janela = sg.Window("Final do jogo", layout)
    for c in range(1):
        eventos = janela.read()

if vitoria_jgd4 >= vitoria_jgd2 and vitoria_jgd4 >= vitoria_jgd3 and vitoria_jgd4 >= vitoria_jgd1:
    sg.theme('LightGreen5')
    layout = [
        [sg.Text(f'Parabens! {player4} você é o grande vencedor(a)!')],
        [sg.Button('Finalizar')]]
    janela = sg.Window("Final do jogo", layout)
    for c in range(1):
        eventos = janela.read()