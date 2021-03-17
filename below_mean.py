# When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

def below_mean(numbers: list):
    if type(numbers) is not list:
        raise ValueError("The element has to be the list type")
    if len(numbers) == 0:
        raise ValueError("The list has to have more than an element at least")

    mean = sum(numbers) / len(numbers)
    return [i for i in numbers if i < mean]

numbers = [3, 34, 98, 4, 124, 10503]
print(*below_mean(numbers))
