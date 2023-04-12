# Hard Programming Interview Challenge: Maximum Sum of Non-Adjacent Numbers

## Problem Statement

Given a list of positive integers, find the maximum sum you can achieve by adding non-adjacent numbers from the list. The non-adjacent numbers are those, which have at least one other number between them in the list. You cannot modify the order of numbers in the list.

Write a function `max_sum_non_adjacent` to solve this problem:

```python
def max_sum_non_adjacent(numbers: List[int]) -> int:
    pass
```

### Input

- A list of integers `numbers` (1 ≤ len(numbers) ≤ 10^5) containing positive integers.

### Output

- Return an integer, which represents the maximum sum of non-adjacent numbers in the given list.

### Examples:

- The function `max_sum_non_adjacent([1, 2, 3, 4, 5, 6, 7])` should return 16.
- The function `max_sum_non_adjacent([3, 2, 7, 10])` should return 13.
- The function `max_sum_non_adjacent([3, 2, 5, 10, 7])` should return 15.

### Note

In the first example, [1, 3, 5, 7] and [2, 4, 6] are non-adjacent subsequences. The first one has the maximum sum of 16.

In the second example, [3, 10] is a non-adjacent subsequence and has the maximum sum of 13.

In the third example, [3, 5, 7] is a non-adjacent subsequence and has the maximum sum of 15.

### Testing

To test your solution, create a Python file `solution.py` and implement the `max_sum_non_adjacent` function. Then, run the provided test file `test_hard_challenge.py` to verify your solution.