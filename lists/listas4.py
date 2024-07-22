# .append() metodo utilizado para inserir elementos em uma lista!

L = []

while True:
    n1 = int(input('Digite um número (0 para sair): '))
    if n1 == 0:
        break
    L.append(n1)

x = 0

while x < len(L):
    print(L[x])
    x += 1