import numpy
from scipy import stats

speed = [30, 31, 32, 34, 39, 30, 32, 32, 35, 32]

print("MEAN =",numpy.mean(speed))
print("MEDIAN =",numpy.median(speed))
print("MODE =",stats.mode(speed))
print("Standard Deviation =",numpy.std(speed))
print("Variance =",numpy.var(speed))
print("percentile =",numpy.percentile(speed, 70))
