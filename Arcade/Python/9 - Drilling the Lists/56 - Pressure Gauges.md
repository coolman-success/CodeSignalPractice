# Pressure Gauges

Harry dropped out of school to pursue his dreams and work in Pipes Corporations. He is now in charge of a lot of pipes, and his task is to check the gauges twice a day. By analyzing the `morning` and `evening` pressures of each pipe, Harry should write a report about the minimum and the maximum pressure during the day.

Given the pressures Harry wrote down for each pipe, return two lists: the first one containing the minimum, and the second one containing the maximum pressure of each pipe during the day.

## Example

For `morning = [3, 5, 2, 6]` and `evening = [1, 6, 6, 6]`,

the output should be

`solution(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]]`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer morning**

	A list of pressures, where the <code>i<sup>th</sup></code> element is the value the pressure gauge showed for the <code>i<sup>th</sup></code> pipe in the morning.

	*Guaranteed constraints:*

	`1 ≤ morning.length ≤ 10`,

	`0 ≤ morning[i] ≤ 1000`.

- **[input] array.integer evening**

	A list of evening pressures in the same format as `morning`.

	*Guaranteed constraints:*

	`evening.length = morning.length`,

	`0 ≤ evening[i] ≤ 1000`.

- **[output] array.array.integer**

	A list containing two lists, where the <code>i<sup>th</sup></code> elements of the first and the second lists are the minimum and the maximum pressures the <code>i<sup>th</sup></code> pipe had, respectively.
