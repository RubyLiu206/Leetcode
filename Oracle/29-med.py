#divide two intergers
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if (dividend >= 0) == (divisor >= 0) else -1
        dd = abs(dividend)
        dr = abs(divisor)
        if dd < dr:
            return 0
        if dd == dr:
            return sign
        if dr == 1:
            dd = dd if sign > 0 else -dd
            return min(2**31-1, dd)
            
        res = 1
        while dd > dr+dr:
            dr += dr
            res += res
        return sign*(res + self.divide(dd-dr, abs(divisor)))