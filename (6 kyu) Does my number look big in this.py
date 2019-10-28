def narcissistic(value):
    resp=0
    xxx = list(map(int, str(value)))
    for number in xxx:
        resp = resp + number**(len(xxx))
    if resp == value:
        return True
    return False

# !!! CODEWAR RESOLUTIONS !!!

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))