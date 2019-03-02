class Solution(object):
    def setZeroes(self, matrix):
      
        index_i = []
        index_j = []
        #Collecting the index of i and j where they are 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index_i.append(i)
                    index_j.append(j)
        #Again looping and setting all 0 to rows
        for i in range(len(matrix)):
            if i in index_i:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
                    
        #Looping and setting all zeros to column
        for j in range(len(matrix[0])):
            if j in index_j:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
      