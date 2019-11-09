def sum_dig_pow(a, b):
    b=b+1
    lista = list(range(a,b))
    print(lista)
    lista_resp=[]
    for number in lista:
        if int(number) <= 9:
            lista_resp.append(int(number))
        else:
            x_lista = list(map(int,str(number))) #CONVERTE AS SRINGS DE UMA LISTA PARA INTEIROS E JOGA NA LISTA 'X_LISTA'.
            for i in x_lista:
                x_lista = list(map(lambda x: x, x_lista))
                count2 =list(range(1,len(x_lista)+1))
            resp = sum(map(lambda x, y: x ** y, x_lista, count2)) #TRAZ A POTÊNCIA ENTRE DUAS LISTAS DIFERENTES E DEPOIS SOMA OS VALORES.
            count2 = []
            if number == resp:
                lista_resp.append(resp)
    return lista_resp

'''CODEWAR BEST PRACTICISES AND CLEVER'''

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))