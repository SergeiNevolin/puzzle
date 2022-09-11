from node import Node
from tree import Tree
from matrix import Matrix


# start = Matrix([
#     ['2', '4', '3'],
#     ['1', '8', '5'],
#     ['7', '-', '6']
# ])

# target = Matrix([   
#     ['1', '2', '3'],
#     ['4', '5', '6'],
#     ['7', '8', '-']
# ])

start = Matrix([
    ['2', '1', '6'],
    ['4', '-', '8'],
    ['7', '5', '3']
])

target = Matrix([   
    ['1', '2', '3'],
    ['8', '-', '4'],
    ['7', '6', '5']
])

root = Node(start, target)

print(root)
print()

tree = Tree()
tree.insert(root, None)

result = tree.solve()
print(result)

tree.display()


