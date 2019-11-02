def solution(args):
    len_arsgs = len(args)
    i = 0
    while i < len_arsgs:
        low = args[i]

        # Enquanto o contador 'i' for um caracter menor que o tamanho da lista e
        # o valor do argumento atual +1 for igual ao proximo.
        # Soma-se 1 ao contador 'i'.

        while i < len_arsgs-1 and args[i]+1 == args[i+1]:
            i+=1

        # Ao quebrar a sequencia numerica a variavel 'hi' passa a ser o ultimo numero
        # da sequencia verificado.

        hi = args[i]

        # Se ouver algum numero entre o valor do 'hi' e do 'low' yield guarda apenas
        # os dois valores posicionados nas extremidadas da sequancia numerica. O maior
        # e o menor.

        if hi - low >= 2:
            yield (low, hi)

        # Se os números forem apenas consecutivos mas são apenas dois, 'hi' e 'low' são
        # quardados separadamente.

        elif hi - low == 1:
            yield (low,)
            yield (hi,)

        # Não havendo valor consecutivo, sendo assim não tem o porque
        # separa-los em 'hi' e 'low'.

        else:
            yield (low,)
        i+=1

def printtr(ranges):
    ll=[]
    count=0
    for r in ranges:
        count+=1
        if len(r) == 2:
            sep='~'
            print(r[0], r[1])
            ll.append([('{} ~> {}'.format(r[0], r[1]))])
            # ll.append(int(r[0])+sep+int(r[1]))
        else:
            ll.append(('{}'.format(r[0])))
    print(ll)



#
# def printtr(ranges):
#     print(','.join((('%i-%i' % r) if len(r) == 2 else '%i' % r) for r in ranges))

if __name__ == '__main__':
    for lst in [[-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7,
                 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]]:
        #print(list(solution(lst)))
        printtr(solution(lst))
