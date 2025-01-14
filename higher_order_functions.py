from functools import reduce

def sum_of_squares(list_of_numbers_to_square):
    uncommented_numbers = filter(lambda x: '#' not in x, list_of_numbers_to_square)
    numbers_as_doubles = map(float, uncommented_numbers)
    squares = map(lambda x: x**2, numbers_as_doubles)
    sum_of_squares = reduce(lambda x, y: x + y, squares)
    return int(sum_of_squares)

print(sum_of_squares(['1', '2', '#100', '3']))