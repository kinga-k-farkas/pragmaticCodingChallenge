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


def requestPrecisionValue():
    """This function gets an appropriate user input and returns its value"""
    while True:
        precisionRequest = \
        input("Input the number of decimal places to be used for the calculations. To skip, type Skip: ")
        if precisionRequest == "Skip":
            decimalPlaceCount = 2
            break
        else:
            try:
                decimalPlaceCount = int(precisionRequest)
                break
            except ValueError:
                print("Oops. That was not a valid value. Try again...")

    return decimalPlaceCount


def checkPrecisionValue(value):
    """This function checks the value of the requested precision against what is possible on the local machine
     and interacts with user to correct value if needed. Then returns the value"""
    localMaxPrecision = np.finfo(np.longdouble).precision
    if value < 0:
        print("Oops. You have entered a negative value. Try again.")
        return checkPrecisionValue(requestPrecisionValue())
    elif value > localMaxPrecision:
        print ("The max number of decimal places your computer can use is ", localMaxPrecision)
        print("The number of decimal places you requested is not feasible on your computer. Try again.")
        return checkPrecisionValue(requestPrecisionValue())
    else:
        print("All set.")
        print(value)
        return value


def calculateStats(inputArray, decimalPlaces):
    """calculates and  mean, standard deviation and median of an 1 dimensional numpy array of longdoubles to
    decimalPlaceCount decimal places """
    print(round(np.mean(inputArray), decimalPlaces), round(np.std(inputArray), decimalPlaces),
          round(np.median(inputArray), decimalPlaces))


#***************************************************

print("Configuring accuracy.")

decimalPlaceCount = checkPrecisionValue(requestPrecisionValue())
print(decimalPlaceCount)

inputValues = []

print("Please input your list -- one number per line. Type Exit when finished.")

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break

    else:
        try:
            num = np.longdouble(line.rstrip())
            inputValues.append(num)
            print(inputValues)
            calculateStats(inputValues, decimalPlaceCount)

        except ValueError:
            print("Please input numbers only...")
            print("Type Exit to quit.")


print("Done")