def order(sentence):
    listinha=[]
    dict={}
    x = sentence.split()
    #print(len(x))
    for word in sentence.split():
        # print(word)
        for letter in word:
            if letter.isdigit():
                dict[letter] = word
            else:
                continue
                # print(letter)
    for number in range(1, len(x)+1):
        listinha.append(dict[str(number)])
    return ' '.join(listinha),'ok'











print (order("is2 Thi1s T4est 3a"))                    # "Thi1s is2 3a T4est")
print (order("4of Fo1r pe6ople g3ood th5e the2"))      # "Fo1r the2 g3ood 4of th5e pe6ople")
print (order(""))                                      # "")