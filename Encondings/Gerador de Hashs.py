import hashlib

print('\nGERADOR DE HASHS')
op = int(input('Escolha a opção de HASH:\n1 - MD5\n2 - SHA1\n3 - SHA224\n4 - SHA256\n5 - SHA384\n6 - SHA512\n7 - Todos\n'))
strs = input('Digite a string que deseja gerar o HASH: ')
print('Obs: Todos os resultados estão resumidos/apresentados em hexadecimal.')
print('-'*100)

if op == 1:
    res = hashlib.md5(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em MD5 é:\n{res.hexdigest()}')

elif op == 2:
    res = hashlib.sha1(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA1 é:\n{res.hexdigest()}')

elif op == 3:
    res = hashlib.sha224(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA224 é:\n{res.hexdigest()}')

elif op == 4:
    res = hashlib.sha256(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA256 é:\n{res.hexdigest()}')

elif op == 5:
    res = hashlib.sha384(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA384 é:\n{res.hexdigest()}')

elif op == 6:
    res = hashlib.sha512(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA512 é:\n{res.hexdigest()}')

elif op == 7:
    res = hashlib.md5(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em MD5 é:\n{res.hexdigest()}')

    res = hashlib.sha1(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA1 é:\n{res.hexdigest()}')

    res = hashlib.sha224(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA224 é:\n{res.hexdigest()}')

    res = hashlib.sha256(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA256 é:\n{res.hexdigest()}')

    res = hashlib.sha384(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA384 é:\n{res.hexdigest()}')

    res = hashlib.sha512(strs.encode('UTF-8'))
    print(f'\nO hash de {strs} em SHA512 é:\n{res.hexdigest()}')

else:
    print('Não existe esta opção !')

