import numpy as np

# تابعی برای تبدیل آرایه سه‌ستونی به ماتریس کامل
def sparse_to_dense(sparse_matrix, shape):
    dense_matrix = np.zeros(shape)
    for row, col, value in sparse_matrix:
        dense_matrix[int(row), int(col)] = value
    return dense_matrix

# تابع اصلی برای ضرب دو ماتریس اسپارس و بازگشت به آرایه سه‌ستونی
def sparse_multiply(sparse_A, shape_A, sparse_B, shape_B):
    if shape_A[1] != shape_B[0]:
        return "number of columns in first matrix must equal the number of rows in second matrix"
    # تبدیل به ماتریس کامل
    dense_A = sparse_to_dense(sparse_A, shape_A)
    dense_B = sparse_to_dense(sparse_B, shape_B)
    
    # ضرب ماتریس‌ها
    dense_result = np.dot(dense_A, dense_B)
    
    # تبدیل نتیجه به آرایه سه‌ستونی
    sparse_result = []
    for i in range(dense_result.shape[0]):
        for j in range(dense_result.shape[1]):
            if dense_result[i, j] != 0:
                sparse_result.append([i, j, int(dense_result[i, j])])  # تبدیل به عدد صحیح
    
    return np.array(sparse_result)

# مثال از ورودی‌های اسپارس
sparse_A = np.array([
    [0, 0, 1],
    [0, 1, 2],
    [1, 0, 3],
    [2, 0, 4]
])
shape_A = (4, 3)

sparse_B = np.array([
    [0, 1, 1],
    [1, 0, 6],
    [2, 0, 7]
])
shape_B = (3, 3)

# ضرب ماتریس‌ها
result = sparse_multiply(sparse_A, shape_A, sparse_B, shape_B)
print("3_Column Array:")
print(result)
