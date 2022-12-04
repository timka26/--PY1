def delete(list_, index=None):
    if index==0:
        return list_[1:]
    elif index is None:
        return list_[:-1]
    else:
        return list_[:index] + list_[index+1:]
print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
