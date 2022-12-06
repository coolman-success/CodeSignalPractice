# Kill K-th Bit

In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number `n` the <code>k<sup>th</sup></code> bit from the right was initially set to `0`, but its current value might be different. It's now up to you to write a function that will change the <code>k<sup>th</sup></code> bit of `n` back to `0`.

## Example

- For `n = 37` and `k = 3`, the output should be

    `solution(n, k) = 33`.

    <code>3710 = 1001<span style="color:red">0</span>1<sub>2</sub> ~> 1000<span style="color:red">0</span>1<sub>2</sub> = 33<sub>10</sub></code>.

- For `n = 37` and `k = 4`, the output should be

    `solution(n, k) = 37`.

    The <code>4<sup>th</sup></code> bit is `0` already (looks like the Mad Coder forgot to encrypt this number), so the answer is still `37`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] integer n**

	Guaranteed constraints:

	<code>0 ≤ n ≤ 2<sup>31</sup> - 1</code>.

- **[input] integer k**

	The 1-based index of the changed bit (counting from the right).

	Guaranteed constraints:

	`1 ≤ k ≤ 31`.

- **[output] intege**

