class Node:
    def __init__(self, node_type):
        self.node_type = node_type
        self.single_son = None
        self.son_left = None
        self.son_right = None
        self.father = None
        self.follow_pos = None
        self.first_pos = None
        self.last_pos = None
        self.leaf = False
        self.symbol = None
        self.number_identifier = None
        self.nullable = None

    def set_sons(self, son_left, son_right):
        self.son_left = son_left
        self.son_right = son_right

    def set_father(self, father):
        self.father = father

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_single_son(self, son):
        self.single_son = son

    def set_number_identifier(self, number_identifier):
        self.number_identifier = number_identifier

    def set_as_leaf(self, symbol):
        self.leaf = True
        self.symbol = symbol

    def calculate_first_pos(self):
        self.first_pos = self.son_left.first_pos

    def calculate_last_pos(self):
        self.first_pos = self.son_left.first_pos

    def calculate_nullable(self):
        self.nullable = self.son_left.nullable
