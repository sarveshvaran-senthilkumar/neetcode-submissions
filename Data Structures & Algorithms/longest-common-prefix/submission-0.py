class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        long=strs[0]

        for i in strs[1:]:
            while not i.startswith(long):
                long=long[:-1]

            if long=="":
                return ""
        return long 
        