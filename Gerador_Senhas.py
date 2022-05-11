import string, random

print('\nGERADOR DE SENHAS SEGURAS/COMPLEXAS')

lista_s = []

def arqs(num):
    with open('chaves.txt', 'w', encoding='UTF-8') as arq:
        arq.write(f'CHAR: {num}\nQTD: {len(lista_s)}\n\nSENHA(S):\n\n')
        for i in lista_s:
            arq.write(i+'\n')

def gerador(num):
    if num < 6:
        print('-'*75)
        print('Infelizmente esta senha será insegura, portanto não continuaremos com o Gerador')
    else:
        chars = string.ascii_letters + string.digits + "!@#$%¨&*()_+=-§¬¢£]}º[{~^;:.,<>\|/'ç"
        rnd = random.SystemRandom()
        senhas = ''
        print('-'*75)
        print(f'\nSenha Gerada com {num} caracteres:')
        for i in range(num):
            a = rnd.choice(chars)
            senhas += a
        lista_s.append(senhas)
        print(senhas)

op = input('\n1 - Várias senhas em loop\n2 - Uma única senha\n3 - Loop com salvamento em arquivo\n4 - Única com salvamento em arquivo\n')

num = int(input('Digite a quantidade de caracteres para criação de senha(s):\n\nObs1: Por segurança o mínimo são 6 caracteres'
                '\nObs2: O ideal mesmo é no mínimo 8 caracteres\n'))

print('-'*75)
if op == '1':
    loop1 = int(input('Digite a quantiade de senhas a serem Criadas: '))
    for i in range(loop1):
        gerador(num)

elif op == '2':
    gerador(num)

elif op == '3':
    loop1 = int(input('Digite a quantiade de senhas para criação em loop: '))
    for i in range(loop1):
        gerador(num)
    arqs(num)
    print('\nArquivo com nome: chaves.txt')

elif op == '4':
    gerador(num)
    arqs(num)
    print('\nArquivo com nome: chaves.txt')

else:
    print('Opção Inexistente.')

