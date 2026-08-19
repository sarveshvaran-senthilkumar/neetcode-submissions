class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer={}
        n=len(strs)
        for i in range(n):
            ele=strs[i]
            key=''.join(sorted(ele))

            if key not in answer:
                answer[key]=[ele]
            else:
                answer[key].append(ele)
        
        return list(answer.values())
        