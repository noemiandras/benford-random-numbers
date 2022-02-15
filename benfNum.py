'''
Author: Noemi Andras
Project Title: Benford's Law Applied on RNG (Random Number Generation)
'''
from random import randrange
import matplotlib.pyplot as plt


# pseudorandom number generation
def pseudo_rand_num(size):
    mill = 1000000
    return [randrange(mill) for i in range(size)]


def count_first_digit(lst):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for n in lst:
        n_str = str(n)
        first_digit = int(n_str[0])
        count[first_digit] += 1

    return numbers, count


def show_bar_graph(num, count):
    fig = plt.figure()
    plt.bar(num, count)

    plt.title('Testing Benford\'s Law Hypothesis')
    plt.ylabel('First Digit counts')
    plt.show()


if __name__ == "__main__":
    print("Hello World")
    print("Random values generated: \n")

    lst = pseudo_rand_num(100)
    numbers, count = count_first_digit(lst)
    show_bar_graph(numbers, count)