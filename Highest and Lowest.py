def high_and_low(numbers):
    numeros = numbers.split(' ')
    x = list(map(int,numeros))
    return str(max(x))+" "+str(min(x))

#codewars resolution

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))