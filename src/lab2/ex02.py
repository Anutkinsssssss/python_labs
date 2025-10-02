def unique_sorted(nums):
    otvetik = sorted(set(nums))
    return otvetik

nums = [3, 1, 2, 1, 3]
print(unique_sorted(nums))
nums = []
print(unique_sorted(nums))
nums = [-1, -1, 0, 2, 2]
print(unique_sorted(nums))
nums = [1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(nums))
