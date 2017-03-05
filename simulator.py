import math
import numpy
import timeit
import csv
accuracy = 4
increment = 1 / 10**accuracy
frequency = 10
results = []
# math.sin, math.asin etc...
e = math.e

def function(x):
    try:
        # insert f(x) here
        y = 3*x*x*x
        return y
    except ZeroDivisionError:
        raise ZeroDivisionError

def main():
    positive_hits = 0
    negative_hits = 0

    lower_y = get_min(lower_x, upper_x)
    upper_y = get_max(lower_x, upper_x)
    total_area = ((upper_y if upper_y > 0 else 0)+ (abs(lower_y) if lower_y < 0 else 0)) * abs(upper_x-lower_x)

    sample_y = numpy.random.uniform(low= (0 if lower_y > 0 else lower_y), high= (0 if upper_y < 0 else upper_y), size=(iterations,))
    sample_x = numpy.random.uniform(low = lower_x, high= upper_x, size=(iterations,))
    for i in range(0, iterations):
        if i % frequency == 0:
            results.append([str(positive_hits), str(negative_hits), str(i)])
        rand_y = sample_y[i]
        rand_x = sample_x[i]
        x = function(rand_x)
        if (x >= 0 and rand_y <= x and rand_y >= 0):
            positive_hits += 1
        elif (x <= 0 and rand_y >= x and rand_y <= 0):
            negative_hits += 1
    with open("output.csv", "w", newline='') as csvFile:
        f = csv.writer(csvFile, dialect="excel")
        f.writerow(["Positive", "Negative", "Total", "Total Area = %s" % total_area])
        f.writerows(results)
    calculated_area = ((positive_hits - negative_hits)/iterations * total_area)
    print("Number of hits: ", positive_hits+negative_hits)
    print("\nPositive Ratio: ", positive_hits/iterations)
    print("Negative Ratio: ", negative_hits/iterations)
    print("\nAREA: ", calculated_area)

def get_max(lower_x, upper_x):
    data = []
    for i in range((lower_x)*(10**accuracy), (upper_x)*(10**accuracy) + 1):
        data.append(function(i*increment))
    return max(data)

def get_min(lower_x, upper_x):
    data = []
    for i in range((lower_x)*(10**accuracy), (upper_x)*(10**accuracy) + 1):
        data.append(function(i*increment))
    return min(data)

if __name__ == "__main__":
    iterations = int(input("Iterations: "))
    lower_x = int(input("Starting range: "))
    upper_x = int(input("Ending range: "))
    runtime = timeit.timeit(main, number = 1)
    print("\nRUNTIME: %.4fs" % runtime)
