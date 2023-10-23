class LexicalTree:
    def __init__(self):
        self.nodes = []
        self.follow_pos = dict()

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def calculate_follow_pos(self):
        for node in self.nodes:
            node.calculate_follow_pos()
