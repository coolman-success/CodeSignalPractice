# Numbers Grouping

You are given an array of integers that you want distribute between several groups. The first group should contain numbers from `1` to <code>10<sup>4</sup></code>, the second should contain those from <code>10<sup>4</sup> + 1</code> to <code>2 * 10<sup>4</sup></code>, ..., the <code>100<sup>th</sup></code> one should contain numbers from <code>99 * 10<sup>4</sup> + 1</code> to <code>10<sup>6</sup></code> and so on.

All the numbers will then be written down in groups to the text file in such a way that:

- the groups go one after another;
- each non-empty group has a header which occupies one line;
- each number in a group occupies one line.

Calculate how many lines the resulting text file will have.

## Example

For `a = [20000, 239, 10001, 999999, 10000, 20566, 29999]`, the output should be

`solution(a) = 11`.

The numbers can be divided into `4` groups:

- `239` and `10000` go to the <code>1<sup>st</sup></code> group (<code>1 ... 10<sup>4</sup></code>);
- `10001` and `20000` go to the second <code>2<sup>nd</sup></code> (<code>10<sup>4</sup> + 1 ... 2 * 10<sup>4</sup></code>);
- `20566` and `29999` go to the <code>3<sup>rd</sup></code> group (<code>2 * 10<sup>4</sup> + 1 ... 3 * 10<sup>4</sup></code>);
- groups from `4` to `99` are empty;
- `999999` goes to the <code>100<sup>th</sup></code> group (<code>99 * 10<sup>4</sup> + 1 ... 10<sup>6</sup></code>).

Thus, there will be `4` groups (i.e. four headers) and `7` numbers, so the file will occupy `4 + 7 = 11` lines.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer a**

	*Guaranteed constraints:*

	<code>1 ≤ a.length ≤ 10<sup>5</sup></code>,

	<code>1 ≤ a[i] ≤ 10<sup>9</sup></code>.

- **[output] integer**

	The number of lines needed to store the grouped numbers.
