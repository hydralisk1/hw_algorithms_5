# When given a list of elements find the two lowest elements. They can be equal to each other or different.
def two_lowest_elements(numbers: list):
    if len(numbers) < 2:
        raise ValueError("The list has to have more than 2 elements at least")
    if type(numbers) is not list:
        raise ValueError("The element has to be the list type")
    
    numbers.sort()
    return [numbers[0], numbers[1]]

numbers = [3, 34, 98, 4, 124, 10503]
print(*two_lowest_elements(numbers))
