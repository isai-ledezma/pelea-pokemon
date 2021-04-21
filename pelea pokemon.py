import random
import os

def pelea_pokemon():
    continuar = 's'
    vida_pikachu = 100
    vida_skirtle = 100
    c = 0
    while continuar == 's' or continuar == 'S':

        if c != 0:
            vida_pikachu = 100
            vida_skirtle = 100
            c = 0
          #  barra_de_vida(vida_pikachu, vida_skirtle)
        if vida_pikachu >= 1 and vida_skirtle >= 1:
            vida_skirtle = ataque_pikachu(vida_skirtle)
            print('')
            #if c != 1:
            barra_de_vida(vida_pikachu, vida_skirtle)

            input('enter para continuar')

            os.system("cls")
        '''    else:
                c += 1'''

        if vida_pikachu <= 0:
            os.system('cls')
            vida_pikachu = 0
            print('felicidades!!!')
            print('has ganado')
            print('atrapaste un pichachu')

            c += 1

            continuar = input('deseas continuar?:')

            os.system('cls')

        if vida_skirtle >= 1 and vida_pikachu >= 1:

            vida_pikachu = ataque_skirtle(vida_pikachu)
            print('')


        elif vida_skirtle <= 0:
            vida_skirtle = 0
            os.system('cls')
            barra_de_vida(vida_pikachu, vida_skirtle)
            print('as perdido :(')
            print(f'el pikachu salvage se escapa con {vida_pikachu} puntos de vida')

            c+=1

            continuar = input('deseas continuar?:')


def barra_de_vida(vida_pikachu, vida_skirtle):
    print('')
    vida1 = 0
    vida1p = 0
    vida1 = int(vida_pikachu / 10)
    vida1p= int(10 - vida_pikachu / 10)
    if vida1 + vida1p != 10:
        vida1p = 10 - vida1

    print(f'vida pikachu = [' + '$' * int(vida_pikachu / 10) + '-' * vida1p + f']{vida_pikachu}')
    vida1 = int(vida_skirtle / 10)
    vida1p = int(10 - vida_skirtle / 10)
    if vida1 + vida1p != 10:
        vida1p = 10 - vida1
    print(f'vida skirtle = [' + '#' * int(vida_skirtle / 10) + '-' * vida1p + f']{vida_skirtle}')
    print('')



def ataque_skirtle(vida):
    ataques_posibles = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']
    print('\nelige un ataque')
    print('a: chorro de agua')
    print('b: oleada')
    print('c: beber agua')
    print('d: no hacer nada')
    op = None
    potencia = 69
    while op not in ataques_posibles:
        op = input('?:')

        if op == 'a':
            potencia = random.randint(0, 20)
            vida -= potencia
        elif (op == 'b'):
            potencia = random.randint(0, 10)
            vida -= potencia
        elif (op == 'c'):
            potencia = random.randint(0, 5)
            vida -= potencia
        elif (op == 'd'):
            potencia = 0
            print('no haces nada huevon')
        else:
            print('opcion incorrecta vuelve a elegir')
        if potencia != 69:
            if potencia >= 15:
                print(f'ataque critico le quitaste {potencia} puntos de vida')
            elif potencia == 0 and op !='d':
                print('se te cebo no le quitaste nada')

            elif potencia == 69:
                print('')
            else:
                print(f'le quitaste {potencia} puntos de vida')
    print(f'le quedan {vida} puntos de vida')

    return vida


def ataque_pikachu(vida):
    atac = random.randint(1, 3)
    if atac == 1:
        print('-pikachu eligio inpactrueno!!')
        print('ataque critico!! -20 de vida ')
        vida -= 20
    elif atac == 2:
        print('-pikachu eligio coletazo!!')
        print('-10 de vida')
        vida -= 10

    else:
        print('-pikachu intento hecharte agua pero fallo')

    return vida


# espacio para funciones principales
# funcion principal
pelea_pokemon()


     
