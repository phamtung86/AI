def dot_product(weights, inputs):
    """Tính tích vô hướng giữa weights và inputs."""
    return sum(w * x for w, x in zip(weights, inputs))


def update_weights(weights, inputs, error, learning_rate):
    """Cập nhật trọng số dựa trên lỗi và tỷ lệ học."""
    return [w + learning_rate * error * x for w, x in zip(weights, inputs)]


def activation_function(value):
    """Hàm kích hoạt: trả về 1 nếu giá trị >= 0, ngược lại trả về 0."""
    return 1 if value >= 0 else 0


# Dữ liệu huấn luyện
data = [
    {"features": [1, 2, 3], "label": 0},
    {"features": [9, 8, 9], "label": 1},
    {"features": [3, 4, 1], "label": 0},
    {"features": [8, 7, 6], "label": 1}
]

# Dữ liệu kiểm tra
X_test = [2, 4, 2]

# Khởi tạo trọng số và bias
weights = [0, 0, 0]
bias = 0
learning_rate = 0.1
epochs = 1000

# Huấn luyện mô hình
for epoch in range(epochs):
    total_error = 0
    for sample in data:
        inputs = sample["features"]
        target = sample["label"]

        # Tính toán đầu ra
        output = activation_function(dot_product(weights, inputs) + bias)

        # Tính toán lỗi
        error = target - output
        total_error += abs(error)

        # Cập nhật trọng số và bias
        weights = update_weights(weights, inputs, error, learning_rate)
        bias += learning_rate * error

    # Nếu không còn lỗi, dừng huấn luyện
    if total_error == 0:
        break

# Dự đoán cho dữ liệu kiểm tra
prediction = activation_function(dot_product(weights, X_test) + bias)
print(f"Dự đoán cho X {X_test}: {prediction}")