"""
Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
- Input: một từ
- Output: dictionary đếm số lần các chữ xuất hiện
- Note: Giả sử các từ nhập vào đều có các chữ cái thuộc[a-z] hoặc[A-Z]
"""

def character_count(word):
    count_dict = {}

    for char in word:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    return count_dict


assert character_count("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
print(character_count ("smiles")) # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}