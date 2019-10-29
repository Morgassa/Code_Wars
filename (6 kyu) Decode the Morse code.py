MORSE_CODE = {
    'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-', 'SOS':'...---...',
    '   ':' ', '!':'-.-.--'
}
#
#
def decodeMorse(morse_code):
    dict={}
    translated_code=[]
    morse_code = morse_code.replace('   ',' / ')
    # print(morse_code)
    split_code = list(morse_code.split(' '))
    while '' in split_code:
        split_code.remove('')
    while '/' in split_code[0]:
        split_code.remove('/')
    # print('splited:', split_code)
    # Invertendo keys and values.
    for (v, k) in zip(MORSE_CODE.values(), MORSE_CODE.keys()):
        # creating new dict.
        dict[v] = k
    for code in split_code:
        if code == '/':
            translated_code.append(' ')
        elif code not in dict:
            continue
        else:
            translated_code.append(dict[code])
    message = ''.join(translated_code)
    return message

# !!! CODEWAR RESOLUTIONS !!!

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
