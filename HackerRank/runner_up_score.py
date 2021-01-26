'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Sample Input:
5
2 3 6 6 5

Sample Output:
5
'''


def find_runner_up(n, input_list):
    highest = max(input_list[0], input_list[1])
    runner_up = min(input_list[0], input_list[1])

    if (highest == runner_up):
        i = 2;
        while (highest == runner_up):
            runner_up = min(highest, input_list[i])
            i = i + 1

    for i in range(2, n):
        if (input_list[i] >= highest):
            highest = input_list[i]
        elif (input_list[i] > runner_up and input_list[i] != runner_up):
            runner_up = input_list[i]

    print(runner_up)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    input_list = list(arr)
    input_list.sort(reverse=True)
    find_runner_up(n, input_list)