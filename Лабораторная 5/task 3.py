from random import sample
def get_unique_list_numbers() -> list[int]:
    list1=sample(range(-10,10),15)
    return list1

    ...  # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
