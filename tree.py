from heapq import heappop, heappush

from node import Node
from utils import timer

class Tree:

    def __init__(self):
       self.root = None
       self.height = 0
       self.nodes = []

    def generate_nodes(self, node):
        children = node.matrix.generate_children()

        for child in children:
            self.insert(Node(child, node.target, parent=node), node)

    def insert(self, node, parent):
        if parent is None:
            if self.root is None:
                self.root = node
        else:
            parent.add_child(node)

        heappush(self.nodes, node)

    @timer
    def solve(self):
        if self.root is None:
            return

        iterations = 0
        cur_node = heappop(self.nodes)

        while cur_node.different != 0:
            self.generate_nodes(cur_node)
            cur_node = heappop(self.nodes)
            iterations += 1

        print('iter count', iterations)
        print('node depth', cur_node.depth)

        return cur_node

    def root(self):
        return self.root