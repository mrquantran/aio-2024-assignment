"""
Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện.
• Input: Đường dẫn đến file txt
• Output: dictionary đếm số lần các từ xuất hiện
• Note:
– Giả sử các từ trong file txt đều có các chữ cái thuộc [a-z] hoặc [A-Z]
– Không cần các thao tác xử lý string phức tạp nhưng cần xử lý các từ đều là viết
thường
– Các bạn dùng lệnh này để download
!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
"""

from pathlib import Path

def word_count(file_path):
    count_dict = {}

    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()

            for word in words:
                word = word.lower()

                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1

    return count_dict


file_path = Path(__file__).parent / "p1_data.txt"
result = word_count(file_path)

assert result["who"] == 3

print(result['man']) # 6
