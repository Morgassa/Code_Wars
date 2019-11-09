def diamond(n):
    resp=''
    if n %2 != 0 and n > 0:
        for i in range(1,n+1,2):
            spaces=int((n-i)/2)
            resp = resp+'{}{}\n'.format(' '*spaces,'*'*i,)
        for i in range(n-2, 0, -2):
            spaces=int((n-i)/2)
            resp = resp +'{}{}\n'.format(' '*spaces,'*'*i,)
    else:
        return None
    return resp


print(diamond(7))