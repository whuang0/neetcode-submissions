class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # a set for each row/column/subbox
        # O(9n) + O(9n) + O(9n)
        # have an array to store the sets for the rows, columns, subboxArray
        # 9 for the rows 9 for columns 9 subboxes
        # for a number it's in a row/column and subbox, 
        # as you iterate through you add to the respective row/column/subbox
        # if any duplicate is found in a set return false
        # if is not duplicate the value is saved in the set
        
        # for the subbox check that the numbers across/ under/ in box are unique
        # iterate through rows keeping tab of location of the matrix

        rowArray = [set() for i in range(9)]
        columArray = [set() for i in range(9)]
        subboxArray = [set() for i in range(9)]

        for i,row in enumerate(board):                
            for j,num in enumerate(row):
                if num != ".":
                    boxindex = (i // 3) * 3 + (j // 3) 

                    if num in rowArray[i] or num in columArray[j] or num in subboxArray[boxindex]:
                        return False
                    rowArray[i].add(num)
                    columArray[j].add(num)
                    subboxArray[boxindex].add(num)
        return True


            