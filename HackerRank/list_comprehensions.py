'''
Problem statement
------------------
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''


def list_comprehensions(x, y, z, n):
    print([[val_x, val_y, val_z] for val_x in range(0, x+1) for val_y in range(0, y+1) for val_z in range(0, z+1) if val_x + val_y + val_z != n])


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_comprehensions(x, y, z, n)