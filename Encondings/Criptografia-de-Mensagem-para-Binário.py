name = input('Digite o nome para o arquivo: ')
name += '.txt'
msg = input('Digite a mensagem para codificação: ')
crip_bin = []
for x in msg:
    cod = ord(x)
    b = bin(int(cod))
    crip_bin.append(b)
crip_bin = str(crip_bin)
with open(name, 'w+') as arq:
    wr = arq.write(crip_bin)
print('_'*50)
print('Processo Concluído!')
