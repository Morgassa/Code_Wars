def combine(*args):
    pass





print(combine(['a', 'b', 'c'], [1, 2, 3]))                                         #, ['a', 1, 'b', 2, 'c', 3])
print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]))                                   #, ['a', 1, 'b', 2, 'c', 3, 4, 5])
print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]))                      #,['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5])
print(combine([{ 'a': 1 }, { 'b': 2 }], [1, 2]))                                   #,[{"a":1},1,{"b":2},2])
print(combine([{ 'a': 2, 'b':1 }, { 'a': 1, 'b': 2 }], [1, 2, 3, 4],[5,6],[7]))    #, [{"a":2,"b":1},1,5,7,{"a":1,"b":2},2,6,3,4])