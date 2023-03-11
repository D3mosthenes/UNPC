In this problem you will generate a lucky number by manipulating a list of odd numbers. The user will enter a number (n) indicating the number of “passes” through the list. The first pass is to generate a list of positive odd integers. The list will be composed of the first 10,000 odd numbers. On the second pass, eliminate every third number from the list. This is because 3 is the 2nd number in the original list and this is the 2nd pass. On the third pass, eliminate every 7th number in the revised list. This is because 7 is the 3rd number in the revised list and this is the 3rd pass. If the user entered 4 for n, then the next pass is to display the 4th number in the revised list. The fourth number will be 9. This is the lucky number for a user entered value of 4.

For example: Original list (pass one): 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 … 19999

Revised list (pass two) after eliminating every 3rd number (which was the 2nd number in the list above) 1 3 7 9 13 15 19 21 25 27 31 33 37 39 43 45 49 51 55 57 … (5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65 … were eliminated)

Revised list (pass three) after eliminating every 7th number (which was the 3rd number in the revised list) 1 3 7 9 13 15 21 25 27 31 33 37 43 45 49 51 55 57 … (19, 39, 61, 81, 103 … were eliminate)

The lucky number is the 4th number in the revised list.

Input Format

Prompt for and read a single positive integer between 1 and 2066 inclusive. Data will be entered from console. You do not need to edit the input data. Rerun your application to test each test case.

Constraints

Only accept a numerical Input between between 1 and 2066

Output Format

The nth number in the revised list after n – 1 passes as described above.

Sample Input 0

4
Sample Output 0

9


https://www.hackerrank.com/contests/ucsi-national-programming-competition/challenges/unpc-eliminate-unlucky-numbers
