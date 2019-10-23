def digital_root(n):
    if n != 0:
        a = reduz(n)[1]
        b = reduz(n)[0]
        while b > 1:
            a = reduz(b)[0]
            b = reduz(a)[1]
        return a
    else:
        return 0


def reduz(lista):
   new_lista=[]
   n = str(lista)
   for i in n:
       new_lista.append(int(i))
   return sum(new_lista), len(new_lista)


#CODEWARS SOLUTION

def digital_root_CW(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

print(digital_root_CW())