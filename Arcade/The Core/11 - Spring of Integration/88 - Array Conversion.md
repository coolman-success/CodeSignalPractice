# Array Conversion

Given an array of <code>2<sup>k</sup></code> integers (for some integer `k`), perform the following operations until the array contains only one element:

On the <code>1<sup>st</sup></code>, <code>3<sup>rd</sup></code>, <code>5<sup>th</sup></code>, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
On the <code>2<sup>nd</sup></code>, <code>4<sup>th</sup></code>, <code>6<sup>th</sup></code>, etc. iterations replace each pair of consecutive elements with their product.
After the algorithm has finished, there will be a single element left in the array. Return that element.

## Example

For `inputArray = [1, 2, 3, 4, 5, 6, 7, 8]`, the output should be

`solution(inputArray) = 186`.

We have `[1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186]`, so the answer is `186`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer inputArray**

	*Guaranteed constraints:*

	<code>1 ≤ inputArray.length ≤ 2<sup>7</sup></code>,

	`-100 ≤ inputArray[i] ≤ 100`.

- **[output] integer**
