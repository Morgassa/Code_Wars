def adjacent_element_product(array):
    max_value =0
    arrays =[]
    
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if abs(i-j) == 1:
                arrays.append(array[i]*array[j])
    
    return (max(arrays))






print(adjacent_element_product([5, 8]))
print(adjacent_element_product([1, 2, 3]))
print(adjacent_element_product([1, 5, 10, 9])) 
print(adjacent_element_product([4, 12, 3, 1, 5]))
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))
print(adjacent_element_product([9, 5, 10, 2, 24, -1, -48]))
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))