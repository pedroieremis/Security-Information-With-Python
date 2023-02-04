import os

print('_'*70)
destino = input('Digite o endereço de destino para testar o ping: ')
print('_'*70)

os.system(f'ping -n 8 {destino}')
print('_'*70)
