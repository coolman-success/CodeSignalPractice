# Multiplication Table

Looks like your little brother doesn't want to remember the multiplication table! Instead he wants to play videogames all day long. To teach him a lesson you'd like to write a virus that will pop up in the middle of the game and disappear only when the brother correctly solves several math questions.

To begin with, you need to construct a multiplication table. Given an integer `n`, return the multiplication table of size `n × n`.

## Example

For `n = 5`, the output should be

```
solution(n) = [[1, 2,  3,  4,  5 ], 
                [2, 4,  6,  8,  10], 
                [3, 6,  9,  12, 15], 
                [4, 8,  12, 16, 20], 
                [5, 10, 15, 20, 25]]
```

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	The size of the multiplication table.

	*Guaranteed constraints:*

	`2 ≤ n ≤ 30`.

- **[output] array.array.integer**

	Multiplication table of size `n × n`, i.e. a square matrix that has value `i * j` at the intersection of the <code>i<sup>th</sup></code> row and the <code>j<sup>th</sup></code> column (both 1-based).
