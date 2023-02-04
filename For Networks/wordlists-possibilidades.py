import itertools, time

print('\nWORDLISTS/POSSIBILIDADES\n\nObs: Só é viável palavra de até 11 caracteres.')
word = input('Digite a palavra para gerar as possibilidades: ')
if len(word) > 11:
    print(f'\nA palavra "{word}" tem "{len(word)}" caracteres\nSerá inviável prosseguir com o programa')

elif len(word) <= 11:
    a = ''
    poss = 0
    res = itertools.permutations(word, len(word))
    if len(word) == 9:
        print(f'\nAVISO:\nA palavra "{word}" tem "{len(word)}" caracteres\nSerá um pouquinho mais demorado a depender da opção...')
        time.sleep(1.5)
    elif len(word) == 10:
        print(f'\nAVISO:\nA palavra "{word}" tem "{len(word)}" caracteres\nSerá mais demorado a depender da opção...')
        time.sleep(1.5)
    elif len(word) == 11:
        print(f'\nAVISO:\nA palavra "{word}" tem "{len(word)}" caracteres\nSerá consideravelmente demorado a depender da opção...')
        time.sleep(1.5)

    print(f'\nA palavra "{word}" tem "{len(word)}" caracteres.')
    im = int(input(f'\n1 - Imprimir na tela\n2 - Salvar em arquivo\n'
                   f'3 - Imprimir em tela e salvar em arquivo\nOutro - Nada\n'))
    inicio = time.time()
    if im == 1:
        for i in res:
            a += a.join(i)
            print(a)
            a = ''
            poss += 1
    elif im == 2:
        arq = open('wordlist.txt', 'w')
        for i in res:
            a += a.join(i)
            arq.write(a+'\n')
            a = ''
            poss += 1
        print('Arquivo de nome: "wordlist.txt"')

    elif im == 3:
        arq = open('wordlist.txt', 'w')
        for i in res:
            a += a.join(i)
            print(a)
            arq.write(a+'\n')
            a = ''
            poss += 1
        print('Arquivo de nome: "wordlist.txt"')

    fim = time.time()-inicio
    print(f'\nA palavra {word} gerou {poss} possibilidades\nTempo para cálculos e funcionalidades foi de: {fim:.{2}f} segundos')
