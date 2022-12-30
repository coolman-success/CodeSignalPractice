# Calc Final Score

You are working on a revolutionary video game. This game will consist of several levels, and on each level the player will be able to collect bonuses. For each passed level the player will thus get some score, determined by the number of collected bonuses.

Player's final score is decided by the number of completed levels and scores obtained on each of them. The final score is calculated as the sum of squares of `n` maximum scores obtained. If the number of completed levels is less than `n`, the score is calculated as the sum of squared scores for each level, and final result is divided by `5` as a penalty (the result is rounded down to the nearest integer).

Given the list of `scores` the player got for completed levels and the number `n` that determines the number of levels you have to pass to avoid being penalized, return the player's final game score.

## Example

- For `scores = [4, 2, 4, 5]` and `n = 3`,

    the output should be

    `solution(scores, n) = 57`.

    <code>5<sup>2</sup> + 4<sup>2</sup> + 4<sup>2</sup> = 57</code>.

- For `scores = [4, 2, 4, 5]` and `n = 5`,

    the output should be

    `solution(scores, n) = 12`.

    <code>(4<sup>2</sup> + 2<sup>2</sup> + 4<sup>2</sup> + 52) / 5 = 61 / 5 ≈ 12</code>.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer scores**

	A list of scores the player obtained.

	*Guaranteed constraints:*

	`0 ≤ scores.length ≤ 20`,

	`0 ≤ scores[i] ≤ 50`.

- **[input] integer n**

	The number of levels that should be completed in order not to receive a penalty.

	*Guaranteed constraints:*

	`1 ≤ n ≤ 20`.

- **[output] integer**

	The final score.
