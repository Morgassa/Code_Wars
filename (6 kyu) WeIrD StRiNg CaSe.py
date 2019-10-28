def to_weird_case(string):
    count = 0
    position=[]
    words_list = list(map(str,string))
    resp=[]
    #position_list = list(range(1, len(string)))
    for word in words_list:
        count+=1
        if word == ' ':
            count=0
            position.append(' ')
            continue
        position.append(count)
    for (w, p) in zip(words_list, position):
        if type(p) == int and p%2 != 0:
            w = w.upper()
            resp.append(w)
            continue
        resp.append(w)
    str_join = "".join(resp)
    return str_join

# !!! CODEWAR RESOLUTIONS !!!

def to_weird_case_word(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))


def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())