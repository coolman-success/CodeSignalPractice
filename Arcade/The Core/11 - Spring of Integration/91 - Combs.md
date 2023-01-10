# Combs

Miss X has only two solution in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the solution. The only way they fit is horizontally and without overlapping. Given teeth' positions on both solution, find the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.

It is also guaranteed that the total length of two strings is smaller than `32`.

Note, that the solution can **not** be rotated/reversed.

## Example

For `comb1 = "*..*"` and comb2 = `"*.*"`, the output should be

`solution(comb1, comb2) = 5`.

Although it is possible to place the solution like on the first picture, the best way to do this is either picture 2 or picture 3.

![Example](../../../assets%20(dont%20delete)/arcade-the_core-91.png)

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string comb1**

	A comb is represented as a string. If there is an asterisk (`'*'`) in the <code>i<sup>th</sup></code> position, there is a tooth there. Otherwise there is a dot (`'.'`), which means there is a missing tooth on the comb.

	*Guaranteed constraints:*

	`3 ≤ comb1.length ≤ 8`.

- **[input] string comb2**

	The second comb is represented in the same way as the first one.

	*Guaranteed constraints:*

	`1 ≤ comb2.length ≤ 5`.

- **[output] integer**

	The minimum length of a purse Miss X needs.
