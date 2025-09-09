# 0067.Add_Binary

'''
Build-in function:
- int(a, 2)
- "{0:b}".format(...) → Convert the argument into its binary representation as a string.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2 ) + int(b, 2))