def min_max(nums):
    if len(nums) == 0:
        raise ValueError
    minimumchik = min(nums)
    maxichek = max(nums)
    return (minimumchik, maxichek)


nums = [3, -1, 5, 5, 0]
print(min_max(nums))
