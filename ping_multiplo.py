import time
import os

conteudo = ''
c = 's'
while c.lower() == 's':
    assunto = input('Digite IP para ping multiplo: ')
    conteudo += assunto+'\n'
    c = input('Deseja continaur adicionando? ')

with open('hosts.txt', 'w+', encoding='utf-8', newline='') as arq:
    escrever = arq.write(conteudo)

with open('hosts.txt', 'r', encoding='utf-8', newline='') as arqv:
    ler = arqv.readlines()
    for ip in ler:
        os.system(f'ping -n 8 {ip}')
        time.sleep(1)
        print('-'*70)
