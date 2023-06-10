# Easy Programming Interview Challenge

## Problem Statement

You are given an array of integers. Return the length of the longest sequence of increasing integers in the array.

## Example

Input: `[1, 3, 5, 4, 7]`

Output: `3`

Explanation: The longest increasing subsequence is `[1, 3, 5]`.

## Function Signature

```
def longest_increasing_subsequence(arr: List[int]) -> int:
```

## Constraints

* The array will have a length from 1 to 10^4.
* The integers in the array will be in the range [-10^4, 10^4].

## Note

The solution should have a time complexity not more than O(n log n), where n is the length of the input array.