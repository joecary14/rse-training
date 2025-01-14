class Node(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.value = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.value}, {self.children})"

#    +
#   / \
#  1  *
#    / \
#   2   3
t = Node('+', [Node('1'),
               Node('*', [Node('2'),
                          Node('3')])])

def get_number_of_nodes(node : Node):
    if node.children is None:
        return 1
    
    else:
        return 1 + sum(get_number_of_nodes(node) for node in node.children)
    
nodes = get_number_of_nodes(t)
print(nodes)

def get_result(node : Node):
    if not node.children:
        return int(node.value)
    
    else:
        if node.value == '+':
            return get_result(node.children[0]) + get_result(node.children[1])
        
        elif node.value == '*':
            return get_result(node.children[0]) * get_result(node.children[1])
        
        elif node.value == '-':
            return get_result(node.children[0]) - get_result(node.children[1])
        
        elif node.value == '/':
            return get_result(node.children[0]) / get_result(node.children[1])
        
result = get_result(t)
print(result)