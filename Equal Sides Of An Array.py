def find_even_index(arr):
    print(arr)
    indx=0
    list=[]
    for i in arr:
        list.append(i)
    for x in list:
        indx+=1
        indx2 = indx - 1
        if sum(list[:indx2]) == sum(list[indx::]):
            return indx2

    for x in list:
        indx+=1
        indx2 = indx - 1
        if sum(list[:indx2]) != sum(list[indx::]):
            return -1


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


