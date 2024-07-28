# Empilhando pratos!

# Adicione e retire pratos por cima da lista.

prato = 5

pilha = list(range(1, prato + 1))

while True:
 print(f'\nExistem {len(pilha)} pratos na pilha.')
 print(f'Pilha atual: {pilha}')
 print('Digite D para empilhar mais pratos...')
 print('Ou digite E para lavar um prato. S para sair.')
 operacao = input(f'Operação (E, D ou S): ')

 if operacao == 'D':
  prato += 1
  pilha.append(prato)

 elif operacao == 'E':
  
  if len(pilha) > 0:
   lavado = pilha.pop(-1)
   print(lavado)

  else:
   print('pilha vazia. Nada para lavar')

 elif operacao == 'S':
  break
 
 else:
  print('Operação invalida! Digite apenas E, D ou S.')
