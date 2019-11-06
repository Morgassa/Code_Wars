# def zeros(n):
#     count =0
#     i=5
#     while (n/i>=1):
#         count+= int(n/i)
#         i *= 5
#     return int(count)


def zeros(n):

    # No factorial is going to have fewer zeros than the factorial of a smaller
    # number.
    #
    # Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
    # smaller than `n` (`n // 5`).
    #
    # Each multiple of 25 adds two 0's, so next we add another 0 for each multiple
    # of 25 smaller than n.
    #
    # We continue on for all powers of 5 smaller than (or equal to) n.


    # A cada multiplo de 5 é adicionado um 0, primeiramente contamos quantos multiplos
    # de 5 são menores do que 'n' -> (n//5).
    # A cada multiplo de 25 adicionados dois 0's, entãa adicionamos outro 0 para cada
    # multiplo de 25 menor que n.
    # Continuamos por todos os "powers" de 5 (menor ou iqual) a 'n'.

    pow_of_5 = 5
    zeros = 0

    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 = pow_of_5 * 5
    return zeros


print(zeros(30))