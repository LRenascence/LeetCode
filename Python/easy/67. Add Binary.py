"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
# very long code, not cool
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        returnStr = ""
        ifAddition = False
        length = min(len(a), len(b))
        i = -1
        while i >= -length:
            num = int(a[i]) + int(b[i])
            if ifAddition:
                num += 1
            if num > 1:
                ifAddition = True
                returnStr = str(num - 2) + returnStr
            else:
                returnStr = str(num) + returnStr
                ifAddition = False
            i -= 1
        if len(a) > len(b):
            i = len(a) - len(b) - 1
            while i >= 0:
                num = int(a[i])
                if ifAddition:
                    num += 1
                if num > 1:
                    ifAddition = True
                    returnStr = "0" + returnStr
                else:
                    ifAddition = False
                    returnStr = str(num) + returnStr
                i -= 1
            if ifAddition:
                returnStr = "1" + returnStr
            return returnStr
        elif len(a) < len(b):
            i = len(b) - len(a) - 1
            while i >= 0:
                num = int(b[i])
                if ifAddition:
                    num += 1
                if num > 1:
                    ifAddition = True
                    returnStr = "0" + returnStr
                else:
                    ifAddition = False
                    returnStr = str(num) + returnStr
                i -= 1
            if ifAddition:
                returnStr = "1" + returnStr
            return returnStr
        else:
            if ifAddition:
                returnStr = "1" + returnStr
            return returnStr

# other's short code, cool
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        returnStr = ""
        while i >= 0 or j >= 0 or c == 1:
            if i >= 0:
                c += int(a[i])
            if j >= 0:
                c += int(b[j])
            returnStr = str(c % 2) + returnStr
            c = int(c / 2)
            i -= 1
            j -= 1
        return returnStr