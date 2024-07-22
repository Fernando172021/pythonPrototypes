notas = [5, 2, 3, 4, 2, 9, 10]
soma = 0
x = 0

while x < len(notas):
    soma += notas[x]
    x += 1
print(f'Média {soma / x:5.2f}')

# len() metodo usado para identificar quantidade de elementos em uma lista!