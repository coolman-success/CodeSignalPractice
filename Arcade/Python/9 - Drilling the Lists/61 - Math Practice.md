# Math Practice

Little Billy is not too good with numbers and having trouble even multiplying and adding them. He needs some practice, and you are the one helpful fellow who can give him a list of numbers to practice on. Given a list of `numbers`, Billy should calculate the following value:

```
(((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...)
```

Unfortunately you yourself are not too good with math, but you know how to code. Implement a function that, given a list of `numbers`, will return the result of the operation `Billy` has to perform.

## Example

For `numbers = [1, 2, 3, 4, 5, 6]`, the output should be

`solution(numbers) = 71`.

Here's how the answer is obtained: `((1 + 2) * 3 + 4) * 5 + 6 = 71`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer numbers**

	A list of numbers.

	*Guaranteed constraints:*

	`2 ≤ numbers.length ≤ 20`,

	`0 ≤ numbers[i] ≤ 50`.

- **[output] integer**

	The answer Billy should obtain.
