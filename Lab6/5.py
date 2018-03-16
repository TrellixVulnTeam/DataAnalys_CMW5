# HW 2 - Arjun Soin

import numpy as np
import scipy as sp
import pylab as py
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import csv
from numpy import sin, cos, pi, sqrt
import scipy


file = open('san-francisco-2014.csv')
csv_file = csv.reader(file)
payroll_list = []
payroll_list_float = []
overtime_pay_float = []
overtime_pay = []

for row in csv_file:
	payroll_list.append(row[7])
	overtime_pay.append(row[3])

payroll_list.pop(0)
overtime_pay.pop(0)

for elem in payroll_list:
	payroll_list_float.append(float(elem))

for elem in overtime_pay:
	overtime_pay_float.append(float(elem))


mean = np.mean(payroll_list_float)
print("Mean: ", mean)

SD = np.std(payroll_list_float)
print("Standard Deviation: ", SD)

bin_array = []

for i in range(530):
	bin_array.append(i*1000)


data = pd.read_csv("san-francisco-2014.csv", index_col = 0)
lm = smf.ols(formula='TPB ~ BP', data=data).fit()
print("The linear regression model is: ", lm.params[0], "+ ", lm.params[1], "*BP")

plt.hist(payroll_list_float, bins = bin_array)
plt.xlabel('Total Pay and Benefits for 2014')
plt.ylabel('Number of people')
plt.show()