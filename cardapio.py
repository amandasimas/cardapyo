import random
import alimento


def gerar_cardapio():

    p = random.choice(alimento.proteinas)
    c = random.choice(alimento.carboidratos)
    o = random.choice(alimento.oleaginosas)
    m = random.choice(alimento.molho)
    l = random.sample(alimento.legumes, 3)
    f = random.sample(alimento.frutas, 1)
    s = l + f 

    up_line()
    print('Proteína:', p)
    print('Carboidrato:', c)
    print('Oleaginosa:', o)
    print('Molho:', m)
    print('Salada:', s)
    

def up_line():
    print ("\n")


def receita_salgada():
    up_line() 
    print('em construção 2')
    up_line()
    prox_escolha()
    escolhas()
    
def receita_doce():
    up_line()
    print('em construção 3')
    up_line()
    prox_escolha()
    escolhas()
    
def escolhas():
    desejo = int(input())

    if desejo == 0:
        exit()
    elif desejo == 1:
        gerar_cardapio() 
        up_line()
        prox_escolha()
    elif desejo == 2:
        receita_salgada()
    elif desejo == 3:
        receita_doce()
    else:
        print('O número precisa estar entre 0 e 4')
        exit()




def inicio():
    print('Olá, tudo bem?')
    print('O que deseja fazer?')
    print('1 - Gerar novo cardápio')
    print('2 - Sugerir receita salgada')
    print('3 - Sugerir receita doce')
    print('0 - Sair')
    print('> ', end='')
    escolhas()
    
def prox_escolha():
    print('Agora escolha uma opção: ')
    print('1 - Gerar novo cardápio')
    print('2 - Sugerir receita salgada')
    print('3 - Sugerir receita doce')
    print('0 - Sair')
    print('> ', end='')
    escolhas()

inicio()

