In this problem you will build a new array using the numbers from an existing array. Add each number, one at a time, to the end of the new array. Then reverse the order of the numbers in the new array. Repeat this for each number added. For example, given the array [1, 2, 3, 4]. Add the first element [1] to the end of a new array and reverse it. Then add the second element [2] to the end of the new array and reverse the array. Repeat this process n times where n is the size of the array. The result is the array [4, 2, 1, 3]. Below are the detailed steps for the array [1, 2, 3, 4].

|     |  Add next element to end |  Reversed the array  |
| --- | ------------------------ | -------------------- |
|1    |   [1]                    |         [1]          |
|2    |   [1,2]                  |         [2,1]        |
|3    |   [2,1,3]                |         [3,1,2]      |
|4    |   [3,1,2,4]              |         [4,2,1,3]    |

Here is another example starting with the original array [4, 8, 6, 1, 7, 9] and ending with a result of [9, 1, 8, 4, 6, 7].

      |  Add next element to end |  Reversed the array  |
| --- |  ----------------------- | -------------------- |
| 1   |  [4]                     |     [4]              |  
| 2   |  [4,8]                   |     [8,4]            |
| 3   |  [8,4,6]                 |     [6,4,8]          |
| 4   |  [6,4,8,1]               |     [1,8,4,6]        |
| 5   |  [1,8,4,6,7]             |     [7,6,4,8,1]      |
| 6   |  [7,6,4,8,1,9]           |     [9,1,8,4,6,7]    |


Input Format

Prompt for the input as shown below. Enter an integer, N, that represents the count of numbers to follow. N will be greater than 0. Enter N integers with each integer separated by a space. Data will be entered from console. You do not need to edit the input data. Rerun your application to test each test case.

Constraints

Need to accept only one input and that input needs to be numbers seperated by a space.

Output Format

A list of integers, each separated by a space, representing the final result.

Sample Input 0

6 4 8 6 1 7 9
Sample Output 0

9 1 8 4 6 7




https://www.hackerrank.com/contests/ucsi-national-programming-competition/challenges/unpc-multi-array-reversing
