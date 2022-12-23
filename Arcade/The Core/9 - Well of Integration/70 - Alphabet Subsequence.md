# Alphabet Subsequence

Check whether the given string is a subsequence of the plaintext alphabet.

`A` is considered a **subsequence** of `B` if every element from `A` appears in `B` in the same order (not necessarily contiguous; there can be other elements in between). In other words, `A` can be obtained just by deleting elements from `B`.

The **plaintext alphabet** is a string `"abcdef...xyz"`.

## Example

- For `s = "effg"`, the output should be

    `solution(s) = false`;

- For `s = "cdce"`, the output should be

    `solution(s) = false`;

- For `s = "ace"`, the output should be

    `solution(s) = true`;

- For `s = "bxz"`, the output should be

    `solution(s) = true`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string s**

	*Guaranteed constraints:*

	`2 ≤ s.length ≤ 15`.

- **[output] boolean**

	`true` if the given string is a *subsequence* of the *alphabet*, `false` otherwise.
