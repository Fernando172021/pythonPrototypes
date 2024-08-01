# Pesquisa Sequencial

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L)
p = int(input('\nDigite o valor da procura: '))

x = 0
achou = False

while True:

    if L[x] == p:
        achou = True
    
    x += 1

    if achou == True:
        print('\nPara ver o resultado digite E...')
        operacao = input('\nDigite a letra da operação: ')

        if operacao == 'E':
            print(f'\n{p} achado na posição {x - 1}.')
            break

        else:
            print('Operação Invalida. Digite E para ver o resultado.')
            break

    elif achou == False and x == len(L):
        print('\nDigite um numero que esteja na lista acima') 
        break
