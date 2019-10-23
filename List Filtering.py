def filter_list(l):
    resp=[]
    for i in range(len(l)):
        if type(l[i]) == type(1):
            resp.append(l[i])
    return resp

def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

def filter_list(l):
  return filter(lambda x: not type(x) is str, l)