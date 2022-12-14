# Super Prize

In a large and famous supermarket a new major campaign was launched. From now on, each <code>n<sup>th</sup></code> customer has a chance to win a prize: a brand new luxury car! However, it's not that simple. A customer wins a prize only if the total price of their purchase is divisible by `d`. This number is kept as a secret, so the customers don't know in advance how much they should spend on their purchases. The winners will be announced once the campaign is over.

Your task is to implement a function that will determine the winners. Given the `purchases` of some customers over time, return the 1-based indices of all the customers who won the prize, i.e. each <code>n<sup>th</sup></code> who spend on their purchases amount of money divisible by `d`.

## Example

For `purchases = [12, 43, 13, 465, 1, 13]`, `n = 2`, and `d = 3`,

the output should be

`solution(purchases, n, d) = [4]`.

Each second customer has a chance to win a car, which makes customers `2`, `4` and `6` potential winners. Customer number `2` spent `43` on his purchase, which is not divisible by `3`. `13` also is not divisible by `3`, so the sixth customer also doesn't get the price. Customer `4`, however, spent `465`, which is divisible by `3`, so he is the only lucky guy.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer purchases**

	A list that represents the cost of the purchases some customers made.

	*Guaranteed constraints:*

	`0 ≤ purchases.length ≤ 100`,

	`1 ≤ purchases[i] ≤ 1000`.

- **[input] integer n**

	*Guaranteed constraints:*

	`2 ≤ n ≤ 20`.

- **[input] integer d**

	*Guaranteed constraints:*

	`2 ≤ d ≤ 20`.

- **[output] array.integer**

	A sorted list of 1-based customers who won the prize.
