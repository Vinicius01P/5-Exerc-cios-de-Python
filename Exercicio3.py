num_input = int(input('Insira o número: '))
menor = num_input
for c in range(0, 2):
  num_input = int(input('Insira o número: '))
  if menor > num_input:
    menor = num_input
print(f'O menor número inserido foi {menor}')