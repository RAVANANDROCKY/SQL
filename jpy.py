1. According to a study, the daily average time spent by a user on a
social media website is 50 minutes. To test the claim of this study,
Ramesh, a researcher, takes a sample of 25 website users and finds
out that the mean time spent by the sample users is 60 minutes and
the sample standard deviation is 30 minutes.
Based on this information, the null and the alternative hypotheses
will be:
Ho = The average time spent by the users is 50 minutes
H1 = The average time spent by the users is not 50 minutes
Use a 5% significance level to test this hypothesis.

from scipy.stats import t

# Define the sample statistics and parameters
n = 25 # sample size
x_bar = 60 # sample mean
s = 30 # sample standard deviation
mu_0 = 50 # hypothesized population mean
alpha = 0.05 # significance level

# Calculate the t-statistic and p-value
t_stat = (x_bar - mu_0) / (s / (n**0.5))
p_val = 2 * (1 - t.cdf(abs(t_stat), n-1))

# Print the results
print("Sample size: ", n)
print("Sample mean: ", x_bar)
print("Sample standard deviation: ", s)
print("Null hypothesis: The average time spent by users is ", mu_0, " minutes")
print("Alternative hypothesis: The average time spent by users is not ", mu_0, " minutes")
print("Significance level: ", alpha)
print("Degrees of freedom: ", n-1)
print("T-statistic: ", t_stat)
print("P-value: ", p_val)

# Check if the null hypothesis can be rejected based on the p-value
if p_val < alpha:
    print("We reject the null hypothesis at the", alpha, "level of significance.")
else:
    print("We fail to reject the null hypothesis at the", alpha, "level of significance.")