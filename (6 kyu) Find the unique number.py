# def find_uniq(arr):
#     number=0
#     uniques=[]
#     for i in arr:
#         number=arr.count(i)
#         if number == 1:
#             if uniques.count(i) == 0:
#                 uniques.append(i)
#             # print(i, number)
#     print(uniques[0])


def find_uniq(arr):
    mylist = list(dict.fromkeys(arr))
    for i in mylist:
        number = arr.count(i)
        if number == 1:
            return i


## CODEWAR SOLUTION ##