def solution(args):
    resp_list=[]
    rep=[]
    rep.append(args[0])
    for a, b in zip(args, range(0,len(args))):
        # print(a,b)
        print(args.index(a), b)
        # if rep[-1]+1 == args[b] and rep[-1]+2 == args[b+1]:
        #     rep.append(a)
        # rep.append(a)
        # print(rep[-1], args[b+1], args[b+2])

        # print(a,b)

    print(rep)
    print(args)
    return 'o'
    # your code here







#solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20])