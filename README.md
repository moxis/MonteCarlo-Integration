# Monte Carlo Integration

A program that lets you evaluate definite integrals of nearly any function with great accuracy using the Monte Carlo method. For more details about the method, refer to the writeup below.

I wrote this program for my IB Mathematics IA research. The writeup can be found [here](https://www.dropbox.com/s/rk69e5pqna4p1wt/Monte%20Carlo%20Simulations%20%28Nguyen%20Van%20Nguyen%29.docx?dl=0).

### Prerequisites
* Python 3+

Install these modules through pip:

```
$ pip install numpy
$ pip install timeit
```

### Usage

Firstly, replace the **y** variable in the code with the function you are planning to evaluate.
```
    try:
        # insert f(x) here
        y = 3*x*x*x
        return y
    except ZeroDivisionError:
        raise ZeroDivisionError
```
Afterwards, run the simulator. It will ask you to define the limits. Below is an example of inputs for evaluating the integral of 3x<sup>3</sup> using 1 million random coordinates from x=0 to x=10.

```
$ python simulator.py
$ Iterations: 1000000
$ Starting range: 0
$ Ending range: 10
```
