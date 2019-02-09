#intersection of two arrays
def intersection(self, nums1, nums2):
    dic = {}
    result = []
    if len(nums1) < len(nums2):
        temp = nums1
        nums1= nums2
        nums2 = temp
    for i in range(len(nums1)):
        if nums1[i] in dic:
            dic[nums1[i]]+=1
        else:
            nums1[i] = 1
    for j in range(len(nums2)):
        if nums2[j] in dic and nums2[j] not in result:
            result.append[nums2[j]]
    return result
    