def get_middle(var):
    print(var)
    list=[]

    for i in var:
        list.append(i)
    if len(list)%2 == 0:
        mid = len(list)/2
        return '{}{}'.format(list[int(mid-1)], list[int(mid)])
    else:
        mid = len(list)//2
        return '{}'.format(list[int(mid)])

    print (list, len(list)//2)

print(get_middle('amadeu'))
