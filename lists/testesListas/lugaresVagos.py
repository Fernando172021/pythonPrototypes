"""
 Um programa que controla a utilização das salas de um cinema.
"""
# Indice 0 + 1 = sala 1 / indice 1 + 2 = sala 2...
lugares_vazios = [10, 2, 1, 3, 0]

while True:
    print('\nUtilização das salas')

    for x, l in enumerate(lugares_vazios):
        print(f'\nSala {x + 1} - {l} lugar(es) vazio(s).')

    print('\nSalas: 1, 2, 3, 4 e 5')
    
    sala = int(input('\nDeseja assistir em qual sala?(Digite 0 para sair) '))

    if sala == 0:
        print('\nFim')
        break

    elif sala > len(lugares_vazios) or sala < 1:
        print('\nSala Invalida.')

    elif lugares_vazios[sala - 1] == 0:
        print('\nDesculpe, sala lotada!')

    else: 
        lugares = int(input(f'\nQuantos lugares você deseja? ({lugares_vazios[sala - 1]} vagos) '))

        if lugares > lugares_vazios[sala - 1]:
            print('\nEsse número de lugares não esta disponivel nesta sala.')
        
        elif lugares <= 0:
            print('\nNúmero invalido')

        elif lugares <= lugares_vazios[sala - 1]:
            print(f'\n{lugares} Lugar(es) vendido(s)!')
            print('-' * 56)
    