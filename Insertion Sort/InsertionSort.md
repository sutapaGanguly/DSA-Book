You are given an array of integers. Your task is to sort the array using the Insertion Sort algorithm and print the sorted array.

Insertion Sort works by building a sorted portion of the array one element at a time:

Start with the first element (already sorted).

Pick the next element and insert it into the correct position within the sorted portion.

Repeat until the array is sorted.

Input Format

The first line contains an integer n — the number of elements in the array.

The second line contains n space-separated integers — the elements of the array.

Constraints

1≤𝑛≤1000 1≤n≤1000

−10^4 ≤ 𝑎[𝑖] ≤ 10^4 −10^4 ≤ a[i] ≤ 10^4

Output Format

Print the sorted array in non-decreasing order.

Sample Input 0

5
4 3 2 10 12
Sample Output 0

2 3 4 10 12
Sample Input 1

6
-5 0 2 -2 1 -3
Sample Output 1

-5 -3 -2 0 1 2