def count_numbers(numbers_list: list):
    """
    Count occurrences in numbers_list
    :param numbers_list:list
    :return:dict()
    """
    numbers_set = set(numbers_list)
    result = dict()

    for number in numbers_set:
        result[number] = numbers_list.count(number)

    return result


print(count_numbers([1, 1, 3, 5, 1, 3]))
