# Pref Sum

There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of *prefix sums*. Given array `a`, your task is to calculate all its prefix sums.

Array of **prefix sums** is defined as:

```
  B[0] = A[0]
  B[1] = A[0] + A[1]
  B[2] = A[0] + A[1] + A[2]
  ...
  B[n - 1] = A[0] + A[1] + ... + A[n - 1]
```

## Example

For `a = [1, 2, 3]`, the output should be

`solution(a) = [1, 3, 6]`.

Here's how the *prefix sums* can be calculated: `[1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer a**

	*Guaranteed constraints:*

	<code>2 ≤ a.length ≤ 3 · 10<sup>4</sup></code>,

	`-1000 ≤ a[i] ≤ 1000`.

- **[output] array.integer**
