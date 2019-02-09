# Roman to integer
def romantoint(self, s):
    dic = {'M':1000,'D':500 ,'C':100,'L':50,'X':10,'V':5,'I':1}
    z = 0
    for i in range(len(s)-1):
        if s[i] in dic and s[i+1] in dic:
            if dic[s[i]]>=dic[s[i+1]]:
                z+=dic[s[i]]
            if dic[s[i]]<dic[s[i+1]]:
                z-=dic[s[i]]
    return z + dic[s[-1]]

# remember to add the last element in s


