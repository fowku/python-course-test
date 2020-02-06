class Matrix:
    def __init__(self, rows: int, columns: int):
        """
        Constructor, creates a matrix with the shape (rows, columns)
        Fill it with 0
        :param rows:int
        :param columns:int
        """
        self._matrix = [[0] * columns for _ in range(rows)]

    def __getitem__(self, row: int):
        """
        [] operator overload
        :param row:int
        :return:list
        """
        return self._get_row(row)

    def _get_row(self, row: int):
        """
        Get row from matrix
        :param row:int
        :return:list
        """
        return self._matrix[row]


x = Matrix(5, 5)

x[2][1] = 8
x[1][1] = 31

print(x[2][1], x[1][1], x[2][2])
