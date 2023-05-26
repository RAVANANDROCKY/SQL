Given the following distribution of returns, determine the lower
quartile:
{10 25 12 21 19 17 16 11 15 19}

import numpy as np

returns = [10, 25, 12, 21, 19, 17, 16, 11, 15, 19]
lower_quartile = np.percentile(returns, 25)

print(lower_quartile)