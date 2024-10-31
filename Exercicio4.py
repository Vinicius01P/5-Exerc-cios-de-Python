num_input = int(input('Insira o número: '))
divisores = 0
for c in range(1, num_input + 1):
  if num_input % c == 0:
    divisores += 1
if divisores > 2:
  print('Não é primo')
else:
  print('É primo')