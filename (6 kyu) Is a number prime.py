
def is_prime(num):
    num_pares = [0,2,4,6,8]
    par = list(map(lambda x: x, str(num)))
    print(par)
    if int(par[-1]) in num_pares:
        print('Não primo é PAR')
    else:
        anteriores = list(range(2,num))
        lista = list(map(lambda x: num%x, anteriores))
        print(anteriores)
        print(lista)
        if 0 in lista:
            print(lista)
            print(num, 'Nao Primo')
        else:
            print('Primo')

is_prime(13183)