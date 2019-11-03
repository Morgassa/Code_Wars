def generator_factoral(n):
    for numbers in range(1,n+1):
        yield (numbers)

def generator_trail():
    pass

def zeros(n):
    if n != 0:
        x =generator_factoral(n)
        multi=1
        for i in x:
            multi = multi*i
        print(multi)
        x = str(','.join(str(multi)))
        return x.count('0')
    else:
        return 1








print(zeros(100))



# Examples
#
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros