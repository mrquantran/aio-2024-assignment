def levenshtein_distance(source, target):
    # Bước 1: Khởi tạo ma trận D với kích thước (len(source) + 1) x (len(target) + 1)
    M, N = len(source) + 1, len(target) + 1
    D = [[0] * N for _ in range(M)]

    # Bước 2: Hoàn thiện hàng và cột đầu tiên
    for i in range(M):
        D[i][0] = i  # Xoá các ký tự trong source để thành chuỗi rỗng
    for j in range(N):
        D[0][j] = j  # Thêm các ký tự trong target từ chuỗi rỗng

    # Bước 3: Tính toán các giá trị cho các ô còn lại
    for i in range(1, M):
        for j in range(1, N):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            D[i][j] = min(
                D[i - 1][j] + 1,     # Xoá một ký tự từ source
                D[i][j - 1] + 1,     # Thêm một ký tự vào target
                D[i - 1][j - 1] + cost  # Thay thế ký tự
            )

    # Bước 4: Trả về khoảng cách Levenshtein từ D[M-1][N-1]
    return D[-1][-1]


assert levenshtein_distance("hi", "hello") == 4.0

print(levenshtein_distance("hola", "hello")) # 3.0
