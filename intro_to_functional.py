numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

squared_fc_function = list(map(square, numbers))
squared_lambda = list(map(lambda x: x ** 2, numbers))

