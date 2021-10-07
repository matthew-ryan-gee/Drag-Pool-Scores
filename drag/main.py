import pandas as pd
import numpy as np
import xlrd
from nltk.metrics import *



elim1 = "JTLEDBUORGKS"
elim2 = "JTLEDBUOGRKS"

dataset = pd.read_csv('drag.csv')

print(dataset)
participants = []

from math import floor, ceil


# Function to calculate the
# Jaro Similarity of two s
def jaro_distance(s1, s2):
    # If the s are equal
    if (s1 == s2):
        return 1.0

    # Length of two s
    len1 = len(s1)
    len2 = len(s2)

    # Maximum distance upto which matching
    # is allowed
    max_dist = floor(max(len1, len2) / 2) - 1

    # Count of matches
    match = 0

    # Hash for matches
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)

    # Traverse through the first
    for i in range(len1):

        # Check if there is any matches
        for j in range(max(0, i - max_dist),
                       min(len2, i + max_dist + 1)):

            # If there is a match
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break

    # If there is no match
    if (match == 0):
        return 0.0

    # Number of transpositions
    t = 0
    point = 0

    # Count number of occurances
    # where two characters match but
    # there is a third matched character
    # in between the indices
    for i in range(len1):
        if (hash_s1[i]):

            # Find the next matched character
            # in second
            while (hash_s2[point] == 0):
                point += 1

            if (s1[i] != s2[point]):
                point += 1
                t += 1
    t = t // 2

    # Return the Jaro Similarity
    return (match / len1 + match / len2 +
            (match - t + 1) / match) / 3.0



class Person:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0

    def to_string(self):
        print(self.name)
        print(self.score3)

for entry in dataset.iteritems():
    name = entry[0]
    order = entry[1].to_string()
    order = order.replace('0', "")
    order = order.replace(" ", "")
    participants.append(Person(name, order))



for i in participants:
    i.score1 = jaro_distance(elim1, i.order)
    i.score2 = jaro_distance(elim2, i.order)
    i.score3 = max(i.score1,i.score2)

best = 0
best_p = ""

participants.sort(key=lambda x: x.score3, reverse=True)
count = 0
last = 1
for i in participants:
    if i.score3 > best:
        best = i.score3
        best_p = i.name
    print("placement: ", count)
    if i.score3 < last:
        count += 1
    last = i.score3
    i.to_string()


print(best_p, best)









