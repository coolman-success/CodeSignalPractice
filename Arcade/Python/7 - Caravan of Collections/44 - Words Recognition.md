# Words Recognition

You are working on an AI that can recognize words. To begin with, you'd like to try the following approach: for the given pair of words the AI should find two strings of sorted letters that uniquely identify these words.

Given words `word1` and `word2`, return an array of two strings sorted lexicographically, where the first string contains characters present only in `word1`, and the second string contains characters present only in `word2`.

## Example

For `word1 = "program"` and `word2 = "develop"`,

the output should be

`solution(word1, word2) = ["agmr", "delv"]`.

Letters `'o'` and `'p'` are present in both words, and other letters identify them uniquely.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string word1**

	The first word consisting of lowercase English letters.

	*Guaranteed constraints:*

	`1 ≤ word1.length ≤ 20`.

- **[input] string word2**

	The second word consisting of lowercase English letters.

	*Guaranteed constraints:*

	`1 ≤ word2.length ≤ 20`.

- **[output] array.string**

	Array of two strings sorted *lexicographically*, where the first string uniquely identifies the first word, and the second string uniquely identifies the second word.
