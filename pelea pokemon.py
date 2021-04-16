import random


def pelea_pokemon():
    continuar = 's'
    vida_pikachu = 100
    vida_skirtle = 100
    while continuar == 's' or continuar == 'S':

        if vida_pikachu >= 1 and vida_skirtle >= 1:
            vida_skirtle = ataque_pikachu(vida_skirtle)

        elif vida_pikachu <= 0:
            print('felicidades!!!')
            print('has ganado')
            print('atrapaste un pichachu')
            vida_pikachu = 100
            vida_skirtle = 100
            continuar = input('deseas continuar?:')

        if vida_skirtle >= 1 and vida_pikachu >= 1:
            vida_pikachu = ataque_skirtle(vida_pikachu)

        elif vida_skirtle <= 0:
            print('as perdido :(')
            print(f'el pikachu salvage se escapa con {vida_pikachu} puntos de vida')
            vida_pikachu = 100
            vida_skirtle = 100
            continuar = input('deseas continuar?:')


def ataque_skirtle(vida):
    print('elige un ataque')
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
    print('\n')
    return vida


def ataque_pikachu(vida):
    atac = random.randint(1, 3)
    if atac == 1:
        print('pikachu eligio inpactrueno!!')
        print('ataque critico!! -20 de vida ')
        vida -= 20
        print(f'solo te qudan {vida} puntos de vida')
    elif atac == 2:
        print('pikachu eligio coletazo!!')
        print('-10 de vida')
        vida -= 10
        print(f'solo te qudan {vida} puntos de vida')
    else:
        print('pikachu intento hecharte agua pero fallo')
    print('\n')
    return vida


# espacio para funciones principales
# funcion principal
pelea_pokemon()
