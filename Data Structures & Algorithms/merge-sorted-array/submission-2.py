class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m1Len = len(nums1) -1
        m1Ptr = m - 1
        n2Ptr = n - 1

        while m1Ptr >= 0 and n2Ptr >= 0:
            if nums2[n2Ptr] >= nums1[m1Ptr]:
                nums1[m1Len]  = nums2[n2Ptr]
                n2Ptr -= 1
            else:
                nums1[m1Len]  = nums1[m1Ptr]
                m1Ptr -= 1
            m1Len -= 1
            
        if n2Ptr >=0:
            nums1[0:m1Len+1] = nums2[0:m1Len+1]

        
        
            

        
        