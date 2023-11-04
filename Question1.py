# Creational Design Pattern (Prototype Design Pattern) [40 Marks]
# Clone an object call document using shallow and full recursive deep #(deep copy) method.
# The object should consist of a list of two lists.
# Four copies should be created.
# The output should print something similar (not same as you are free to choose any numbers) following;
# Use python to demonstrate above example. Share code along with a word document including snapshots with detailed explanation.

import copy

# obj with two lists
document = [["apple", "banana", "grapes", "blueberry"], ["yellow", "green", "red", "orange"]]

# Clone an object called document using shallow and deep copy methods.
shallowCopy = copy.copy(document)
deepCopy = copy.deepcopy(document)

# Four copies
shallowCopyOfDoc1 = copy.copy(document)
shallowCopyOfDoc2 = copy.copy(document)
shallowCopyOfDoc3 = copy.copy(document)
shallowCopyOfDoc4 = copy.copy(document)

deepCopy1 = copy.deepcopy(document)
deepCopy2 = copy.deepcopy(document)
deepCopy3 = copy.deepcopy(document)
deepCopy4 = copy.deepcopy(document)

# Modify the original object to see the differences
document[1][2] = "passion fruit"
document[1][0] = 'mango'
document[1][0] = 'honey'
document[1].extend(["triangle", "circle", "square", "cube"])

# Print the original and copied objects to observe the differences

# Original document
print("Original Document:")
print(document)
print()

# Shallow Copies
print("Shallow Copies:")
print("Shallow Copy (shallowCopy):")
print(shallowCopy)
print("Shallow Copy (shallowCopyOfDoc1):")
print(shallowCopyOfDoc1)
print("Shallow Copy (shallowCopyOfDoc2):")
print(shallowCopyOfDoc2)
print("Shallow Copy (shallowCopyOfDoc3):")
print(shallowCopyOfDoc3)
print("Shallow Copy (shallowCopyOfDoc4):")
print(shallowCopyOfDoc4)
print()

# Deep Copies
print("Deep Copies:")
print("Deep Copy (deepCopy):")
print(deepCopy)
print("Deep Copy (deepCopy1):")
print(deepCopy1)
print("Deep Copy (deepCopy2):")
print(deepCopy2)
print("Deep Copy (deepCopy3):")
print(deepCopy3)
print("Deep Copy (deepCopy4):")
print(deepCopy4)
