#importação de biblioteca
import  os
#contagem de vezes e criação de variável r para armazenamento de conteúdo
vez = 0
r = ''
try:#tratamento de exceções
    #nome de arquivo para abertura
    name = input('Descriptografia de Conteúdo\n\nDigite o nome do arquivo para abertura com a extensão ".enc" ')
    #verificação da extensão
    if '.enc' not in name:
        print('-'*50)
        print('Extensão não reconhecida para procedimentos. Use ".enc"')
    else:
        #chave necessária para descriptografar
        key = input('Insira a chave necessária para descriptografia: ')
        #abertura de arquivo com o nome fornecido, em modo binário - rb
        with open(name, 'rb') as arquivo:
            #criação de laço dentro de laço para acessar cada byte
            for i in arquivo:
                for x in i:
                    #aplicação do xor em cada byte a cada vez. E adição do mesmo, descriptografado, na variável r
                    xor = chr(int(x ^ ord(key[vez])))
                    r += xor
        #exclusão de arquivo criptografado
        os.remove(name)
        #criação de variável para armazenar o nome original do arquivo, dividido por ponto
        name2 = name.split('.')
        #abertura do mesmo arquivo com nome original sem a extensão .enc, agora com .txt. Em modo w+ para escrita e leitura
        with open(name2[0]+'.txt', 'w+') as arq:
        #criação de laço para escrita descriptografada no arquivo novo, mais apresentação de conclusão
            for y in r:
                w = arq.write(y)
        print('-'*50)
        print('Operação concluída!')
#continuidade do tratamento de exceções
except Exception as e:
    print(f'Ocorreu um erro.n\nError: {e}')