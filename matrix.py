import copy

class Matrix:
    def __init__(self, array, last_empty_position = None):
        self.array = array
        self.last_empty_position = last_empty_position

    def get_empty_position(self):
        for i in range(len(self.array)):
            if '-' in self.array[i]:
                return (i, self.array[i].index('-'))

    def generate_children(self):
        children = []
        empty_pos = self.get_empty_position()

        if empty_pos[0] > 0 and (empty_pos[0] - 1, empty_pos[1]) != self.last_empty_position:
            temp = copy.deepcopy(self.array)
            temp[empty_pos[0]][empty_pos[1]] = temp[empty_pos[0] - 1][empty_pos[1]]
            temp[empty_pos[0] - 1][empty_pos[1]] = '-'
            children.append(Matrix(temp, empty_pos))

        if empty_pos[0] < len(self.array) - 1 and (empty_pos[0] + 1, empty_pos[1]) != self.last_empty_position:
            temp = copy.deepcopy(self.array)
            temp[empty_pos[0]][empty_pos[1]] = temp[empty_pos[0] + 1][empty_pos[1]]
            temp[empty_pos[0] + 1][empty_pos[1]] = '-'
            children.append(Matrix(temp, empty_pos))

        if empty_pos[1] > 0 and (empty_pos[0], empty_pos[1] - 1) != self.last_empty_position:
            temp = copy.deepcopy(self.array)
            temp[empty_pos[0]][empty_pos[1]] = temp[empty_pos[0]][empty_pos[1] - 1]
            temp[empty_pos[0]][empty_pos[1] - 1] = '-'
            children.append(Matrix(temp, empty_pos))

        if empty_pos[1] < len(self.array[0]) - 1 and (empty_pos[0], empty_pos[1] + 1) != self.last_empty_position:
            temp = copy.deepcopy(self.array)
            temp[empty_pos[0]][empty_pos[1]] = temp[empty_pos[0]][empty_pos[1] + 1]
            temp[empty_pos[0]][empty_pos[1] + 1] = '-'
            children.append(Matrix(temp, empty_pos))

        return children

    def get_different(self, target):
        different = 0

        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                if self.array[i][j] != target.array[i][j] and self.array[i][j] != '-': 
                    different += 1 

        return different

    def __repr__(self):
        return '\n'.join(['  '.join([str(item) for item in row]) 
                        for row in self.array])

    def __str__(self):
        return '\n'.join(['  '.join([str(item) for item in row]) 
                        for row in self.array])

    def __len__(self):
        return len(self.array)
