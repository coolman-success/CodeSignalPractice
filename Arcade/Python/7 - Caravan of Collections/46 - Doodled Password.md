# Doodled Password

Your friend has been doodling during the lecture and wrote down several digits in a circle. You're wondering if these `digits` might form the password to your friend's computer. You're planning to prank him some time in the future, and hacking into his computer will definitely help. If the `digits` written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.

Given a list of `digits` as they are written in the clockwise order, find all other combinations the password could possibly have.

## Example

For `digits = [1, 2, 3, 4, 5]`, the output should be

<pre style="white-space: pre;">
<code>solution(digits) = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                    [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
</code></pre>

Here's what your friend wrote down:

![Example](../../../assets%20(dont%20delete)/arcade-python-46.png)

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer digits**

	The list of digits your friend wrote down.

	*Guaranteed constraints:*

	`1 ≤ digits.length ≤ 20`,

	`0 ≤ digits[i] ≤ 9`.

- **[output] array.array.integer**

	All possible password combinations in the following order: first the combination starting with `digits[0]` should go, then the one starting with `digits[1]`, etc. The last combination should start with `digits[digits.length - 1]`
