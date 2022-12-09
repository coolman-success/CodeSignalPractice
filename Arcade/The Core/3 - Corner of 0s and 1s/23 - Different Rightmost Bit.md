# Different Rightmost Bit

You're given two integers, `n` and `m`. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.

Return the value of <code>2<sup>position_of_the_found_bit</sup></code> (0-based).

## Example

- For `n = 11` and `m = 13`, the output should be

    `solution(n, m) = 2`.

    <code>11<sub>10</sub> = 10<span style="color:red">1</span>1<sub>2</sub></code>, <code>13<sub>10</sub> = 11<span style="color:red">0</span>1<sub>2</sub></code>, the rightmost bit in which they differ is the bit at position `1` (0-based) from the right in the binary representations.

    So the answer is <code>2<sup>1</sup> = 2</code>.

- For `n = 7` and `m = 23`, the output should be

    `solution(n, m) = 16`.

    <code>7<sub>10</sub> = 111<sub>2</sub></code>, <code>23<sub>10</sub> = 10111<sub>2</sub></code>, i.e.

    ```
    00111
    10111
    ```

    So the answer is <code>2<sup>4</sup> = 16</code>.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	Guaranteed constraints:

	<code>0 ≤ n ≤ 2<sup>30</sup></code>.

- **[input] integer m**

	Guaranteed constraints:

	<code>0 ≤ m ≤ 2<sup>30</sup><code>,

	`n ≠ m`.

- **[output] integer**

