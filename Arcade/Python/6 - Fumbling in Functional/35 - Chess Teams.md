# Chess Teams

A grand Team Chess Tournament will be held at your University. Two teams, `smarties` and `cleveries`, will clash to determine whose chess skills are better. The teams have the same number of members, and the <code>i<sup>th</sup></code> member of `smarties` will play against the <code>i<sup>th</sup></code> member of `cleveries` in the <code>i<sup>th</sup></code> game for each valid `i`

Given the names of the players of both `smarties` and `cleveries`, return the games in the order they will be played.

## Example

For `smarties = ["Jane", "Bob", "Peter"]` and `cleveries = ["Oscar", "Lidia", "Ann"]`, the output should be
```
solution(smarties, cleveries) = [["Jane",  "Oscar"],
                                   ["Bob",   "Lidia"],
                                   ["Peter", "Ann"]]
```

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.string smarties**

	Array of strings, where each string is the name of the member of `smarties`.

	*Guaranteed constraints:*

	`0 ≤ smarties.length ≤ 10`,

	`2 ≤ smarties[i].length ≤ 10`.

- **[input] array.string cleveries**

	Members of `cleveries` in the same format as `smarties`.

	*Guaranteed constraints:*

	`cleveries.length = smarties.length`,

	`2 ≤ cleveries[i].length ≤ 10`.

- **[output] array.array.string**

	The games in the following format: <code>[game<sub>0</sub>, game<sub>1</sub>, ..., game<sub>smarties.length - 1</sub>]</code> where <code>game<sub>i</sub> = [smarty<sub>i</sub>, clevery<sub>i</sub>]</code>.
