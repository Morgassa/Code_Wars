def generator(args):
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

def solution(ranges):
    ddd = generator(ranges)
    ls=''
    count=0
    for r in ddd:
        count+=1
        if len(r) == 2:
            ls+=(''.join(('{}-{},'.format(r[0], r[1]))))
        else:
            ls+=(''.join(('{},'.format(r[0]))))
    return (ls[:-1])



## CODEWARS RESOLUTION ##
## CODEWARS RESOLUTION ##

def solution(args):
    out = []
    started = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == started:
                out.append(str(started))
            elif end == started + 1:
                out.extend([str(started), str(end)])
            else:
                out.append(str(started) + "-" + str(end))
            started = n
        end = n
    return ",".join(out)