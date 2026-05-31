class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)!=len(t):
        return False
      res ={}
      for c in s:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
      for c in t:
        if c in res:
            res[c] -= 1
        else:
            return False
      for c in res.values():
        if c != 0:
            return False
      return True
               
            
        
    
      
        