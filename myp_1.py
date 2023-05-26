13.In a study, physicians were asked what the odds of breast cancer
would be in a woman who was initially thought to have a 1% risk of
cancer but who ended up with a positive mammogram result (a
mammogram accurately classifies about 80% of cancerous tumors
and 90% of benign tumors.) 95 out of a hundred physicians estimated
the probability of cancer to be about 75%. Do you agree

import random

# Simulate 100,000 women with a 1% risk of cancer
num_women = 100000
num_cancer = int(num_women * 0.01)
women = ['C'] * num_cancer + ['not C'] * (num_women - num_cancer)

# For women with cancer, 80% of mammograms are positive
# For women without cancer, 10% of mammograms are positive
results = []
for woman in women:
    if woman == 'C':
        if random.random() < 0.8:
            results.append('positive')
        else:
            results.append('negative')
    else:
        if random.random() < 0.1:
            results.append('positive')
        else:
            results.append('negative')

# Calculate the proportion of positive mammograms for women with and without cancer
cancer_results = [r for r in results[:num_cancer] if r == 'positive']
not_cancer_results = [r for r in results[num_cancer:] if r == 'positive']
prop_cancer = len(cancer_results) / num_cancer
prop_not_cancer = len(not_cancer_results) / (num_women - num_cancer)

print('Proportion of positive mammograms for women with cancer:', prop_cancer)
print('Proportion of positive mammograms for women without cancer:', prop_not_cancer)