class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        ans = letters[0]

        for i in letters[::-1]:
            if i > target:
                ans = i
        
        return ans