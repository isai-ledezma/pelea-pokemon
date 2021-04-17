import random

def pelea_pokemon():
    continuar = 's'
    vida_pikachu = 100
    vida_skirtle = 100
    c = 0
    while continuar == 's' or continuar == 'S':

        if c == 0:
            c= c + 1
            barra_de_vida(vida_pikachu, vida_skirtle)
        if vida_pikachu >= 1 and vida_skirtle >= 1:
            vida_skirtle = ataque_pikachu(vida_skirtle)

        elif vida_pikachu <= 0:
            print('felicidades!!!')
            print('has ganado')
            print('atrapaste un pichachu')
            vida_pikachu = 100
            vida_skirtle = 100
            continuar = input('deseas continuar?:')
            c = 0

        if vida_skirtle >= 1 and vida_pikachu >= 1:
            vida_pikachu = ataque_skirtle(vida_pikachu)

            barra_de_vida(vida_pikachu, vida_skirtle)
        elif vida_skirtle <= 0:
            barra_de_vida(vida_pikachu, vida_skirtle)
            print('as perdido :(')
            print(f'el pikachu salvage se escapa con {vida_pikachu} puntos de vida')


            vida_pikachu = 100
            vida_skirtle = 100
            continuar = input('deseas continuar?:')
            c = 0

def barra_de_vida(vida_pikachu, vida_skirtle):
    vida1 = 0
    vida1p = 0
    vida1 = int(vida_pikachu / 10)
    vida1p= int(10 - vida_pikachu / 10)
    if vida1 + vida1p != 10:
        vida1p = 10 - vida1

    print(f'vida pikachu = [' + '$' * int(vida_pikachu / 10) + '-' * vida1p + ']')
    vida1 = int(vida_skirtle / 10)
    vida1p = int(10 - vida_skirtle / 10)
    if vida1 + vida1p != 10:
        vida1p = 10 - vida1
    print(f'vida skirtle = [' + '#' * int(vida_skirtle / 10) + '-' * vida1p + ']')


def ataque_skirtle(vida):
    print('\nelige un ataque')
    print('a: chorro de agua')
    print('b: oleada')
    print('c: beber agua')
    op = None
    while op != 'a' and op != 'b' and op != 'c':
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
        else:
            print('opcion incorrecta vuelve a elegir')

        if potencia >= 15:
            print(f'ataque critico le quitaste {potencia} puntos de vida')
        elif potencia == 0:
            print('se te cebo no le quitaste nada')
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


