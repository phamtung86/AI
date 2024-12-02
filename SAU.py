class Node:
    def __init__(self, ten, cha=None):
        self.ten = ten
        self.cha = cha

    def display(self):
        print(self.ten)


from collections import defaultdict

# Dữ liệu đồ thị
data = defaultdict(list)

data['A'] = ['D', 'N', 'K']
data['D'] = ['G']
data['N'] = ['S', 'P']
data['K'] = ['Z']
data['S'] = ['T', 'C']
data['Z'] = ['B', 'M']


def KiemTra(tam, O):
    """Kiểm tra xem nút đã được khám phá hay chưa."""
    for v in O:
        if v.ten == tam.ten:
            return True
    return False


def DuongDi(n):
    """In ra đường đi từ nút hiện tại về nút gốc."""
    if n is not None:
        DuongDi(n.cha)
        print(n.ten)


def DFS(To, Tg):
    """Tìm kiếm theo chiều sâu từ To đến Tg."""
    MO = []  # Ngăn xếp
    Dong = []  # Danh sách đã duyệt
    MO.append(To)  # Thêm nút bắt đầu vào ngăn xếp

    while len(MO) > 0:
        n = MO.pop()  # Lấy nút cuối cùng từ ngăn xếp

        if n.ten == Tg.ten:
            print("Tìm kiếm thành công")
            DuongDi(n)  # In ra đường đi
            return

        Dong.append(n)  # Đánh dấu nút là đã duyệt
        for v in data[n.ten]:
            tam = Node(v)
            if not KiemTra(tam, MO) and not KiemTra(tam, Dong):
                MO.append(tam)  # Thêm nút kề vào ngăn xếp
                tam.cha = n  # Gán nút cha

    print("Tìm kiếm không thành công")  # Nếu không tìm thấy


# Gọi hàm DFS để tìm kiếm từ 'A' đến 'B'
DFS(Node('A'), Node('B'))