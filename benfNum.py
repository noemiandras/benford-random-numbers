'''
Author: Noemi Andras
Project Title: Benford's Law Applied on RNG (Random Number Generation)
'''
from random import randrange


# pseudorandom number generation
def pseudo_rand_num(size):
    mill = 1000000
    return [randrange(mill) for i in range(size)]


if __name__ == "__main__":
    print("Hello World")
    print("Random values generated: \n")
    print(pseudo_rand_num(100))
