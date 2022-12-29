# Correct Lineup

For the opening ceremony of an upcoming sports event, an even number of athletes from two teams A and B were picked to put on a performance. They start by forming a correct lineup in which an athlete from one team stands next to an athlete from the other team (i.e., in an alternating pattern). As a part of the performance, adjacent pairs of athletes (i.e. the first one together with the second one, the third one together with the fourth one, etc.) have to swap positions with each other.

Given a list of `athletes`, return the list of `athletes` after the changes, i.e. after each adjacent pair of athletes is swapped.

## Example

For `athletes = [1, 2, 3, 4, 5, 6]`, the output should be

`solution(athletes) = [2, 1, 4, 3, 6, 5]`.

## Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[input] array.integer athletes**

	A list of even length representing the athletes, where each athlete is given by the number written on their back.

	*Guaranteed constraints:*

	`2 ≤ athletes.length ≤ 20`,

	`1 ≤ athletes[i] ≤ 100`.

- **[output] array.integer**

	Array of `athletes` with each pair of adjacent elements swapped.
