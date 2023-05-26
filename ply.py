6.  It is estimated that 50% of emails are spam emails. Some software
has been applied to filter these spam emails before they reach your
inbox. A certain brand of software claims that it can detect 99% of
spam emails, and the probability for a false positive (a non-spam
email detected as spam) is 5%. Now if an email is detected as spam,
then what is the probability that it is in fact a non-spam email

p_b_given_a = 0.99
p_not_a = 0.5
p_b_given_not_a = 0.05

p_a = 1 - p_not_a

p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a

p_a_given_b = p_b_given_a * p_a / p_b

print("Probability that an email detected as spam is not actually spam:", 1 - p_a_given_b)