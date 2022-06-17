#importação de biblioteca
import os
#criação de opções para execução das funcionalidades do programa
op = input('Criptografia de conteúdo\n\nDigite;\n1 - Se deseja abrir arquivo existente e criptografar com chave\n'
           '2 - Se deseja criar, escrever conteúdo e criptografar com chave ')
#contagem de vezes e criação de variável r para armazenamento de conteúdo
vez = 0
r = ''
if op == '1': #opção 1 para arquivo existente e com tratamento de exceções
    try:
        print('-'*50)
        #nome de arquivo para abertura e chave desejada para criptografar
        name = input('Digite o nome do arquivo para abertura: (com extensão ".(...)") ')
        key = input('Insira a palavra chave desejada para criptografar: ')
        #abertura de arquivo com o nome fornecido, em modo binário - rb
        with open(name, 'rb') as arquivo:
            #criação de laço dentro de laço para acessar cada byte
            for i in arquivo:
                for x in i:
                    #aplicação do xor em cada byte a cada vez. E adição do mesmo, criptografado, na variável r
                    xor = chr(x ^ ord(key[vez]))
                    r += xor
        #exclusão de arquivo não criptografado
        os.remove(name)
        #criação de variável para armazenar o nome original do arquivo, divido por ponto
        name2 = name.split('.')
#abertura do mesmo arquivo com nome original,sem extensão antiga, mas com a extensão .enc adicionada, em modo w+ para escrita e leitura
        with open(name2[0]+'.enc', 'w+') as arq:
        #criação de laço para escrita criptografada no arquivo novo, mais apresentação de conclusão
            for y in r:
                w = arq.write(y)
        print('-'*50)
        print('Operação concluída!')
    #continuidade do tratamento de exceções
    except Exception as e:
        print(f'Ocorreu um erro.n\nError: {e}')

#Opção 2 (Adicional)
elif op == '2': #opção 2 para criação de arquivo com conteúdo na hora e com tratamento de exceções
    try:
        print('-'*50)
        #digitar qual será o nome do arquivo e seu conteúdo, sem declarar extensão
        name = input('Digite o nome do arquivo para criação e abertura (sem extensão): ')
        ct = input('Digite o conteúdo do arquivo para criptografia: ')
        #extensão adicionada automaticamente ao nome do arquivo e digitação da chave desejada para codificação
        name += '.enc'
        key = input('Insira a chave desejada para criptografar: ')
        #abertura de arquivo em modo w+ para escrever o conteúdo desejado
        with open(name, 'w+', encoding='utf-8') as arq:
            w = arq.write(ct)
        #abertura de arquivo em modo rb, binário para efetuar codificação
        with open(name, 'rb') as arquivo:
            #criação de laço dentro de laço para acessar cada byte
            for i in arquivo:
                for x in i:
                    #aplicação do xor em cada byte a cada vez. E adição do mesmo, criptografado, na variável r
                    xor = chr(x ^ ord(key[vez]))
                    r += xor
        #abertura de arquivo em modo a, para adicionar conteúdo criptografado
        with open(name, 'a', encoding='utf-8') as arqv:
            #exclusão do conteúdo não criptografado
            arqv.seek(0)
            a = arqv.truncate()
            #criação de laço para a adição de escrita criptografada, mais apresentação de conclusão
            for y in r:
                w = arqv.write(y)
        print('-'*50)
        print('Operação concluída!')
    #continuidade do tratamente de exceções
    except Exception as e:
        print(f'Ocorreu um erro.n\nError: {e}')
#caso alguém digite uma numeração diferente das opções 1 e 2, a mensagem é apresentada e o programa é encerrado
else:
    print('-'*50)
    print('Número diferente das opções.\nPrograma encerrado!')

#EVITE USAR QUALQUER ACENTUAÇÃO NO CONTEÚDO DO ARQUIVO