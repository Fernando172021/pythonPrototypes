L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L)

p = int(input('\nDigite um número para pesquisa: '))

for number in L:
    if number == p:
        print('\nDigite E para ver o resultado...')
        print('Digite S para sair...')
        operation = input('Digite a letra da operação: ')

        if operation == 'E':
            print(f'\n{p} foi encontrado na posição {number - 1}')
            break

        elif operation == 'S':
            print('Até a proxima...')
            break

        elif operation != 'E' and operation != 'S':
            print('\nOperação invalida. Reinicie o programa.')
            break
else:
    print('\nDigite um número que esteja na lista acima.')
