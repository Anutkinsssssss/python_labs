def flatten(nums):
    otvetik = []
    for e in nums:
        if type(e) == list or type(e) == tuple:
            for i in range(len(e)):
                if e[i] != '':
                    otvetik.append(e[i])
        else:
            raise TypeError
    return otvetik

nums = [[1, 2], [3, 4]]
print(flatten(nums))
nums = [[1, 2], (3, 4, 5)]
print(flatten(nums))
nums = [[1], [], [2, 3]]
print(flatten(nums))
nums = [[1, 2], "ab"]
print(flatten(nums))