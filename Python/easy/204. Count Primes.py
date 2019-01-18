"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0
        for i in range(2, int(n / 2) + 1):
            if isPrime[i]:
                isPrime[i * i : n : i] = [0] * len(isPrime[i * i : n : i])
        return sum(isPrime)