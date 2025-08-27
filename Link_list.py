
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "node data is: %s" % self.data
    
n1 =Node(10)
print(n1)
