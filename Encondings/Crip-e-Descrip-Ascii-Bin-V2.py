import time

crip_ascii = []
crip_bin = []
dec = []
descrip = []

def funcions(w):
    for x in w:
        cod = ord(x)
        crip_ascii.append(cod)
        b = bin(int(cod))
        crip_bin.append(b)

    a = ''
    for y in crip_bin:
        d = int(y, 2)
        dec.append(d)
        a = ''.join(chr(i) for i in dec)
    descrip.append(a)

def sub_menu():
    while True:
        print('-'*100)
        op = int(input('Escolha o que deseja visualizar:\n1 - Criptografia ASCII\n2 - Criptografia Binária\n'
                        '3 - Mensagem Descriptografada\n4 - Conteúdo Descriptografado, de forma original\n5 - Voltar\n'))
        print('-'*100)
        if op == 1:
            print(f'EM ASCII:\n{crip_ascii}')
        elif op == 2:
            print(f'EM BINÁRIO\n{crip_bin}')
        elif op == 3:
            print(f'DESCRIPTOGRAFADO\n{descrip}')
        elif op == 4:
            print('MANTENDO ORIGINALIDADE DE ESCRITA')
            for i in descrip:
                print(i)
        elif op == 5:
            crip_ascii.clear()
            crip_bin.clear()
            dec.clear()
            descrip.clear()
            break
        else:
            print('Opção inesxitente. Tente novamente!')


def menu():
    while True:
        print('-'*100)
        op = int(input('1 - Criptografia de conteúdo de arquivo\n2 - Criptografia de String imediata\n3 - Encerrar\n'))
        if op == 1:
            name = input('Digite o nome do arquivo de texto para criptografia: ')
            with open(name, 'r+', encoding='utf-8') as arquivo:
                w = arquivo.read()
                funcions(w)
                sub_menu()
        elif op == 2:
            w = input('Insira a String desejada> ')
            funcions(w)
            sub_menu()
        elif op == 3:
            print('Encerrando...')
            #time.sleep(0.5)
            break
        else:
            print('Opção inexistente!')

menu()