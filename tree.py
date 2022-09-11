from heapq import heappop, heappush
from collections import deque

import graphviz

from node import Node
from utils import timer

class Tree:

    def __init__(self):
       self.root = None
       self.height = 0
       self.nodes = []
       self.solution_path = []

    def root(self):
        return self.root

    def insert(self, node, parent):
        if parent is None:
            if self.root is None:
                self.root = node
        else:
            parent.add_child(node)

    @timer
    def solve(self):
        if self.root is None:
            return

        iterations = 0

        heappush(self.nodes, self.root)
        cur_node = heappop(self.nodes)

        while cur_node.different != 0:
            children = cur_node.matrix.generate_children()
            for child in children:
                new_node = Node(child, cur_node.target, parent=cur_node)
                self.insert(new_node, cur_node)

                heappush(self.nodes, new_node)

            cur_node = heappop(self.nodes)

            iterations += 1

        print('iter count', iterations)
        print('node depth', cur_node.depth)

        self.solution_path = self.find_solution_path(cur_node)

        return cur_node

    def find_solution_path(self, solution_node):
        path = []
        path.append(solution_node.uuid)
        parent = solution_node.parent
        while parent is not None:
            path.append(parent.uuid)
            parent = parent.parent
        
        return path[::-1]

    @timer
    def display(self):
        if self.root is None:
            return

        d = graphviz.Digraph(filename='tree.gv')
        d.attr('node', shape='square')

        queue = deque([self.root])
        d.node(str(self.root.uuid), str(self.root))
        while queue: 
            node = queue.popleft()
            if node.uuid in self.solution_path:
                d.node(str(node.uuid), str(node), style='filled', fillcolor='green')
            else:
                d.node(str(node.uuid), str(node))

            for child in node.children:
                d.edge(str(node.uuid), str(child.uuid))

                queue.append(child) 

        d.view()
