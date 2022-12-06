# Second-Rightmost Zero Bit

Presented with the integer `n`, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

Return the value of <code>2<sup>position_of_the_found_bit</sup></code>.

## Example

For `n = 37`, the output should be

`solution(n) = 8`.

<code>37<sub>10</sub> = 10<span style="color:red">0</span>101<sub>2</sub></code>. The second rightmost zero bit is at position `3` (0-based) from the right in the binary representation of `n`.

Thus, the answer is <code>2<sup>3</sup> = 8</code>.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	Guaranteed constraints:

	<code>4 ≤ n ≤ 2<sup>30</sup></code>.

- **[output] intege**

