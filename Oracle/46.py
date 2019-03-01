def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.dfs(nums,sub)
        return self.res

def dfs(self, Nums, subList):
    # when sublist == len(nums), then add into res
    if len(subList) == len(Nums):
        #print res,subList
        self.res.append(subList[:])
    for m in Nums:
        if m in subList:
            continue
        subList.append(m)
        self.dfs(Nums,subList)
        subList.remove(m)
        
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)