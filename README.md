# Benford's Law Applied on RNG and Population Data 
The project aims to showcase that Benford's Law applies on not any kind of random data, but naturally occurring sets of numbers. 

My quest in this project was to understand what exactly is a "naturally occurring number" and if the expected downwards curve appears using different types of data. I explored the following three scenarios:
1. Graphing pseudo random numbers using RNG (Random Number Generation)
2. Graphing random numbers occurring in the physical world
3. Graphing population data which are considered "naturally occurring"

## What is the Newcomb-Benford Law? 
The law states that taking the first digit of any naturally occurring number set, the majority of the numbers will start with a one, then a two, etc, forming a downward curve when graphed. 

## To run project
```bash
py benfNum.py
```

## Graphing Scenarios Explained
### 1. Pseudo Number Graph 

100 numbers in the interval of 1-1000000 were generated using the python `random` library. 
These numbers are not truly random, hence pseudo random because they can be re generated, making them predictable. 

![Pseudo Number Graph](/graphs/pseudo-number-graph.JPG)

The result is as expected. Because the numbers are not truly random, they don't follow the downwards Benford's curve. 

### 2. Random Number Graph
100 numbers in the interval of 1-1000000 were generated using data from [random.org](https://www.random.org/integers/).
The data provided from the source is random data taken from natural phenomena, and cannot be replicated.

![random.org Number Graph](/graphs/random.org-number-graph.JPG)

After graphing these numbers, it is evident that the numbers don't follow Benford's law. This can be that the numbers don't vary enough because they are from atmospheric noise according to the source.

### 3. State Population Data
The data was taken from the 2020 Census Population divided into each state ([Wikipedia](https://en.wikipedia.org/wiki/2020_United_States_census)).

![2020 Census Graph by First Digit](/graphs/census2020-state-number-graph.JPG)

Overall, the graph follows Benford's Law by the downward curve that can be traced on the graph.
Since the dataset is small (50 entires = 50 states), it is not the best representation of the Law, however it is still valid because on average, it follows the expected distribution. 