class Node:
    def __init__(self, name, par = None):
        self.name = name
        self.par = par
    def display(self):
        print(self.name)

from collections import defaultdict

data = defaultdict(list)
data['A'] =['D', 'N', 'K']
data['D'] =['G']
data['N'] =['S','P']
data['K'] =['Z']
data['S'] =['T', 'C']
data['Z'] =['B', 'M']

def equal(O, G):
    return O.name == G.name
def checkInArray(temp, Open):
    for x in Open:
        if equal(x, temp):
            return True
        return False
def path(O):
    print(O.name)
    if O.par != None:
        path(O.par)
    else:
        return
#BFS tìm kiếm chiều rộng
def BFS(S = Node('A'), M = Node('S')):
    Open = []
    Closed = []
    Open.append(S)
    while True:
        if len(Open) == 0:
            print('Tim kiem that bai')
            return
        O = Open.pop(0)
        Closed.append(O)
        if equal(O, M) == True:
            print('Tim kiem thanh cong')
            path(O)
            return
        for x in data [O.name]:
            tmp = Node(x)
            tmp.par = O
            ok1 = checkInArray(tmp, Open)
            ok2 = checkInArray(tmp, Closed)
            if not ok1 and not ok2:
                Open.append(tmp)
BFS(Node('A'), Node('S'))
