def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    soma = 0

    while True:
        current_soma = 0
        # enumerate(str(n)[::-1] serve para inverter a ordem das strings em 'n'.
        for index, digit in enumerate(str(n)[::-1]):
            # Aqui é feita a coreelação da posição do valor em 'n' com seu respectivo par em pattern.
            # Por se tratar de um padrão o valor do index dever correr dentro da 'pattern' repetidas vezes
            # para isso dividimos o index pelo comprimento total da string 'pattern'.
            current_index = index % len(pattern)
            # Já sabendo o valor correspondente dentro de 'pattern' podemos fazer a multiplicação e soma-las.
            current_soma += int(digit) * pattern[current_index]
        # Se a soma não for iguql a 'n' o estrutura toda se repete.
        if soma == current_soma:
            return soma

        soma = current_soma
        n = current_soma
        
print(6%6)
print(thirt(178))