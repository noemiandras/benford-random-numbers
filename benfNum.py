'''
Author: Noemi Andras
Project Title: Benford's Law Applied on RNG (Random Number Generation)
'''
from random import randrange
import matplotlib.pyplot as plt
import csv


# pseudorandom number generation
def pseudo_rand_num(size):
    mill = 1000000
    return [randrange(mill) for i in range(size)]


# read .csv file obtained from RANDOM.org
def read_csv(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    header = next(csvreader)
    lst = []
    for row in csvreader:
        for item in row:
            lst.append(item)
    return lst


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
    #generating pseudo random numbers
    lst = pseudo_rand_num(100)
    numbers, count = count_first_digit(lst)
    show_bar_graph(numbers, count)

    #reading and graphing random numbers generated from RANDOM.ORG
    lst = read_csv("./data/random.org-numbers.csv")
    numbers, count = count_first_digit(lst)
    show_bar_graph(numbers, count)