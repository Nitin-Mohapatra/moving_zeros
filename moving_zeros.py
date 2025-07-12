start = 0
for idx in range(len(nums)):
    if nums[idx] != 0:
        nums[start] = nums[idx]
        start += 1  # ✅ Move pointer forward when non-zero is added

while start < len(nums):
    nums[start] = 0
    start += 1  # ✅ Fill remaining with zeroes
