# Medium Programming Interview Challenge - Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to target.

You may assume that each input would have _exactly_ one solution, and you may not use the same element twice. You can return the answer in any order.

### Examples

#### Example 1
```python
nums: List[int] = [2, 7, 11, 15]
target: int = 9

find_two_sum(nums, target)
```

Output: [0, 1]

**Explanation:** Because nums[0] + nums[1] == 9 (2 + 7 == 9), we return [0, 1].

#### Example 2
```python
nums: List[int] = [3, 2, 4]
target: int = 6

find_two_sum(nums, target)
```

Output: [1, 2]

**Explanation:** Because nums[1] + nums[2] == 6 (2 + 4 == 6), we return [1, 2].

#### Example 3
```python
nums: List[int] = [3, 3]
target: int = 6

find_two_sum(nums, target)
```

Output: [0, 1]

**Explanation:** Because nums[0] + nums[1] == 6 (3 + 3 == 6), we return [0, 1].

### Constraints

- 2 <= nums.length <= 10^3
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.