def count_lines(file_name: str):
    """
    Count number of lines in file
    :param file_name:str
    :return:int
    """
    number_of_rows = 0

    with open(file_name) as file:
        for line in file:
            number_of_rows += 1

    return number_of_rows


print(count_lines('2.py'))
