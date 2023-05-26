5. For a certain type of computer, the length of time between charges of
the battery is normally distributed with a mean of 50 hours and a
standard deviation of 15 hours. John owns one of these computers
and wants to know the probability that the length of time will be
between 50 and 70 hours.

from scipy.stats import norm

mean = 50
std_dev = 15

lower_bound = (50 - mean) / std_dev
upper_bound = (70 - mean) / std_dev

prob = norm.cdf(upper_bound) - norm.cdf(lower_bound)

print("The probability that the length of time is between 50 and 70 hours is:", prob)