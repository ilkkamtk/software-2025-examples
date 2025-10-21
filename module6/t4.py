def sum_of_numbers(numbers):
    summa = 0
    for i in numbers:
        summa = summa + i
    return summa

number_list=[3,5,9,2,6,8,4,7,12]
result=sum_of_numbers(number_list)
print(result)