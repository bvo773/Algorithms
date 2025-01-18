class Solution:
    def isValidSudoku(self, board: list[list[str]])->bool:
        return False





class NestedList:

    def twoDMatrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        print(matrix)
        print(matrix[0][1]) #accessing, output 2 
    
    def iteratingTwoDMatrix(self):
        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        for row in matrix:
            for item in row:
                print(item, end= ' ')
            print()
nested = NestedList()
nested.twoDMatrix()
