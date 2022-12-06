# Equal Pair of Bits

You're given two integers, `n` and `m`. Find position of the rightmost pair of equal bits in their binary representations (it is guaranteed that such a pair exists), counting from right to left.

Return the value of <code>2<sup>position_of_the_found_pair</sup></code> (0-based).

## Example

For `n = 10` and `m = 11`, the output should be

`solution(n, m) = 2`.

<code>10<sub>10</sub> = 10<span style="color:red">1</span>0<sub>2</sub></code>, <code>11<sub>10</sub> = 10<span style="color:red">1</span>1<sub>2</sub></code>, the position of the rightmost pair of equal bits is the bit at position `1` (0-based) from the right in the binary representations.

So the answer is <code>2<sup>1</sup> = 2</code>.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	Guaranteed constraints:

	<code>0 ≤ n ≤ 2<sup>30</sup></code>.

- **[input] integer m**

	Guaranteed constraints:

	<code>0 ≤ m ≤ 2<sup>30</sup></code>.

- **[output] intege**

