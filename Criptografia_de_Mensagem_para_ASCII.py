name = input('Digite o nome para o arquivo: ')
name += '.txt'
msg = input('Digite a mensagem para codificação: ')
crip_ascii = []
for x in msg:
    cod = ord(x)
    crip_ascii.append(cod)
with open(name, 'w+') as arq:
    for x in str(crip_ascii):
        w = arq.write(x)
print('_'*50)
print('Processo Concluído!')