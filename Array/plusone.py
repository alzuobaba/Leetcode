class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # sum = 1
        # retsum = []
        # digits = digits[::-1]
        # for i in range(len(digits)):
        #     sum +=digits[i]*10**i
        # lenth = len(str(sum))
        #
        # sum = str(sum)
        # for i in range(lenth):
#         #     retsum.append(int(sum[i]))
# ----------
#         s = ''
#         ret = []
#         for i in digits:
#             s += str(i)
#         s = str(int(s)+1)
#         for i in s:
#             ret.append(i)
# # -------------
#         for i in range(1,len(digits)+1):
#             if digits[-i] +1 ==10:
#                 digits[-i] = 0
#                 digits[-]
#         return ret
        length = len(digits)
        for i in range(length-1,-1,-1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                if i==0:
                    digits.insert(0,1)
                    return digits
            else:
                return digits


print Solution().plusOne([9,9,9])