function solution(inputString) {
  let reverseString = inputString.split("").reverse().join("");
  return inputString == reverseString;
}
