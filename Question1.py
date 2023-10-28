# Creational Design Pattern (Prototype Design Pattern) [40 Marks]
# Clone an object call document using shallow and full recursive deep #(deep copy) method.
# The object should consist of a list of two lists.
# Four copies should be created.
# The output should print something similar (not same as you are free to choose any numbers) following;
# Use python to demonstrate above example. Share code along with a word document including snapshots with detailed explanation.

import copy

# obj with two lists
document = [[1, 2, 3], [4, 5, 6]]

# Clone an object call document using shallow and full recursive deep #(deep copy) method.
shallowCopy = copy.copy(document)
deepCopy = copy.deepcopy(document)

# Four copies
copyOfDoc1 = copy.copy(document)
copyOfDoc2 = copy.copy(document)
copyOfDoc3 = copy.copy(document)
copyOfDoc4 = copy.copy(document)

# Modify the original object to see the differences
copyOfDoc1[1][2] = 15
copyOfDoc2[1].extend([9, 10, 11])
copyOfDoc3[1][0] = '456'
copyOfDoc4[1][0] = '789'

# Print the original and copied objects to observe the differences
print("name=Original list=", document)
print("name=Copy 1 list=", copyOfDoc1)
print("name=Original list=", document)
print("name=Copy 2 list=", copyOfDoc2)
print("name=Original list=", document)
print("name=Copy 3 list=", copyOfDoc3)
print("name=Original list=", document)
print("name=Copy 4 list=", copyOfDoc4)
