# Pesquisa Sequencial

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = int(input('\nDigite o valor da procura: '))

x = 0
achou = False

while x < len(L):

    if L[x] == p:
        achou = True
    
    x += 1

    if achou == True:

        while True:
            print('\nPara ver o resultado digite E...')
            print('Para recomeçar a pesquisa digite D...')
            operacao = input('Operação E ou D: ')

            if operacao == 'E':

                if achou == True:
                    print(f'\n{p} achado na posição {x}.')

                else:
                    print(f'\n{p} não encontrado.')
                    print(x)

            elif operacao == 'D':
                p = input('\nDigite o valor da procura: ')
                x = 0
                achou = False
                break

            else:
                print('\nOperacao invalida! Digite E ou D...')
