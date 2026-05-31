class solution:
    def isAnagram(self,s,t):
        return sorted(s) == sorted(t)