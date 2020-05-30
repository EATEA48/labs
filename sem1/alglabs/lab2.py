from random import randint


def insertion_sort(nums):
    n = 0
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        n += 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

lists = [2, 0, 11, 4, 23, 1, 3, 41, 23, 5, 24, 54, 76, 14, 99]
print(lists)
n = 0
insertion_sort(lists)
print(lists)
for i in range(len(lists)):
    n += 1
    if n == 5:
        lists.insert(5, 0)
    elif n == 10:
        lists.insert(11, 0)
    elif  n == 15:
        lists.insert(17, 0)
print(lists)

