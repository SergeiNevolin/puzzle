import uuid

from matrix import Matrix

class Node(object):

    def __init__(self, matrix, target,  parent=None, children=None):
        self.uuid = uuid.uuid1()
        self.matrix = matrix
        self.target = target
        self.parent = parent
        self.depth = self.get_depth()
        self.different = matrix.get_different(self.target)
        self.value = self.get_value()
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def get_depth(self):
        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth

    def get_value(self):
        return self.depth + 4 * self.different

    def add_child(self, node):
        node.parent = self
        assert isinstance(node, Node)
        self.children.append(node)

    def __lt__(self, other):
        return self.get_value() < other.get_value()

    def __repr__(self):
        return '\n'.join(['  '.join([str(item) for item in row]) 
                        for row in self.matrix.array])

    def __str__(self):
        return '\n'.join(['  '.join([str(item) for item in row]) 
                        for row in self.matrix.array])