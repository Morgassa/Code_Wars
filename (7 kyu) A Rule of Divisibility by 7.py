'''
Um número 'm' da forma 10x + y é divisível por 7 se e somente se x - 2y é divisível por 7.
Em outras palavras, subtraia duas vezes o último dígito do número formado pelos dígitos 
restantes. Continue fazendo isso até que um número conhecido como ''divisível ou não por 7'' 
seja obtido; você pode parar quando esse número tiver no máximo 2 dígitos, porque você 
deve saber se um número de no máximo 2 dígitos é divisível por 7 ou não.

O número original é divisível por 7 se e somente se o último número obtido usando este 
procedimento for divisível por 7.
'''

'''
def seven(m):
    # Converte 'm' para uma lista.
    number_list = list(str(m))
    # Variavé de manobra.
    new_number = 0
    # Constando os passos.
    step = 0
    # Enquanto o comprimento na lista for maior do que 2. 
    while(len(number_list) > 2):
        # Retira o ultimo número da lista e converte para númeral inteiro na variavél 'last_number'.
        last_number = int(number_list.pop(len(number_list)-1))
        # Com o ultimo string da lista já retirado converte-se o restante da lista para um númeral inteiro.
        remaining = int(''.join(number_list))
        # Executa a equação x - 2y e atribui a uma nova variavél.
        new_number = remaining - 2 * last_number
        # Atribui o valor da nova variavel a lista inicial no inicio do 'while'.
        number_list = list(str(new_number))
        # Adiciona um passo ao processo.
        step += 1
    # Converte a lista a um numero integral.
    divisible = int(''.join(number_list))
    # retorna a resposta desejada.
    return (divisible, step)
    '''
def seven(m):
    lista_numeros = list(str(m))
    novo_numero=0
    passos=0
    
    while len(lista_numeros) > 2:
        ulti_numero = int(lista_numeros.pop(len(lista_numeros)-1))
        rest_numeros = int(''.join(lista_numeros))
        novo_numero = rest_numeros - (ulti_numero * 2)
        lista_numeros = list(str(novo_numero))
        passos+=1
    div = int(''.join(lista_numeros))
    return (div, passos)











# print(seven(600290))
# print(seven(648761))
print(seven(131480))
print(seven(3265623))
# print(seven(643145))
# print(seven(0))
# print(seven(372))
# print(seven(1603))
# print(seven(371))
# print(seven(483))
# print(seven(477557101))
