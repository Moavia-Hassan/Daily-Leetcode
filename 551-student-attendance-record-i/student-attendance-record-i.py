class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
            if s[i:i+3] == 'LLL':
                return False
        
        if absent > 1 :
            return False
        
        return True
        
        return true
