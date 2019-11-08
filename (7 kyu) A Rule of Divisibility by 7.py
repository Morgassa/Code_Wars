def seven(m):
    parametro=2
    count_runs=0
    n_string = str(m)
    if m == 0:
        return (0,0)
    value = int(n_string[:-1]) - (int(n_string[-1]) * parametro)
    qd = len(list(map(int,str(m))))
    # print('value:', value)
    if value % 7 != 0 and qd > 2:
        value = int(n_string[:-1]) - (int(n_string[-1]) * parametro)
        n_string=str(value)
        count_runs+=1
        # print ('ops')
    while value % 7 == 0 and qd > 2:
        value = int(n_string[:-1]) - (int(n_string[-1]) * parametro)
        n_string=str(value)
        count_runs+=1
        qd = len(list(map(int,str(value))))
  
    return(int(n_string), count_runs)


print(seven(0))
print(seven(372))
print(seven(1603))
print(seven(371))
print(seven(483))
print(seven(477557101))
