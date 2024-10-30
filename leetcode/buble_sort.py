def bubble(nums):
    size = len(nums)
    for _ in nums:
        print(nums)
        is_sorted = True
        for i in range(size-1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                # inverte
                nums[i+1], nums[i] = nums[i], nums[i+1]
        if is_sorted:
            return nums
    return nums
bubble([1, 2, 3, 4, 5])
bubble([5, 1, 3, 4, 1])