def sum_two_smallest_numbers(numbers):
    sum=sorted(numbers)[0]+sorted(numbers)[1]
    return sum


print(sum_two_smallest_numbers([5, 8, 12, 18, 22,5]))
