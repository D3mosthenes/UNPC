In this problem, you must follow a set of instructions to travel through the rooms of a museum. The museum is housed in a rectangular building. The building is divided into equal size rooms that can be defined by a grid of a fixed number of rows and columns. Rooms on the outside have doors on their exterior walls to allow entry from the outside. However, corner rooms can only be entered from the north or south. Corner rooms can’t be entered from the east or west. An interior room can be accessed from any adjacent room. The goal is to identify valid museum tours. A valid tour is one that never visits the same room twice and ends with the last instruction causing you to exit the museum.

For each museum tour you are given the grid describing the museum rooms in the form of the number of rows (r) and columns (c). You are also given a starting room. Finally, you are given a series of instructions on how to walk through the rooms. There are three instructions represented by the numbers 0, 1, and 2. Zero is to move straight forward one room. One represents a move one room to the right. A two represents a move one room to the left.

Examples: For this example, the museum has 4 rows and 3 columns. The starting room is S at (0,2). The instructions are 0, 0, 0, 1, 0, 1, 1, 2, 0, 0. The first instruction (0) is to move ahead 1 room placing you in room (1,2). The next instruction (0) is to move ahead 1 room placing you in room (2,3). The next instruction (0) is to move ahead 1 room placing you in room (3,2). The next instruction (1) is to move into the room on your right placing you in room (3,1). The next instruction (0) is to move 1 room ahead placing you in room (3,0). The next instruction (1) is to move into the room on your right placing you in room (2,0). The next instruction (1) is to move into the room on your right placing you in room (2,1). The next instruction (2) is to move into the room on your left placing you in room (1,1). The next instruction (0) is to move 1 room ahead placing you in room (0,1). The next instruction (0) is to move 1 room ahead placing you outside the museum to successfully complete your tour.

image

For this example, the museum again has 4 rows and 3 columns. The starting room S is (0,1). The instructions are 2, 0, 0, 1, 2. The first instruction (2) is to move into the room on your left placing you in room (0,2). The next move (0) is move ahead 1 room. This causes you to exit the museum. Since you still have tour instructions remaining, you have left the building before the tour was over.

image

For this example, the museum still has 4 rows and 3 columns. The starting room is (2,2). The instructions are 0, 2, 2, 2, 0, 1. The first instruction (0) is to move ahead 1 room placing you in room (2,1). The next instruction (2) is to move into the room on your left placing you in room (3,1). The next instruction (2) is to move into the room on your left placing you in room (3,2). The next instruction (2) is to move into the room on your left placing you in room (2,2). This is the second time you have been in this room making this an invalid tour because you have visited the same room more than once.

image

Input Format

Prompt for and read the number of rows and columns in the grid of rooms for the museum. These will be positive integers separated by a space. Both will be greater than 1. Prompt for and read the starting room. These will be two positive integers, or zero, separated by a space. Prompt for and read a combination of zeros, ones, and twos separated by a space and terminated with 99. The 99 terminates the input and is not an instruction for moving through the museum. There will be at least one instruction but there is no maximum number of instructions. Data will be entered from console. You do not need to edit the input data. Rerun your application to test each test case.

Constraints

Your code must accept 3 seperate inputs.

Number of rows then columns
Starting room (row then column)
Instructions
Output Format

Display a single line on the console indicating the result of the tour. There are four possibilities: successful tour; visited same room more than once; tour ended before leaving museum; left building before tour was over.

Sample Input 0

4 3
0 2
0 0 0 1 0 1 1 2 0 0 99    
Sample Output 0

successful tour


https://www.hackerrank.com/contests/ucsi-national-programming-competition/challenges/unpc-museum-tour
