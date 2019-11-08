def sum_cubes(n):
    resp=0
    x = list(range(1,n+1))
    for i in x:
        resp += i**3
    return (resp)