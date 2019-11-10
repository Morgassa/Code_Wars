'''
https://medium.com/rafaeltardivo/python-entendendo-o-uso-de-args-e-kwargs-em-fun%C3%A7%C3%B5es-e-m%C3%A9todos-c8c2810e9dc8
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
'''
def combine(*args):
    result = []
    args_length = len(args)
    # Identifica o valor do 'args' com mais irformação.
    max_len_list = max([len(l) for l in args])
    # O primeiro loop considera o argumento com mais informações gerando numeros que vão de 0 ao maior
    # valor possivel.
    for i in range(max_len_list):
        # Esse segundo loop vai levar em consideração a quantidade de argumentos. Por estar abaixo do 
        # loop anterior esse irá correr por todos os argumentos mantendo o valor de 'i' do loop anterior
        # fixo.
        for j in range(args_length):
            # Se o argumento tiver comprimento compativel com o valor de 'i' ele será adicionado ao resultado.  
            if len(args[j]) > i:
                result.append(args[j][i])
    return result



print(combine(['a', 'b', 'c'], [1, 2, 3, 4]))                                         #, ['a', 1, 'b', 2, 'c', 3])
# print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]))                                   #, ['a', 1, 'b', 2, 'c', 3, 4, 5])
# print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]))                      #,['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5])
# print(combine([{ 'a': 1 }, { 'b': 2 }], [1, 2]))                                   #,[{"a":1},1,{"b":2},2])
# print(combine([{ 'a': 2, 'b':1 }, { 'a': 1, 'b': 2 }], [1, 2, 3, 4],[5,6],[7]))    #, [{"a":2,"b":1},1,5,7,{"a":1,"b":2},2,6,3,4])