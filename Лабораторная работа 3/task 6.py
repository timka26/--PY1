list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0
for i in range(len(list_numbers)):
    max_number = list_numbers[max_index]
    current_number = list_numbers[i]
    if current_number >= max_number:
        max_index = i
list_numbers [-1], list_numbers [max_index] = list_numbers [max_index], list_numbers [-1]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
