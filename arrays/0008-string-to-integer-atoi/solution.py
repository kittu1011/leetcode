# Original, optimal but ugly solution
class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        i = 0
        n = len(s)
        sign = 1
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '-' or s[i] == '+'):
            if (s[i] == '-'):
                sign = -1
            i += 1
        
        while i < n and s[i].isnumeric():
            if sign == 1 and (result > (((2 ** 31) - 1) // 10) or (result == (((2 ** 31) - 1) // 10) and int(s[i]) > ((2 ** 31) - 1) % 10)):
                return 2 ** 31 - 1
            if sign == -1 and (result > ((2 ** 31) // 10) or (result == ((2 ** 31) // 10) and int(s[i]) > (2 ** 31) % 10)):
                return -(2 ** 31)
        
            result *= 10
            result += int(s[i])

            i += 1

        return result * sign
# More elegant solution and slightly faster 
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)

        result = 0
        sign = 1

        i = 0
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '-' or s[i] == '+'):
            if (s[i] == '-'):
                sign = -1
            i += 1
        
        while i < n and s[i].isnumeric():
            digit = int(s[i])
            # this works because it rewrites the inequality r * 10 + digit > int_max is r > (int_max - digit) / 10
            # since result is int we can use floor division
            # this works for int_min case because its fires when result == int_min
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
        
            result = result * 10 + digit
            i += 1

        return result * sign