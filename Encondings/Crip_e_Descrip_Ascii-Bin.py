
name = input('Digite o nome do arquivo de texto para criptografia: ')
with open(name, 'r+', encoding='utf-8') as arquivo:
    w = arquivo.read()

msg = w
crip_bin = []
crip_ascii = []
dec = []
descrip = ''

for x in msg:
    cod = ord(x)
    crip_ascii.append(cod)
    b = bin(int(cod))
    crip_bin.append(b)

cont = 0
for y in crip_bin:
    d = int(y, 2)
    dec.append(d)
    descrip = ''.join(chr(l) for l in dec)


while True:
    print('-'*100)
    op = int(input('Escolha o que deseja visualizar:\n1 - Criptografia ASCII\n2 - Criptografia Binária\n'
                    '3 - Mensagem Descriptografada\n4 - Encerrar '))
    if op == 1:
        print('-'*100)
        print(crip_ascii)
    elif op == 2:
        print('-'*100)
        print(crip_bin)
    elif op == 3:
        print('-'*100)
        print(descrip)
    elif op == 4:
        print('-'*100)
        print('Encerrado!')
        break
    else:
        print('-'*100)
        print('Opção inesxitente. Tente novamente!')