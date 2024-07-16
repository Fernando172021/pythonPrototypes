'''.extend metodo utilizado para inserir elementos de uma lista em outra lista!'''

N1 = []
N2 = []
L = []

while True:
    n1 = int(input('Digite um número (0 para proceguir): '))
    if n1 == 0:
        break
    n2 = int(input('Digite outro número (0 para proceguir): '))
    if n2 == 0:
        break
    N1.append(n1)
    N2.append(n2)

L.extend(N1)
L.extend(N2)
print(L)
