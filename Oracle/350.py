# intersection of two array 2
def intersect(self, nums1, nums2):
    record = {}
    result = []
    for i in nums1:
        if i in record:
            record[i]+=1
        else:
            record[i]=1
    for i in nums2:
		if i in record and record[i]>0:
			result.append(i)
			record[i]-=1
				
		return result