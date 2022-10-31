def sum_list(nums):
    if len(nums) == 0:
        return None
    else:
        (sum_list(nums[1:]) or 0)
        return (sum_list(nums[1:]) or 0) + nums[0]


if __name__ == "__main__":
    listA = []
    listB = [3]
    listC = [1, 2, 3, 4]
    assert sum_list(listA) == None
    assert sum_list(listB) == 3
    assert sum_list(listC) == 10
    print('Everything works correctly!')
