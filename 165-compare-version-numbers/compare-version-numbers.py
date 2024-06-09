class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split string based on . map into int
        v1 = version1.split('.')
        v2 = version2.split('.')

        # equlize the array in length
        v1_idx, v2_idx  = len(v1),len(v2)
        if v1_idx>v2_idx:
            v2+=['0']*(v1_idx-v2_idx)
        else:
            v1+=['0']*(v2_idx-v1_idx)

        # find mismatch point
        for rls1, rls2 in zip(v1,v2):
            if rls1!=rls2:
                tmp_rls1 = rls1.lstrip('0') 
                tmp_rls2 = rls2.lstrip('0')

                tmp_rls1  = tmp_rls1 if tmp_rls1 else '0'
                tmp_rls2  = tmp_rls2 if tmp_rls2 else '0'

                if int(tmp_rls1) > int(tmp_rls2):
                    return 1
                elif   int(tmp_rls1) < int(tmp_rls2):
                    return -1
    
        return 0





        