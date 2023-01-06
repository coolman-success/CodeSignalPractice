# Url Similarity

You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.

For that, you've thought of the special algorithm that for two URLs `url1` and `url2` computes their similarity as following:

1. Initially their similarity is `0`
2. Then, it is increased by the following rules:
- `+5`, if the same protocol is used in both URLs.
- `+10`, if `url1` and `url2` have the same address.
- `+k`, if the *first* `k` components of `path` (delimited by `/`) are exactly the same (and in the same order) between the two URLs.
- `+1` if for each `varNames` common between them. Additional `+1` if the respective values are equal too.

URLs are given in the following format: `protocol://address[(/path)*][?query]` (where `query = varName=value(&varName=value)*`, parts given in `[]` are optional, and parts in `()*` may be repeated several times). Each of the named elements (i.e. `protocol`, `address`, `path`, `varName` and `value`) are guaranteed to contain only alphanumeric characters and periods.

Given the two URLs `url1` and `url2`, compute their similarity using the algorithm described above.

## Example

For
<pre style="white-space:pre;">
<code>url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"</code></pre>

and

<pre style="white-space:pre;">
<code>url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"</code></pre>

the output should be

`solution(url1, url2) = 19`.

Because these URLs have the same protocols, addresses, first path component (`home`) and two `varNames`, with one also having the same value in both of them.
So the resulting similarity is thus `5 + 10 + 1 + 1 + 1 + 1 = 19`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] string url1**

	First URL. It can only contain lowercase English letters, digits and characters `'.'`, `'/'`, `':'`, `'?'`, `'&'` and `'='`.

	It's guaranteed that each `varName` is unique.

	*Guaranteed constraints:*

	`5 ≤ url1.length ≤ 100`.

- **[input] string url2**

	Second URL with the same format as `url1`.

	*Guaranteed constraints:*

	`5 ≤ url2.length ≤ 100`.

- **[output] integer**

	The computed similarity.
