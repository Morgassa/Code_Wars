
# upSpeed -> taxa de crescimento diurno.
# downSpeed -> taxa de DEcrescimento noturno.
# desiredHeight -> Alturo final desejada.

def growing_plant(upSpeed, downSpeed, desiredHeight):
    n_dias = 0
    Height = 0
    
    if desiredHeight <= (upSpeed - downSpeed):
        n_dias =  1
        return (n_dias)
    
    while Height < desiredHeight:
        n_dias += 1
        Height += upSpeed
        if desiredHeight <= Height:
            break
        else:
            Height -= downSpeed
    
    return (n_dias)
    # return n_dias

print(growing_plant(87,3,72))
print(growing_plant(85,57,20))
print(growing_plant(81,49,30))


# print(growing_plant(100,10,910))
# print(growing_plant(10,9,4))
# print(growing_plant(5,2,0))
# print(growing_plant(5,2,5))
# print(growing_plant(5,2,6))