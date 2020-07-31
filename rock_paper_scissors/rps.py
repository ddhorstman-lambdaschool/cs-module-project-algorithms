#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    all_plays = []

    def make_play(n, current_plays=[]):
        nonlocal all_plays
        if n == 0:
            all_plays.append([])
        elif n == 1:
            all_plays.append(current_plays + [plays[0]])
            all_plays.append(current_plays + [plays[1]])
            all_plays.append(current_plays + [plays[2]])
        else:
            make_play(n-1, current_plays + [plays[0]])
            make_play(n-1, current_plays + [plays[1]])
            make_play(n-1, current_plays + [plays[2]])
    make_play(n)
    return all_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
