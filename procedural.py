import numpy as np

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

def attach_names(data, names):
    result = []
    for i, name in enumerate(names):
        result.append({'name': name.capitalize(), 'data': data[i].tolist()})
    return result

print(attach_names(data, ['alice', 'bob']))