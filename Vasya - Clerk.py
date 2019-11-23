def tickets(people):
    registradora={25:0, 50:0, 100:0}
    for nota in people:
        if nota == 25:
            registradora[25] += 1
        elif nota == 50:
            registradora[50] += 1
            if registradora[25] == 0:
                return 'NO'
            else:
                registradora[25] -= 1
        elif nota == 100:
            registradora[100] += 1
            if registradora[25] >= 1 and registradora[50] >=1:
                registradora[25] -= 1
                registradora[50] -= 1
            elif registradora[25] >=3:
                registradora[25] -= 3
            else:
                return 'NnO'
    return "YES"

# def tickets(people):

#     caixa = {25:0, 50:0, 100:0}
#     for money in people:
#         if money == 25:
#             caixa[25]+=1
#         elif money == 50:
#             if money[25] == 0:
#                 return 'NO'
#             caixa[25] -= 1
#             caixa[50] += 1
#         else:
#             caixa[100] += 1
#             if caixa[25] >= 1 and caixa[50] >= 1:
#                 caixa[25] -= 1
#                 caixa[50] -= 1
#             elif caixa[25] >= 3:
#                 caixa[25] -= 3
#             else:
#                 return 'NO'
#     return 'YES'








pagamentos = [25, 25, 25, 25, 100]

print(tickets(pagamentos))
tickets(pagamentos)

