# Cho một list các số nguyên num_list và một sliding window có kích thước size k di
# chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
# đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
# lớn hơn hoặc bằng 1

def max_slide_array(num_list, size):
    max_list = []

    if size > len(num_list):
        return None
    
    for i in range(len(num_list) - size + 1):
        max_list.append(max(num_list[i:i + size]))
    
    return max_list


assert max_slide_array([3, 4, 5, 1, -44], 3) == [5, 5, 5]

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

print(max_slide_array(num_list , k)) # [5, 5, 5, 5, 10, 12, 33, 33]