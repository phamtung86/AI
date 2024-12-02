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
data['N'] =['S']
data['K'] =['P','Z']
data['S'] =['T', 'C']
data['P'] =['B']
data['Z'] =['M']

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
#DFS tìm kiếm chiều sâu
def DFS(S = Node('A'), M = Node('T')):
    Open = []
    Closed = []
    Open.append(S)
    while True:
        if len(Open) == 0:
            print("Tim kiem that bai")
            return
        O = Open.pop(0)
        Closed.append(O)
        if equal(O, M) == True:
            print('Tim kiem thanh cong')
            path(O)
            return
        pos = 0
        for x in data [O.name]:
            tmp = Node(x)
            tmp.par = O
            ok1 = checkInArray(tmp, Open)
            ok2 = checkInArray(tmp, Closed)
            if not ok1 and not ok2:
                Open.insert(pos, tmp)
                pos = pos + 1;
DFS(Node ('A'), Node('T'))