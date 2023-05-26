14.Suppose we have 3 cards identical in form except that both sides
of the first card are colored red, both sides of the second card are
colored black, and one side of the third card is colored red and the
other side is colored black. The 3 cards are mixed up in a hat, and 1
card is randomly selected and put down on the ground. If the upper
side of the chosen card is colored red, what is the probability that the
other side is colored black

# Define the probabilities
P_RB = 1/2
P_B = 1/3
P_notB = 1/3

# Calculate the probability of the upper side being red
P_R = P_RB * P_B + 1 * P_notB

# Calculate the probability of the other side being black given the upper side is red
P_B_given_R = P_RB * P_B / P_R

# Print the result
print("The probability that the other side is black given the upper side is red is:", P_B_given_R)