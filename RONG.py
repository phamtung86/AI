class Node:
    def __init__(sefl,ten,cha = None):
        sefl.ten = ten
        sefl.cha = cha
    def display(sefl):
        print(sefl.ten)
        
from collections import defaultdict
data = defaultdict(list)
data = defaultdict(list)
data['A'] = ['D', 'N', 'K']
data['D'] = ['G']
data['N'] = ['S', 'P']
data['K'] = ['Z']
data['S'] = ['T', 'C']
data['Z'] = ['B', 'M']

def kiemTra(tam,O):
    for v in O:
        if v.ten == tam.ten:
            return True
        return False

def DuongDi(n):
    if n is not None:
        DuongDi(n.cha)
        print(n.ten)

def BFS(To,Tg):
    MO = []
    DONG = []
    MO.append(To)
    while True:
        if len(MO) == 0:
            print("Tim kiem khong thanh cong")
            return
        n = MO.pop(0)
        if n.ten == Tg.ten:
            print("Tim kiem thanh cong")
            DuongDi(n)
            return
        DONG.append(n)
        for v in data[n.ten]:
            tam = Node(v)
            ok1 = kiemTra(tam,MO)
            ok2 = kiemTra(tam,DONG)
            if not ok1 and not ok2:
                MO.append(tam)
                tam.cha = n
BFS(Node('A'),Node('B'))
                
        