'''
If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)

The input will always be in lowercase and never be empty.
'''
import string

def words_to_marks(s):
    let_num ={}
    soma=0
    letras = list(string.ascii_lowercase)
    for x,y in zip(letras, range(1, len(letras)+1)):
        let_num[x]=y
    
    s_list = list(s)
    for i in s_list:
        soma += (let_num[i])
    return soma




print(words_to_marks('attitude'))
print(words_to_marks('friends'))
print(words_to_marks('family'))
print(words_to_marks('selfness'))
print(words_to_marks('knowledge'))