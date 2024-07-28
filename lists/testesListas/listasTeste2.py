# Exclusão de número iguais em ambas as listas!
# del  metodo utilizado para excluir itens de uma lista

N1 = [1, 3, 5, 4, 10, 7, 13]
N2 = [2, 3, 8, 4, 10, 12, 14]
L = []

x = 0
l = 0

print('Listas abaixo')
print(N1)
print(N2)
print('Segue Processamento...')

while l < len(N1) and x < len(N1): 
    sum = len(N1)
    matrix = sum - 1

    if x < len(N1) and l < len(N2):

        if N1[x] == N2[l]:
            del N1[x]
            del N2[l]

        l += 1
        
    if x < len(N1) and l < len(N2):

        if N1[x] == N2[l]:
            del N1[x]
            del N2[l]

        l += 1

    print('-' * 36)
    print(N1)
    print(N2)
    print('-' * 36)

    if x == matrix and l == len(N2):
        choise = int(input('Press ZERO (0) to continue or ONE (1) to stop... '))

        if choise == 0:
            x = 0
            l = 0

        elif choise == 1:
            print('Congratulations')
            L.extend(N1)
            L.extend(N2)

            print('-' * 36)
            print(L)
            print('-' * 36)
            
        else:
            print('Error! Try again!')
            break

    if l == len(N2):
        x += 1
        l = 0
