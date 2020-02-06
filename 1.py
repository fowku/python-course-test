def check_number(numbers_list: list, n: int):
    """
    Check, if there is number in list.
    If not, add to the end of the list.
    :param numbers_list:list
        for ex. [1, 4, 23, 12, 32]
    :param n:int
    :return:list
    """
    if n in numbers_list:
        print('There is n in numbers_list already!')
    else:
        numbers_list.append(n)

    return numbers_list


print(check_number([1, 5, 16, 75], 2))
