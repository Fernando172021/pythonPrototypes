# Pesquisa com FOR 2

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L)

p = int(input('\nDigite um número para a pesquisa: '))

for number in L:
    if number == p:
        print(f'\n{p} foi encontrado na posição {number - 1}')
        break
else:
    print('Digite um número que esteja na lista acima.')
