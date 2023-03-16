class Node:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_adjacent(self, adjacent_node, weight=0):
        self.adjacent[adjacent_node] = weight

    def get_adjacent(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, adjacent_node):
        return self.adjacent[adjacent_node]

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.nodes = {}
        self.size = 0

    def add(self, node):
        self.size += 1
        self.nodes[node] = Node(node)  # assuming nodes are added by IDs and IDs are unique

    def get_node(self, node):
        if node in self.nodes:
            return self.nodes[node]
        else:
            return None

    def add_edge(self, origin, destination, cost=0):
        if origin not in self.nodes:


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    node
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
