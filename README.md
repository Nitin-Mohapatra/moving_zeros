# 🧼 Move Zeroes to End (Python)

This Python script moves all zeroes in a list to the end while maintaining the relative order of the non-zero elements. The operation is done **in-place**, with no additional memory used.

---

## 📘 Problem Statement

Given an array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

You **must do this in-place** without making a copy of the array.

---

## 🧠 Approach

- Use a **two-pointer technique**:
  - `start`: points to the next position to place a non-zero value.
  - `idx`: iterates through the list.
- In the first pass:
  - For every non-zero element, place it at the `start` index and increment `start`.
- In the second pass:
  - Fill the rest of the array from `start` to end with zeroes.

This ensures that non-zero elements are kept in their original order, and all zeroes are moved to the back.

---

## 🧾 Python Code

```python
nums = [0, 1, 0, 3, 12]

start = 0
for idx in range(len(nums)):
    if nums[idx] != 0:
        nums[start] = nums[idx]
        start += 1  # ✅ Move pointer forward when non-zero is added

while start < len(nums):
    nums[start] = 0
    start += 1  # ✅ Fill remaining with zeroes

print(nums)  # Output: [1, 3, 12, 0, 0]
