# Group Dating

You're organizing a group dating activity for cats, i.e. a meeting where an equal number of `male` and `female` cats get together. For each cat you calculate their *nature value*, an integer that describes the cat's spirit. When a male and a female cat with the same *nature value* see each other, they become connected and happily walk out together.

You've just started another group dating, and placed the cats in front of one another so that the <code>i<sup>th</sup></code> male is sitting across the <code>i<sup>th</sup></code> female. What cats will remain at their places, assuming that the pairs of cats sitting in front of each other and having the same *nature values* will walk out?

## Example

For `male = [5, 28, 14, 99, 17]` and `female = [5, 14, 28, 99, 16]`,

the output should be

`solution(male, female) = [[28, 14, 17], [14, 28, 16]]`.

Pairs of cats at positions `0` and `3` (0-based) have the same *nature values*, so they will leave the meeting.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer male**

	*Nature values* of male cats.

	*Guaranteed constraints:*

	`1 ≤ male.length ≤ 20`,

	`0 ≤ male[i] ≤ 100`.

- **[input] array.integer female**

	*Nature values* of female cats.

	*Guaranteed constraints:*

	`female.length = male.length`,

	`0 ≤ female[i] ≤ 100`.

- **[output] array.array.integer**

	A list of two elements, where the first element will contain *nature values* of the remaining male cats, and the second element will contain *nature values* of the remaining female cats. In both cases, the values should go in the order the corresponding cats are sitting.

	*Note*: if your solution returns a list of tuples, the tuples will be converted to list automatically.
