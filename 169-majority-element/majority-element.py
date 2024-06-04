class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_ele = 0
        cnt = 0

        for ele in nums:
            if  cnt==0:
                m_ele = ele
                cnt+=1
            elif m_ele == ele:
                cnt+=1
            else:
                cnt-=1
        return m_ele       
    
        
        