def sum_two_smallest_numbers(numbers):

    menor1, menor2 = numbers[0], numbers[1]


    if menor1 > menor2:
        menor1, menor2 = menor2, menor1  


    for num in numbers[2:]:  
        if num < menor1:  
            menor2,menor1 = menor1,num 
        elif num < menor2:  
            menor2 = num  

    return menor1 + menor2

print(sum_two_smallest_numbers([19, 5, 42, 2, 77])) 