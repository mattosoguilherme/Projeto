#biblioteca\library

from time import sleep #função que dá tempo de espera para excecução entre codgos \ function that gives wait time for execution between codes
from os import system #função que limpa tudo que está acima no terminal \ function that clears everything above the terminal

#listas para guardar votos inseridos pelo usuário \ lists for saving votes entered by the user
bill=[]
mark=[]
elon=[]
null=[]
blank=[]

#fuções \ functions

def color(color, phrase): # Esta serve para colorir as str's,basta inserir 2 parâmetros, o nome da cor: verde, amarelo e vermelho, e a frase. \ This is used to color the str's, just insert 2 parameters, the name of the color: green, yellow and red, and the phrase.
    from sty import fg, bg, ef, rs 
    if color == "green":
        print(fg.green + phrase +fg.rs)
    if color == "yellow":
        print(fg.li_yellow + phrase + fg.rs)
    if color == "red":
        print(fg.red + phrase + fg.rs) # Resultado, retornará um print com a cor inserida \ Result, will return a print with the inserted color


def authorized_vote(year): # Esta tem o propósito de verificar se a idade do usário é valida para o voto \ This is for the purpose of verifying if the user's age is valid for the vote

    age = 2021 - year
    if age <16:
        return "vote denied" 
        
    if 18 <= age <=70:
        return "mandatory vote"
    else:
        return "optional vote"

def votation(verification,vote= -1): # Nesta aqui verifica o número do voto e indentifica quem o usuário escolheu para votar. Contabiliza e mostra quantos votos tiveram. \ This one checks the vote number and identifies who the user has chosen to vote on. Counts and shows how many votes they had.
    
    print(f'\n {name} you are {2021 - age} years olds')
# De acordo com a validação da função anterior, condicionais abaixo irão fazer determinada ação. \  According to the validation of the previous function, conditionals below will do certain action.
    if verification == "vote denied": 
        
        color("red","you can't vote!")

    if verification == "optional vote":    

        question = str(input("\nYour vote is optional. Want to vote? [Y/N] ")).upper().strip()

        while question not in "YN":

                color("red","opção inválida!\u26A0\uFE0F")
                question = str(input("\nYour vote is optional. Want to vote? [Y/N] ")).upper().strip()

                if question == "N":
                    print("\nThank you have a good day!!\U0001f600")

        if question == "Y":
            vote = int(input("\nEnter your vote: "))
                
    if verification == "mandatory vote":
        print("\nYour vote is mandatory")
        vote = int(input("\nEnter your vote: "))
# condicionais para indetificar com o número do voto, qual o canditado. \ conditionals to identify the candidate with the vote number.

    if vote == 1 :
        bill.append(1)
        color("green","\nYou voted for Bill Gates for internet president!")
    elif vote == 2 :
        mark.append(1)
        color("green","\nYou voted for Mark Zuckerberg for internet president!")
    elif vote == 3 :
        elon.append(1)
        color("green","\nYou voted for Elon Musk for internet president!")
    elif vote == 4 :
        null.append(1)
        color("yellow","\nNull vote \U0001F610")
    elif vote == 5 :
        blank.append(1)
        print("\nBlank vote")
    elif vote == -1:
        pass
    else:
        color("red","\nInvalid option\u26A0\uFE0F!")
#tabela que mostra números totais de votos, atravéis de um print, com f string e a função sum que somana valores dentro de uma lista. \ table that shows total numbers of votes, through a print, with f string and the sum function that sums values ​​within a list.
    print(f'''                  
                                ________________________________________________
                                |                                              | 
                                | TOTAL VOTES BILL GATES        [ {sum(bill)} ]          |
                                | TOTAL VOTES MARK ZUCKERBERG   [ {sum(mark)} ]          |
                                | TOTAL VOTES ELON MUSK         [ {sum(elon)} ]          |
                                | TOTAL NULL  VOTES             [ {sum(null)} ]          |
                                | TOTAL BLANK VOTES             [ {sum(blank)} ]          |
                                \_______________________________________________/
    
    ''')



system('clear')
# História \ History
print('''                                                   Elections 2022
                   Charles D'amelio:
                            - The internet has been gaining great traction in recent years, because of this we netizens decided to choose
                            a president to steer and command this boat! Now this year's candidates will say some brief words and we will proceed to vote.
''')
sleep(5)

print('''                   Bill Gates:
                            - When we look to the future, we will see that the leaders will be the ones who favor
                            the development of all others. I want to be the leader who favors tomorrow, vote one 
                            for bill gates in the presidency of the internet!!
 ''')

sleep(5)

print('''                   Mark Zuckerberg:
                            - In a constantly changing world, the only guarantee for not failing is not to take risks.
                            Vote two and make sure it's right, Zuckerberg for president of the internet.
''')

sleep(5)

print('''                   Elon Musk:
                            - Some people don't like change, but you need to embrace change if the alternative
                            is disaster. The internet needs new rules, something better. Vote three for the new one, vote
                            three so I can become the best internet president you've ever seen.
''')

sleep(1)

print('''                   Charles D'amelio:
                            - Netizens, vote wisely, voting is the most powerful thing you have in this system, don't waste it!
''')

# Laço infinito
while True:
    system('clear')
    print('''                                         ____________________________
                                        |                            |
                                        |_______URNA_DIGITAL_________|
                                        |                            |
                                        |    [ 1 ] Bill Gates        |       
                                        |    [ 2 ] Mark Zuckerberg   |
                                        |    [ 3 ] Elon Musk         | 
                                        |    [ 4 ] Null Vote         | 
                                        |    [ 5 ] Blank Vote        |
                                        \____________________________/
    ''')


    name = str(input("\nWhat's your name?\n")).title()
    document = str(input("\nEnter your CPF: "))
    age = int(input(" \nWhat is your birth year?\n"))
    authorized_vote(age)
    votation(authorized_vote(age))
# variavel question criada apenas para dar fim ao laço. \ variable question created just to end the loop.
    question = str(input("\nDo you want to vote again? [Y/N] ")).upper().strip()
    if question == "N": 
        print("Thank you have a good day!\U0001f600 \n Wait for the counting of votes.")
        for count in range(5):
            print("<->")
            sleep(1)
        break
#Laço criado caso para previnir erro de digitação do usário. \ Loop created case to prevent user typing error.
    while  question not in "YN":
        print("invalid option!")
        question = str(input("\nDo you want to vote again? [Y/N] ")).upper().strip()
        if question == "N":
            print("Thank you have a good day!\U0001f600 \n Wait for the counting of votes.")
            for count in range(5):
                print("<->")
                sleep(1)
            break

        else:
            continue

#condicionais para mostrar quem venceu a eleição ou se houve mais votos nulos e brancos. \ conditionals to show who won the election or if there were more null and blank votes.
if sum(bill) >= sum(mark) >= sum(elon) >= sum(null) >= sum(blank):
    print(f"\nCharlie D'amelio:\n-Bill Gates won this election with {sum(bill)} votes!")
    sleep(2)
    print(f'''\nBill Gates:
    - Throughout my journey, i realized that to be great, sometimes you have to take huge risks. 
    Let's all grow, thanks for supporting me!''')

if sum(mark) >= sum(bill) >= sum(elon) >= sum(null) >= sum(blank):
    print(f"\nCharlie D'amelio:\n- Mark Zuckerberg won this election with {sum(mark)} votes!")
    sleep(2)
    print(f'''\nMark Zuckerberg:
    - Thank you very much Netizens!''')

if sum(elon) >= sum(bill) >= sum(mark) >= sum(null) >= sum(blank):
    print(f"\nCharlie D'amelio:\n- Elon Musk won this election with {sum(mark)} votes!")
    sleep(2)
    print(f'''\nElon Musk:
    - I will bring innovative and amazing things for you. I'm looking forward to starting this 
    new phase of my life, thank you internet, thank you world!''')

if sum(null) >= sum(blank) >= sum(mark) >= sum(elon) >= sum(bill):
    print(f"\nCharlie D'amelio:\n- Due to the amount of invalid votes, we netizens decided...the three candidates\nmust meet to govern together")

if sum(blank) >= sum(null) >= sum(mark) >= sum(elon) >= sum(bill):
    print(f"\nCharlie D'amelio:\n- Due to the amount of blank votes, we netizens decided...the three candidates\nmust meet to govern together")



            