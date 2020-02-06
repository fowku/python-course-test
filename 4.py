def mix_symbols(string: str):
    """
    Swap neighbour symbols in string
    :param string:str
    :return:str
    """
    string_arr = list(string)
    temp: str

    for i in range(0, len(string_arr) - 1, 2):
        temp = string_arr[i]
        string_arr[i] = string_arr[i + 1]
        string_arr[i + 1] = temp

    return ''.join(string_arr)


print(mix_symbols('ABCDEF'))
