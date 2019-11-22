def get_sum(a,b):
    list=[]
    i = min(a, b)
    f = max(a, b)
    list.append(i)
    while list[-1] < f:
        i = i+1
        list.append(i)
        # print(list)
    return sum(list)

# def get_sum(a,b):
# sdsd
#     return sum(range(min(a, b), max(a, b) + 1))