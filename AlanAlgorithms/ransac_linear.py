from random import shuffle
from scipy import stats
import numpy as np
import math
from pylab import plot,show

"""
RANSAC Linear Regression: in this algorithm, I will implement the RANSAC algorithm to:
Input: a list of pair of points pti = [xi, yi]
Output: a linear regression function y = slope * x + intercept that best fit the acc_ratio of the input points
        other parameters:
            number of loop: num_loop
            sample_ratio: ratio of data to produce the linear regression line.
"""
def ransac_linear(PT, sample_ratio, num_loop, acc_ratio):
    num_sample = int(sample_ratio * len(PT))
    num_acc_ratio = int(acc_ratio * len(PT))
    loop_slope, loop_intercept, loop_error = [], [], []

    for loop_id in range(num_loop):
        shuffle(PT)
        samplePT = PT[:num_sample]
        X, Y = [], []
        for pt in samplePT:
            X.append(pt[0])
            Y.append(pt[1])
        X, Y = np.array(X), np.array(Y)
        slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
        loop_slope.append(slope)
        loop_intercept.append(intercept)

        square_error = []
        for pt in PT:
            square_error.append((pt[1] - (slope * pt[0] + intercept)) ** 2)
        square_error.sort()
        loop_error.append(math.sqrt(sum(square_error[:num_acc_ratio])/num_acc_ratio))

    idx = loop_error.index(min(loop_error))
    print ("Average erorr = ", loop_error[idx])
    return loop_slope[idx], loop_intercept[idx]

def display_ransac_linear_result(PT, slope, intercept):
    X, Y = [], []
    for pt in PT:
        X.append(pt[0])
        Y.append(pt[1])
    X, Y = np.array(X), np.array(Y)
    line = slope * X + intercept
    plot(X, line, 'r-', X, Y, 'o')
    show()

#Test
PT = [(1, 1), (2, 1), (3, 3), (4, 9), (5, 7), (6, 9), (7, 11), (8, 5), (9, 15), (10, 17)]
slope, intercept = ransac_linear(PT=PT, sample_ratio=0.4, num_loop=10, acc_ratio=0.7)
display_ransac_linear_result(PT, slope, intercept)


