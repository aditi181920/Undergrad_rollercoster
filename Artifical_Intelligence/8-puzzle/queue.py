import sys

import copy

q = []


def compare(s, g):
    if s == g:

        return (1)

    else:

        return (0)


def find_pos(s):
    for i in range(len(s)):

        for j in range(len(s[0])):

            if s[i][j] == 0:
                return ([i, j])


def up(s, pos):
    i = pos[0]

    j = pos[1]

    if i > 0:

        temp = copy.deepcopy(s)

        temp[i][j] = temp[i - 1][j]

        temp[i - 1][j] = 0

        return (temp)

    else:

        return (s)


def down(s, pos):
    i = pos[0]

    j = pos[1]

    if i < 2:

        temp = copy.deepcopy(s)

        temp[i][j] = temp[i + 1][j]

        temp[i + 1][j] = 0

        return (temp)

    else:

        return (s)


def right(s, pos):
    i = pos[0]

    j = pos[1]

    if j < 2:

        temp = copy.deepcopy(s)

        temp[i][j] = temp[i][j + 1]

        temp[i][j + 1] = 0

        return (temp)

    else:

        return (s)


def left(s, pos):
    i = pos[0]

    j = pos[1]

    if j > 0:

        temp = copy.deepcopy(s)

        temp[i][j] = temp[i][j - 1]

        temp[i][j - 1] = 0

        return (temp)

    else:

        return (s)


def enqueue(s):
    global q

    q = q + [s]


def dequeue():
    global q

    # find the state having minimum mis matches with the goal state

    elem = q[0]

    del q[0]

    return (elem)


def search(s, g):
    curr_state = copy.deepcopy(s)

    if s == g:
        return

    c = 0

    while (1):

        pos = find_pos(curr_state)

        new = up(curr_state, pos)

        if new != curr_state:

            if new == g:

                print("found")

                return

            else:

                enqueue(new)

        new = down(curr_state, pos)

        if new != curr_state:

            if new == g:

                print("found")

                return

            else:

                enqueue(new)

        new = right(curr_state, pos)

        if new != curr_state:

            if new == g:

                print("found")

                return

            else:

                enqueue(new)

        new = left(curr_state, pos)

        if new != curr_state:

            if new == g:

                print("found")

                return

            else:

                enqueue(new)

        if len(q) > 0:

            curr_state = dequeue()

        else:

            print("not found")

            return


def main():
    s = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    g = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]

    pos = find_pos(s)

    search(s, g)


if __name__=='__main__':
    main()