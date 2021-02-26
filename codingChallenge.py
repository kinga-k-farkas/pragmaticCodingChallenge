"""Write a program that reads a list of numbers and for each number outputs an estimate of the running mean,
running standard deviation, and running median.  The input should be read from standard in, with one number per line.
For each line of input, the program should print to standard out the estimated running mean, running standard deviation,
and running median.  That is, given the input

1
2
3
137.036

the program should output values close to

1,0,1
1.5,0.5,1.5
2,0.816,2
35.759,58.477,2.5  """


import sys
import numpy as np
inputValues = []

print("Please input your list -- one number per line. Type Exit when finished.")
for line in sys.stdin:
    try:
        num = float(line)
        print("num:", num)
        inputValues.append(num)
        print(inputValues)
        print(np.mean(inputValues), np.std(inputValues), np.median(inputValues))

    except ValueError:
        print("Please input numbers only...")
        print("Remember, type Exit when finished.")
    if 'Exit' == line.rstrip():
        break

print(inputValues)
print(1 + np.finfo(np.longdouble).eps)
print(1 + np.finfo(np.double).eps)
print("Done")