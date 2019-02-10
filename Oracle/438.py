#find all anagrams in a string

class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import itertools
        result = []
        p_len, s_len = len(p), len(s)
        if s_len < p_len:
            return result

        p_per = []
        for i in itertools.permutations(p): #通过itertools中的permutations产生所有组合
            p_per.append(''.join(i))

        for i in range(s_len):
            if i + p_len <= s_len and s[i:i + p_len] in p_per:
                result.append(i)
        return result



class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = [0] * 26
        result = []
        for c in p:
            m[ord(c) - 97] += 1
        current = [0] * 26
        length = len(p)
        for i, c in enumerate(s):
            current[ord(c) - 97] += 1
            if i >= length:
                current[ord(s[i - length]) - 97] -= 1
            if current == m:
                result.append(i - length + 1)
        return result


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        s_len, p_len = len(s), len(p)
        pChar, sChar = Counter(p), Counter()

        result = []
        for i in range(s_len):
            sChar[s[i]] += 1
            if i >= p_len:
                sChar[s[i - p_len]] -= 1
                if sChar[s[i - p_len]] == 0:
                    del sChar[s[i - p_len]]

            if pChar == sChar:
                result.append(i - p_len + 1)
        return result1

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        s_len, p_len = len(s), len(p)
        count = p_len
        pChar = Counter(p)

        result = []
        for i in range(s_len):
            if pChar[s[i]] >= 1:
                count -= 1
            pChar[s[i]] -= 1
            if i >= p_len:
                if pChar[s[i - p_len]] >= 0:
                    count += 1
                pChar[s[i - p_len]] += 1
            if count == 0:
                result.append(i - p_len + 1)

        return result