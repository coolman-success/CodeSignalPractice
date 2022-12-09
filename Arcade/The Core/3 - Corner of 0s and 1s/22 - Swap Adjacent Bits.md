# Swap Adjacent Bits

You're given an arbitrary 32-bit integer `n`. Take its binary representation, split bits into it in pairs (bit number `0` and `1`, bit number `2` and `3`, etc.) and swap bits in each pair. Then return the result as a decimal number.

## Example

- For `n = 13`, the output should be

    `solution(n) = 14`.

    <code>13<sub>10</sub> = 1101<sub>2</sub> ~> {11}{01}<sub>2</sub> ~> 1110<sub>2</sub> = 14<sub>10</sub></code>.

- For `n = 74`, the output should be

    `solution(n) = 133`.

    <code>74<sub>10</sub> = 01001010<sub>2</sub> ~> {01}{00}{10}{10}<sub>2</sub> ~> 10000101<sub>2</sub> = 133<sub>10</sub></code>.

    Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have `32` bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	Guaranteed constraints:

	<code>0 ≤ n < 2<sup>30</sup></code>.

- **[output] integer**

