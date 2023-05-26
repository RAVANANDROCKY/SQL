12. The mean height of a random sample of 100 individuals from a
population is 160. The Standard deviation of the sample is 10. Would
it be reasonable to suppose that the mean height of the population is
165

import math
from scipy.stats import norm

sample_mean = 160
population_mean = 165
standard_deviation = 10
sample_size = 100

standard_error = standard_deviation / math.sqrt(sample_size)
z = (sample_mean - population_mean) / standard_error
p_value = norm.cdf(z) * 2 # two-sided test

print("z-score:", z)
print("p-value:", p_value)