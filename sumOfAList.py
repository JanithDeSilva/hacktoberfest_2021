#This python function sum all the numbers in a list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((10, 2, 3, 0, 7)))
