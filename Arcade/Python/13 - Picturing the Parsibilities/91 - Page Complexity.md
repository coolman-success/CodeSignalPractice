# Page Complexity

You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the complexity of the main page of your site. In order to measure the complexity of the page, you need to find a set of all tags located on the deepest level of a tree correponsing to HTML document. Given a valid HTML `document`, find all distinct tags located on the deepest level.

## Example

For

`document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"`

the output should be

`solution(document) = ["h1", "p"]`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string document**

	Correct HTML document.

	*Guaranteed constraints:*

	`10 ≤ document.length ≤ 900`.

- **[output] array.string**

	List of all distinct tags on the deepest level sorted *lexicographically*.
