class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer={}
        #n=len(strs)
        
        for s in strs:
            key=''.join(sorted(s))

            if key not in answer:
                answer[key]=[]
            answer[key].append(s)
        
        return list(answer.values())