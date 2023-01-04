# Sort Codesginal Users

At CodeSignal the users can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.

Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of `users`.

## Example

For

```
users = [["warrior", "1", "1050"],
         ["Ninja!",  "21", "995"],
         ["recruit", "3", "995"]]
```

the output should be

`solution(users) = ["warrior", "recruit", "Ninja!"]`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.array.string users**

	A list of CodeSignal users, where each user is given in the format <code>[<i>username</i>, <i>id</i>, <i>xp</i>]</code>.

	It is guaranteed that all usernames and ids are unique.

	*Guaranteed constraints:*

	<code>0 ≤ users.length ≤ 10<sup>4</sup></code>,

	`users[i].length = 3`,

	`1 ≤ users[i][0].length ≤ 20`,

	<code>1 ≤ int(users[i][1]), int(users[i][2]) ≤ 10<sup>4</sup></code>.

- **[output] array.string**

	A list of CodeSignal users sorted as described above.
