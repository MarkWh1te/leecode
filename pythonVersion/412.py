# -*- coding: utf-8 -*-


# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution(object):
    @staticmethod
    def replace(n):
        if n % 3 == 0 and n % 5 ==0:
            return 'FizzBuzz'
        if n % 3 == 0:
            return 'Fizz'
        if n % 5 == 0:
            return 'Buzz'
        return n

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return map(self.replace,[i for i in range(1,n+1)])

a = Solution()
print a.fizzBuzz(15)
