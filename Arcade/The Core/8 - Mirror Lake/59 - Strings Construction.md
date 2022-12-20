# Strings Construction

Given two strings `a` and `b`, both consisting only of lowercase English letters, your task is to calculate how many strings equal to `a` can be constructed using only letters from the string `b`? Each letter can be used only once and in one string only.

## Example

- For `a = "abc"` and `b = "abccba"`, the output should be `solution(a, b) = 2`.

    We can construct `2` strings `a = "abc"` using only letters from the string `b`.

- For `a = "ab"` and `b = "abcbcb"`, the output should be `solution(a, b) = 1`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string a**

	String to construct, containing only lowercase English letters.

	*Guaranteed constraints:*

	<code>1 ≤ a.length ≤ 10<sup>5</sup></code>.

- **[input] string b**

	String containing needed letters, containing only lowercase English letters.

	*Guaranteed constraints:*

	<code>1 ≤ b.length ≤ 10<sup>5</sup></code>.

- **[output] integer**

	The number of strings `a` that can be constructed from the string `b`.
