#pascal's triangle
class Solution(object):
    def generate(self, numRows):
        res, row = [], [1]
        for _ in range(numRows):
            res.append(row)
            row = [1] + [row[i]+row[i-1] for i in range(1, len(row))] + [1]
        return res