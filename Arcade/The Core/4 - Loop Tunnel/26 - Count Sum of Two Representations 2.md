# Count Sum of Two Representations 2

Given integers `n`, `l` and `r`, find the number of ways to represent `n` as a sum of two integers `A` and `B` such that `l ≤ A ≤ B ≤ r`.

## Example

For `n = 6`, `l = 2`, and `r = 4`, the output should be

`solution(n, l, r) = 2`.

There are just two ways to write `6` as `A + B`, where `2 ≤ A ≤ B ≤ 4`: `6 = 2 + 4` and `6 = 3 + 3`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	A positive integer.

	Guaranteed constraints:

	<code>5 ≤ n ≤ 10<sup>9</sup></code>.

- **[input] integer l**

	A positive integer.

	Guaranteed constraints:

	`1 ≤ l ≤ r`.

- **[input] integer r**

	A positive integer.

	Guaranteed constraints:

	<code>l ≤ r ≤ 10<sup>9</sup></code>,

	<code>r - l ≤ 10<sup>6</sup></code>.

- **[output] intege**

