import hashlib

lista_palavras_ver = []
lista_parcial_ver = []
lista_parcial = []
lista_verific = []
cont = 'sim'

def verifica(cont):
    while cont.lower() == 'sim':
        strs = input('Digite a string que deseja verificar no histórico de HASHS: ')
        res1 = hashlib.md5(strs.encode('UTF-8')).hexdigest()
        res2 = hashlib.sha1(strs.encode('UTF-8')).hexdigest()
        res3 = hashlib.sha224(strs.encode('UTF-8')).hexdigest()
        res4 = hashlib.sha256(strs.encode('UTF-8')).hexdigest()
        res5 = hashlib.sha384(strs.encode('UTF-8')).hexdigest()
        res6 = hashlib.sha512(strs.encode('UTF-8')).hexdigest()
        lista_verific.append(res1)
        lista_verific.append(res2)
        lista_verific.append(res3)
        lista_verific.append(res4)
        lista_verific.append(res5)
        lista_verific.append(res6)
        with open('Histórico_de_hashs.txt', 'r') as arq1:
            vdd = 'não'
            for i in arq1:
                if i.replace('\n', '') in lista_verific:
                    print(f'\nHASH de "{strs}" contém em histórico!\nResultado encontrado: {i}')
                    vdd = 'sim'
                    lista_palavras_ver.append(f"TINHA: {strs}")
                    break
            if vdd != 'sim':
                op1 = input(f'\nHASH de "{strs}" não contém em histórico\nDeseja adicionar: (sim ou não) ')
                lista_palavras_ver.append(f"NÃO TINHA: {strs}")
                if op1.lower() == 'sim':
                        op2 = int(input('Escolha a opção de HASH deseja adicionar ao arquivo em hexadecimal:\n1 - MD5'
                                        '\n2 - SHA1\n3 - SHA224\n4 - SHA256\n5 - SHA384\n6 - SHA512\n'))
                        if op2 == 1:
                            lista_parcial.append(res1)
                            lista_parcial_ver.append(res1)
                        elif op2 == 2:
                            lista_parcial.append(res2)
                            lista_parcial_ver.append(res2)
                        elif op2 == 3:
                            lista_parcial.append(res3)
                            lista_parcial_ver.append(res3)
                        elif op2 == 4:
                            lista_parcial.append(res4)
                            lista_parcial_ver.append(res4)
                        elif op2 == 5:
                            lista_parcial.append(res5)
                            lista_parcial_ver.append(res5)
                        elif op2 == 6:
                            lista_parcial.append(res6)
                            lista_parcial_ver.append(res6)
                        else:
                            print('Não há esta opção.')
                        with open('Histórico_de_hashs.txt', 'a') as arq2:
                            for j in lista_parcial:
                                arq2.write('\n'+j)
                        lista_parcial.clear()
            lista_verific.clear()
            op3 = input('\nDeseja continuar verificando outras strings? (sim ou não) ')
            print('-'*100)
            if op3.lower() == 'sim':
                continue
            else:
                cont = 'não'


print('\nVERIFICADOR DE HASHS')
loop = 'sim'
while loop.lower() == 'sim':
    op4 = int(input('Digite o que deseja fazer:\n1 - Visualizar histórico salvo\n'
                    '2 - Visualizar histórico parcial de HASH que Não continha e foi adicionado ao Arquivo\n'
                    '3 - Histórico parcial de palavras verificadas\n4 - Verificar string em arquivo\n5 - Encerrar\n'))
    print('-'*100)
    if op4 == 1:
        with open('Histórico_de_hashs.txt', 'r') as arq:
            for i in arq:
                print(i)
            print('-'*100)
    elif op4 == 2:
        for i in lista_parcial_ver:
            print(i)
        print('-'*100)
    elif op4 == 3:
        for i in lista_palavras_ver:
            print(i)
        print('-'*100)
    elif op4 == 4:
        verifica(cont)
        print('-'*100)
    elif op4 == 5:
        loop = 'não'
    else:
        op5 = input('Não existe esta opção')
        print('-'*100)