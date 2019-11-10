def nb_dig(n, d):
    total=0
    full_lista = list(range(0, n+1))
    interest_lista =[]

    for i in full_lista:
        square_of_number = i**2
        if str(d) in str(square_of_number):
            interest_lista.append(square_of_number)
            count_d_in_string = list(str(square_of_number)).count(str(d))
            total += count_d_in_string
            
    return (total)
    







# print(nb_dig(25, 1))   #4700
print(nb_dig(5750, 0))   #4700
# print(nb_dig(11011, 2))  #9481
# print(nb_dig(12224, 8))  #7733
# print(nb_dig(11549, 1))  #11905


# n = 10, d = 1, the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# We are using the digit 1 in 1, 16, 81, 100. The total count is then 4.

# nb_dig(25, 1):
# the numbers of interest are
# 1, 4, 9, 10, 11, 12, 13, 14, 19, 21 which squared are 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
# so there are 11 digits `1` for the squares of numbers between 0 and 25.