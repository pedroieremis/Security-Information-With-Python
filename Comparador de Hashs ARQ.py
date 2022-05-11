import hashlib

print('\nCOMPARADOR DE HASHS\n')
arq1 = input('Digite o nome do primeiro arquivo à comparar o conteúdo: ')
try:
    with open(arq1, 'rb') as arq:
        arq.read()
    arq2 = input('Digite o nome do segundo arquivo à comparar o conteúdo: ')
    try:
        with open(arq2, 'rb') as arq:
            arq.read()

        hash1 = hashlib.new('sha256')
        hash1.update(open(arq1, 'rb').read())

        hash2 = hashlib.new('sha256')
        hash2.update(open(arq2, 'rb').read())

        print(f'Hash do primeiro arquivo em SHA256:   {hash1.hexdigest()}\nHash do segundo arquivo em SHA256:   {hash2.hexdigest()}')
        print('-'*len(hash1.hexdigest())*2)
        if hash1.hexdigest() == hash2.hexdigest():
            print('A comparação indicou Verdadeiro/Igual')
        else:
            print('A comparação indicou Falso/Diferente')
    except:
        print('Segundo arquivo inesxistente !\nPrograma encerrado !')
except:
    print('Primeiro arquivo inesxistente !\nPrograma encerrado !')


