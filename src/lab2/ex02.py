def unique_sorted(nums):
    otvetik = sorted(set(nums))
    return otvetik

nums = [3, 1, 2, 1, 3]
print(unique_sorted(nums))
