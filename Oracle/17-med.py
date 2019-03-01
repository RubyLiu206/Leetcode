#letter combinations of a phone number
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digit_string_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        res = [""]
        for digit in digits:
            new_res = []
            for ch in digit_string_map[digit]:
                new_res.extend([ele+ch for ele in res])
            res = new_res
        return res