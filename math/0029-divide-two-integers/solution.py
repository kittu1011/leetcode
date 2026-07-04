# Optimal solution in python but will have overflow errors in other languages
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        is_neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend) # overflow if dividend is INT_MIN
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            q = 1
            e = divisor

            while dividend >= (e + e): # overflow is e + e > INT_MAX
                e += e
                q += q
            
            dividend -= e
            result += q

        return result if not is_neg else 0 - result
# Elegant solution that fixes edge cases
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        is_neg = (dividend < 0) ^ (divisor < 0)
        dividend = -dividend if dividend >= 0 else dividend # if dividend == INT_MIN it won't overflow as we work with it negative
        divisor = -divisor if divisor >= 0 else divisor

        result = 0
        while dividend <= divisor: # we flip the comparator as the numbers are both negative now
            q = 1
            e = divisor
            # the first boolean checks for overflow; it's equivalent to e + e >= INT_MIN
            while (e >= INT_MIN >> 1) and dividend <= (e << 1):
                e <<= 1 # faster way to multiply by 2
                q <<= 1
            
            dividend -= e
            result += q

        return result if not is_neg else -result