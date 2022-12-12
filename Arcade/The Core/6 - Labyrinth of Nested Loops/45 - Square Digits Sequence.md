# Square Digits Sequence

Consider a sequence of numbers <code>a<sub>0</sub></code>, <code>a<sub>1</sub></code>, ..., <code>a<sub>n</sub></code>, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

Given the first element `a0`, find the length of the sequence.

## Example

- For `a0 = 16`, the output should be

    `solution(a0) = 9`.

    Here's how elements of the sequence are constructed:

    - <code>a<sub>0</sub> = 16</code>
    - <code>a<sub>1</sub> = 1<sup>2</sup> + 6<sup>2</sup> = 37</code>
    - <code>a<sub>2</sub> = 3<sup>2</sup> + 7<sup>2</sup> = 58</code>
    - <code>a<sub>3</sub> = 5<sup>2</sup> + 8<sup>2</sup> = 89</code>
    - <code>a<sub>4</sub> = 8<sup>2</sup> + 9<sup>2</sup> = 145</code>
    - <code>a<sub>5</sub> = 1<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup> = 42</code>
    - <code>a<sub>6</sub> = 4<sup>2</sup> + 2<sup>2</sup> = 20</code>
    - <code>a<sub>7</sub> = 2<sup>2</sup> + 0<sup>2</sup> = 4</code>
    - <code>a<sub>8</sub> = 4<sup>2</sup> = 16</code>, which has already occurred before (<code>a<sub>0</sub></code>)
    
    Thus, there are `9` elements in the sequence.

- For `a0 = 103`, the output should be

    `solution(a0) = 4`.

    The sequence goes as follows: `103 -> 10 -> 1 -> 1`, `4` elements altogether.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer a0**

	First element of a sequence, positive integer.

	*Guaranteed constraints:*

	<code>1 ≤ a0 ≤ 10<sup>5</sup></code>.

- **[output] integer**

